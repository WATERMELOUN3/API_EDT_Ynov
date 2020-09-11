from flask import Blueprint, jsonify
from flask_login import login_required, current_user, login_manager
from .models import User, Cour, Matiere
from . import db

# Main blueprint, contains all 'generals' routes
main = Blueprint('main', __name__)


#
# Routes
#


@main.route('/')
def index():
    return "<h1>EDT API 2020 Xtreme edition Plus Premium</h1>You need to login to access the API"


@main.route('/cours', methods=['GET'])
@login_required
def eleve_cours():
    cours = User.query.filter_by(id=2).first().cours

    return jsonify_list(cours)


@main.route('/error')
def error():
    return "You shouldn't be there... You may try logging in !"


def jsonify_list(l):
    tmp = []
    for e in l:
        tmp.append(e.__dict__)
        del tmp[-1]["_sa_instance_state"]

    return jsonify(tmp)
