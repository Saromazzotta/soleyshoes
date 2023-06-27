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


    # querystring = {"brand":"Nike", "limit":"100"}
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
    #         'story': response.json()['results'][i]['story']
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
        return redirect('register')
    
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
    return redirect('/')