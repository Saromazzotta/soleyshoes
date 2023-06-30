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

        # gets all shoe instances currently in database at random for home
        @classmethod
        def get_all_shoes(cls):

                query = 'SELECT * FROM shoes order by rand() limit 12;'



                shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

                shoes = []

                for shoe in shoes_from_db:
                        shoes.append(cls(shoe))

                return shoes
        
        @classmethod
        def get_nike(cls):

                query = "SELECT * FROM shoes where shoes.brand = 'Nike' order by rand() limit 18;"



                shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

                shoes = []

                for shoe in shoes_from_db:
                        shoes.append(cls(shoe))

                return shoes
        
        @classmethod
        def get_adidas(cls):

                query = "SELECT * FROM shoes where shoes.brand = 'Adidas' order by rand() limit 18;"



                shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

                shoes = []

                for shoe in shoes_from_db:
                        shoes.append(cls(shoe))

                return shoes
        
        @classmethod
        def get_jordan(cls):

                query = "SELECT * FROM shoes where shoes.brand = 'Jordan' order by rand() limit 18;"



                shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

                shoes = []

                for shoe in shoes_from_db:
                        shoes.append(cls(shoe))

                return shoes

        @classmethod
        def get_puma(cls):

                query = "SELECT * FROM shoes where shoes.brand = 'Puma' order by rand() limit 18;"



                shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

                shoes = []

                for shoe in shoes_from_db:
                        shoes.append(cls(shoe))

                return shoes
        
        # gets 3 random shoes to display in view shoe
        @classmethod
        def get_3_shoes(cls):

                query = 'SELECT * FROM shoes order by rand() limit 3;'



                shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

                shoes = []

                for shoe in shoes_from_db:
                        shoes.append(cls(shoe))

                return shoes
        
        @classmethod
        def get_one(cls, data):
                query = 'SELECT * FROM shoes WHERE id = %(id)s;'

                results = connectToMySQL('kicks_kartel').query_db(query, data)

                return cls(results[0])
        
        @classmethod
        def get_deals(cls):

                query = 'select * from shoes where market_value < retailPrice;'



                shoes_from_db = connectToMySQL('kicks_kartel').query_db(query)

                shoes = []

                for shoe in shoes_from_db:
                        shoes.append(cls(shoe))

                return shoes
