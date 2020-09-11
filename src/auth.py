from flask import Blueprint, redirect, url_for, flash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user
from flask_sqlalchemy import request

# auth blueprint, contains all the authentications routes
auth = Blueprint('auth', __name__)


#
# Routes
#


@auth.route('/login', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def login():
    return 'Use POST request to login...'


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = request.form.get('remember')
    if remember == None:
        remember = False

    user = User.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not user.password == password:
        print("Incorrect credentials", username, password)
        # if the user doesn't exist or password is wrong, reload the page
        return "Incorrect credentials"  # redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    
    login_user(user, remember=remember)
    print("User", username, "logged in !")
    return "Successfully logged in !"  # redirect(url_for('main.profile'))


@auth.route('/signup', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def signup():
    return 'Use POST request to signup...'


@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(username=username).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash("Le nom d'utilisateur est déjà utilisé")
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(username=username, password=password,
                    prenom=prenom, nom=nom, prof=0)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    # redirect(url_for('auth.login'))
    return "Signed up ! Please login to gain access."


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return "Logged out !"  # redirect(url_for('main.index'))
