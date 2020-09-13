from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user, login_manager
from .models import User, Cour, Matiere, Assiste
from . import db
import datetime

# Main blueprint, contains all 'generals' routes
main = Blueprint('main', __name__)

#
#
# Routes
#
#


@main.route('/')
def index():
    return "<h1>EDT API 2020 Xtreme edition Plus Premium</h1>You need to login to access the API"

#
# Cours routes
#


@main.route('/cours', methods=['GET'])
@login_required
def cours_get():
    userId = current_user.id
    cours = User.query.filter_by(id=userId).first().cours

    return jsonify_list(cours)


@main.route('/cours', methods=['PUT'])
@login_required
def cours_put():
    idCour = request.form.get("idCour")
    userId = current_user.id

    if idCour is None:
        return "Incorrect form body"

    if Cour.query.filter_by(id=idCour).count() > 0:
        newAssiste = Assiste(idCour=idCour, idStudent=userId)
        db.session.add(newAssiste)
        db.session.commit()
        return "Success"
    else:
        return "Incorrect form body"


@main.route('/cours', methods=['POST'])
@login_required
def cours_post():
    if not current_user.prof:
        return "Unauthorized"

    idMatiere = request.form.get("idMatiere")
    idProf = request.form.get("idProf")
    heureDebut = strtodatetime(request.form.get("heureDebut"))
    heureFin = strtodatetime(request.form.get("heureFin"))

    if idMatiere is None or heureDebut is None or heureFin is None:
        return "Incorrect form body"

    if Matiere.query.filter_by(id=idMatiere).count() > 0:
        newCour = Cour(idMatiere=idMatiere,
                       heureDebut=heureDebut, heureFin=heureFin, idProf=idProf)
        db.session.add(newCour)
        db.session.commit()
        return "Success"
    else:
        return "Incorrect form body"


@main.route('/cours', methods=['DELETE'])
@login_required
def cours_delete():
    idUser = current_user.id
    idCour = request.form.get("idCour")
    idStudent = request.form.get("idStudent")

    if idStudent is None:
        db.session.delete(Assiste.query.filter_by(
            idCour=idCour, idStudent=idUser).first())
    elif current_user.prof:
        db.session.delete(Assiste.query.filter_by(
            idCour=idCour, idStudent=idStudent))
    db.session.commit()

    return "Success"


#
# Matiere routes
#


@main.route('/matiere', methods=['GET'])
@login_required
def matiere_get():
    idProf = request.form.get("idProf")

    matieres = None
    if idProf is None:
        matieres = Matiere.query.all()
    else:
        matieres = Matiere.query.filter_by(idProf=idProf)

    return jsonify_list(matieres)


@main.route('/matiere', methods=['POST'])
@login_required
def matiere_post():
    if not current_user.prof:
        return "Unauthorized"

    nom = request.form.get("nom")
    idProf = request.form.get("idProf")
    ects = request.form.get("ects")

    newMatiere = Matiere(nom=nom, idProf=idProf, ects=ects)

    db.session.add(newMatiere)
    db.session.commit()

    return "Success"


@main.route('/matiere', methods=['PATCH'])
@login_required
def matiere_patch():
    if not current_user.prof:
        return "Unauthorized"

    id = request.form.get("id")
    nom = request.form.get("nom")
    idProf = request.form.get("idProf")
    ects = request.form.get("ects")

    matiere = Matiere.query.filter_by(id=id).first()
    if nom is not None:
        matiere.nom = nom
    if idProf is not None:
        matiere.idProf = idProf
    if ects is not None:
        matiere.ects = ects

    db.session.update(matiere)
    db.session.commit()

    return "Success"


@main.route('/matiere', methods=['DELETE'])
@login_required
def matiere_delete():
    if not current_user.prof:
        return "Unauthorized"

    id = request.form.get("id")
    db.session.delete(Matiere.query.filter_by(id=id).first())
    db.session.commit()

    return "Success"


#
# Prof/User routes
#


@main.route('/prof/user', methods=['GET'])
@login_required
def prof_user_get():
    if not current_user.prof:
        return "Unauthorized"

    id = request.form.get("id")
    if id is None:
        return jsonify_list(User.query.all())
    else:
        return jsonify_list([User.query.filter_by(id=id).first()])


@main.route('/prof/user', methods=['POST'])
@login_required
def prof_user_post():
    if not current_user.prof:
        return "Unauthorized"

    username = request.form.get("username")
    password = request.form.get("password")
    prenom = request.form.get("prenom")
    nom = request.form.get("nom")
    prof = request.form.get("username")

    if username is None or password is None:
        return "Bad arguments"

    newUser = User(username=username, password=password, prof=False)
    if prenom is not None:
        newUser.prenom = prenom
    if nom is not None:
        newUser.nom = nom
    if prof is not None:
        newUser.prof = prof

    db.session.add(newUser)
    db.session.commit()

    return "Success"


@main.route('/prof/user', methods=['DELETE'])
@login_required
def prof_user_delete():
    if not current_user.prof:
        return "Unauthorized"

    id = request.form.get("id")

    db.session.delete(User.query.filter_by(id=id).first())
    db.session.commit()

    return "Success"


@main.route('/prof/user', methods=['PUT'])
@login_required
def prof_user_put():
    if not current_user.prof:
        return "Unauthorized"

    id = request.form.get("id")
    username = request.form.get("username")
    password = request.form.get("password")
    prenom = request.form.get("prenom")
    nom = request.form.get("nom")
    prof = request.form.get("username")

    user = User.query.filter_by(id=id).first()
    if username is not None:
        user.username = username
    if password is not None:
        user.password = password
    if prenom is not None:
        user.prenom = prenom
    if nom is not None:
        user.nom = nom
    if prof is not None:
        user.prof = prof

    db.session.update(user)
    db.session.commit()

    return "Success"


#
# Other routes
#


@main.route('/error')
def error():
    return "You shouldn't be there... You may try logging in !"


def jsonify_list(l):
    tmp = []
    for e in l:
        tmp.append(e.__dict__)
        del tmp[-1]["_sa_instance_state"]

    return jsonify(tmp)


def strtodatetime(text):
    texts = text.split(' ')
    date = datetime.date.fromisoformat(texts[0])
    time = datetime.time.fromisoformat(texts[1])

    return datetime.datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)
