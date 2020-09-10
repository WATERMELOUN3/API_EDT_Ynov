from flask_login import UserMixin
from . import db

# Classe utilisateur


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,
                   autoincrement=True, nullable=False)
    # primary keys are required by SQLAlchemy
    username = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    prof = db.Column(db.Boolean, nullable=False)

# Classe matiere


class Matiere(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,
                   autoincrement=True, nullable=False)
    nom = db.Column(db.String(30), nullable=False)
    ects = db.Column(db.Integer, nullable=False)
    prof = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# Classe cour


class Cour(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,
                   autoincrement=True, nullable=False)
    heure_debut = db.Column(db.String, nullable=False)
    heure_fin = db.Column(db.String, nullable=False)
    matiere = db.Column(db.Integer, db.ForeignKey(
        "matiere.id"), nullable=False)
    prof = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# Classe d'équivalence assiste


class Assiste(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,
                   autoincrement=True, nullable=False)
    idCour = db.Column(db.Integer, db.ForeignKey("cour.id"), nullable=False)
    idStudent = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
