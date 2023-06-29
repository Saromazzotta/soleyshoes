from flask_app import app
from flask_app.controllers import main
from flask_app.controllers import user_home

if __name__ == '__main__':
    app.run(debug = True)