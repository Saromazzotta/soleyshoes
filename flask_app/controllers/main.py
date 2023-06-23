from flask_app import app
from flask_app.models import Shoe

from flask import render_template, redirect, request, session, flash, jsonify
import requests

@app.route('/')
def home():
    # temporary for testing purposes
    # Below method is for adding shoes. doesnt seem to make duplicates when left on but slows initial load of the home page. 
    # this might be changed later to input a data into the query from a form
    # probably might be best to add top 100 shoes from top brands into SQL database for speed
    # to erase the need for an external API essentially just making our own


    # url = "https://the-sneaker-database.p.rapidapi.com/sneakers"

    # querystring = {"limit":"10"}

    # headers = {
	# "X-RapidAPI-Key": "56c2bc8b30msh20ce65860904590p11203bjsn1ce9c783dc28",
	# "X-RapidAPI-Host": "the-sneaker-database.p.rapidapi.com"
    # }

    # response = requests.get(url, headers=headers, params=querystring)


    
    # for i in range(0,10,1):

    #     shoe = {
    #         'id': response.json()['results'][i]['id'],
    #         'brand': response.json()['results'][i]['brand'],
    #         'silhoutte': response.json()['results'][i]['silhouette'],
    #         'colorway': response.json()['results'][i]['colorway'],
    #         'market_value': response.json()['results'][i]['estimatedMarketValue'],
    #         'gender': response.json()['results'][i]['gender'],
    #         'name': response.json()['results'][i]['name'],
    #         'retailPrice': response.json()['results'][i]['retailPrice'],
    #         'story': response.json()['results'][i]['story']
    #     }
    #     Shoe.Shoe.save(shoe)
    


    return render_template('home.html', shoes = Shoe.Shoe.get_all_shoes())