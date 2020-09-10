from flask import Blueprint
from flask_login import login_required, current_user, login_manager
from . import db

# Main blueprint, contains all 'generals' routes
main = Blueprint('main', __name__)


#
# Routes
#


@main.route('/')
def index():
    return "<h1>EDT API 2020 Xtreme edition Plus Premium</h1>You need to login to access the API"


@main.route('/profile')
@login_required
def profile():
    return "BSAHTEK !!"


@main.route('/error')
def error():
    return "You shouldn't be there... You may try logging in !"
