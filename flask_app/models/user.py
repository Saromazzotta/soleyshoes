from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.Shoe import Shoe
from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cart = None

# Validates all user info inputed to the form
    @staticmethod
    def validate_user(user):
        is_valid = True
        query_email = 'SELECT * FROM users WHERE email = %(email)s;'
        results_email = connectToMySQL('kicks_kartel').query_db(query_email, user)


        if len(results_email) >= 1:
            flash("email is already in use.", "register")
            is_valid = False
        if len(user['first_name']) <= 2:
            flash("First Name must be 3 characters or more.", "register")
            is_valid = False
        if len(user['last_name']) <= 2:
            flash("Last Name must be 3 characters or more", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("invalid email", "register")
            is_valid = False
        if len(user['password']) <= 7:
            flash("Invalid password", "register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash('passwords do not match', "register")
            is_valid = False
        return is_valid

# gets a user based on the email used to register
    @classmethod
    def get_by_email(cls, data):
            query = 'SELECT * FROM users WHERE email = %(email)s;'

            results = connectToMySQL('kicks_kartel').query_db(query, data)

            if len(results) < 1:
                return False

            return cls(results[0])

# gets a user by id and main method to get a singular user
    @classmethod
    def get_by_id(cls, data):
            query = 'SELECT * FROM users WHERE id = %(id)s;'

            results = connectToMySQL('kicks_kartel').query_db(query, data)

            return cls(results[0])

# gets all users in the associated database
    @classmethod
    def get_all(cls):
            query = 'SELECT * FROM users;'

            users_from_db = connectToMySQL('kicks_kartel').query_db(query)

            users = []

            for user in users_from_db:
                users.append( cls(user))

                return users
            
# used to create an instance of a user in the register
    @classmethod
    def save(cls, data):
            query = 'INSERT INTO users (first_name, last_name, email,password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'

            return connectToMySQL('kicks_kartel').query_db(query, data)

# updates current user info, more can be added
    @classmethod
    def update_user_info(cls, data):
        if not cls.validate_user_info(data):
            return False
        
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id = %(id)s;'

        return connectToMySQL('kicks_kartel').query_db(query, data)
    
    @classmethod
    def add_to_cart(cls, data):
                query = 'SELECT * FROM users LEFT JOIN shoes On users.id WHERE shoes.id = %(id)s and users.id = %(user_id)s;'

                results = connectToMySQL('kicks_kartel').query_db(query, data)

                result = results[0]
                this_user = cls(result)

                shoe_data = {
                    'id': result['shoes.id'],
                    'brand': result['brand'],
                    'silhoutte': result['silhoutte'],
                    'colorway': result['colorway'],
                    'market_value': result['market_value'],
                    'gender': result['gender'],
                    'name': result['name'],
                    'retailPrice': result['retailPrice'],
                    'story': result['story'],
                    'image': result['image']

                }
                this_user.cart = Shoe(shoe_data)

                return this_user