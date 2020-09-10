"""
Projet API REST
Alexis GELIN--ANDRIEU
"""

#
# IMPORTS
#


import flask
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import flask_login
from flask_login import LoginManager

from models import User
import os.path
import hashlib


#
# INITIALIZATION
#


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy()
db.init_app(app)
dbFile = "db.sqlite"
print("Initialized !")

#
# MAIN ROUTES
#


@app.route('/', methods=['GET'])
def home():
    return "<h1>Projet API REST</h1><p>Je suis une API conçu en Python avec Flask pour gérer un emploi du temps</p>"


#
# AUTH ROUTES
#


@app.route('/login')
def login():
    return 'Login'


@app.route('/signup')
def signup():
    return 'Signup'


@app.route('/logout')
def logout():
    return 'Logout'


#
# FUNCTIONS
#


def check():
    if not os.path.exists(dbFile):
        print("Database file not found (", dbFile, ")", sep='')
        exit(1)


def hash_password(pwd):
    m = hashlib.sha256()
    m.update(pwd)
    return m.digest()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


#
# MAIN
#


check()
app.run()
