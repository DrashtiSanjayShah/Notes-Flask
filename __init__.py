from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy() #initialize the database
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__) #initialize the app. __name__ is the name of the current Python module.
    app.config['SECRET_KEY'] = 'bjhfafkufiqloqbhavc' #secret key for the app.not really used for the production of a real app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #database uri
    db.init_app(app) #initialize the database

    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #register the blueprint from views.py
    app.register_blueprint(auth, url_prefix='/') #register the blueprint from auth.py
    

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #login view
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #get the user by id
 
    return app
def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database!")