import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# TODO: bcrypt : for password hashing.. do we need? since our password already hashed.

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myapp_obj)
login = LoginManager(myapp_obj)


login.login_view = 'login'

from app import routes
