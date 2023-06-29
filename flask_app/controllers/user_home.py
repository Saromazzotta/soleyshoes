from flask_app import app
from flask_app.models.Shoe import Shoe
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

from flask import render_template, redirect, request, session, flash, jsonify
import requests, json

bcrypt = Bcrypt(app)

@app.route('/user/home')
def user_home():
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'id' : session['user_id']
    }
    return render_template('user/user_home.html', user = User.get_by_id(data), shoes = Shoe.get_all_shoes())

@app.route('/shoe/user/<int:id>')
def get_user_shoe(id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': id
    }

    return render_template('user/user_show_shoe.html', shoe = Shoe.get_one(data), shoes = Shoe.get_3_shoes())

@app.route('/shoe/user/brand/nike')
def get_nikes_user():

    return render_template('user/user_nike.html', shoes = Shoe.get_nike())

@app.route('/shoe/user/brand/adidas')
def get_adidas_user():

    return render_template('user/user_adidas.html', shoes = Shoe.get_adidas())

@app.route('/shoe/user/brand/jordan')
def get_jordan_user():

    return render_template('user/user_jordan.html', shoes = Shoe.get_jordan())

@app.route('/shoe/user/brand/puma')
def get_puma_user():

    return render_template('user/user_puma.html', shoes = Shoe.get_puma())

@app.route('/shoe/user/deals')
def get_deals_user():

    return render_template('user/user_deals.html', shoes = Shoe.get_deals()) 

