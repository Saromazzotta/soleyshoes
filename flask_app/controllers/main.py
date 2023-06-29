from flask_app import app
from flask_app.models.Shoe import Shoe
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

from flask import render_template, redirect, request, session, flash, jsonify
import requests, json

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    # temporary for testing purposes
    # Below method is for adding shoes. doesnt seem to make duplicates when left on but slows initial load of the home page. 
    # this might be changed later to input a data into the query from a form
    # probably might be best to add top 100 shoes from top brands into SQL database for speed
    # to erase the need for an external API essentially just making our own


    # url = "https://the-sneaker-database.p.rapidapi.com/sneakers"


    # querystring = {"brand":"Puma", "limit":"100"}
    # querystring_2 = {"brand":"Adidas", "limit":"100"}
    # querystring_3 = {"brand":"Jordan", "limit":"100"}
    # querystring_4 = {"brand":"Puma", "limit":"100"}

    # headers = {
	# "X-RapidAPI-Key": "56c2bc8b30msh20ce65860904590p11203bjsn1ce9c783dc28",
	# "X-RapidAPI-Host": "the-sneaker-database.p.rapidapi.com"
    # }

    # response = requests.get(url, headers=headers, params=querystring)

    

    # for i in range(0,100,1):

    #     shoe = {
    #         'brand': response.json()['results'][i]['brand'],
    #         'silhoutte': response.json()['results'][i]['silhouette'],
    #         'colorway': response.json()['results'][i]['colorway'],
    #         'market_value': response.json()['results'][i]['estimatedMarketValue'],
    #         'gender': response.json()['results'][i]['gender'],
    #         'name': response.json()['results'][i]['name'],
    #         'retailPrice': response.json()['results'][i]['retailPrice'],
    #         'story': response.json()['results'][i]['story'],
    #         'image': response.json()['results'][i]['image']['original']
    #     }
    #     Shoe.save(shoe)

    return render_template('home.html', shoes = Shoe.get_all_shoes())

@app.route('/register')
def register_user_page():

    return render_template('register/register.html')

@app.route('/register/user', methods = ['POST'])
def register_user():

    if User.validate_user(request.form):
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email': request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(data)
        session['user_id'] = id
        return redirect('/')
    else:
        return redirect('/register')
    
    
@app.route('/shoe/<int:id>')
def get_shoe(id):

    data = {
        'id': id
    }

    return render_template('shoe/show_shoe.html', shoe = Shoe.get_one(data), shoes = Shoe.get_3_shoes())

@app.route('/shoe/brand/nike')
def get_nikes():

    return render_template('shoe/nike.html', shoes = Shoe.get_nike())

@app.route('/shoe/brand/adidas')
def get_adidas():

    return render_template('shoe/adidas.html', shoes = Shoe.get_adidas())

@app.route('/shoe/brand/jordan')
def get_jordan():

    return render_template('shoe/jordan.html', shoes = Shoe.get_jordan())

@app.route('/shoe/brand/puma')
def get_puma():

    return render_template('shoe/puma.html', shoes = Shoe.get_puma())

@app.route('/shoe/deals')
def get_deals():

    return render_template('shoe/deals.html', shoes = Shoe.get_deals())
    
@app.route('/login')
def login_user():

    return render_template('login/login.html')

@app.route('/login/user', methods = ['POST'])
def login():

    user = User.get_by_email(request.form)

    if not user:
        flash('invalid credentials', 'login')
        return redirect('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('invalid credentials', 'login')
        return redirect('/login')
    session['user_id'] = user.id
    return redirect('/user/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')