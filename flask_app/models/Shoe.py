from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

# class for individual shoes. will need to be updated to hold photo
class Shoe():


    def __init__(self, data):

        self.id = data['id']
        self.brand = data['brand']
        self.silhoutte = data['silhoutte']
        self.colorway = data['colorway']
        self.market_value = data['market_value']
        self.gender = data['gender']
        self.name = data['name']
        self.retailPrice = data['retailPrice']
        self.story = data['story']
        self.image = data['image']
        
# saves instance of the shoe from the API call
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO shoes (brand, silhoutte, colorway, market_value, gender, name, retailPrice, story, image) VALUES (%(brand)s,%(silhoutte)s,%(colorway)s,%(market_value)s,%(gender)s,%(name)s,%(retailPrice)s,%(story)s,%(image)s);'

        return connectToMySQL('kicks_kartel').query_db(query, data)

# gets all shoe instances currently in database
    @classmethod
    def get_all_shoes(cls):

        query = 'SELECT * FROM shoes LIMIT 12;'



        shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

        shoes = []

        for shoe in shoes_from_db:
                shoes.append(cls(shoe))

        return shoes
