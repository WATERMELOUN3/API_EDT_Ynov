from flask_login import UserMixin
from . import db

# Classe d'équivalence assiste

# assiste_table = db.Table("assiste", db.Model.metadata,
#                          db.Column("id", db.Integer, primary_key=True),
#                          db.Column("idCour", db.Integer,
#                                    db.ForeignKey("cour.id")),
#                          db.Column("idStudent", db.Integer, db.ForeignKey("user.id")))


class Assiste(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    idCour = db.Column("idCour", db.Integer, db.ForeignKey("cour.id"))
    idStudent = db.Column("idStudent", db.Integer, db.ForeignKey("user.id"))

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
    cours = db.relationship(
        "Cour", secondary=Assiste.__table__, backref=db.backref("eleves"))

# Classe matiere


class Matiere(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,
                   autoincrement=True, nullable=False)
    nom = db.Column(db.String(30), nullable=False)
    ects = db.Column(db.Integer, nullable=False)
    idProf = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# Classe cour


class Cour(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,
                   autoincrement=True, nullable=False)
    heureDebut = db.Column(db.DateTime, nullable=False)
    heureFin = db.Column(db.DateTime, nullable=False)
    idMatiere = db.Column(db.Integer, db.ForeignKey(
        "matiere.id"), nullable=False)
    idProf = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# class Assiste(db.Model):
#     id = db.Column(db.Integer, primary_key=True, unique=True,
#                    autoincrement=True, nullable=False)
#     idCour = db.Column(db.Integer, db.ForeignKey("cour.id"), nullable=False)
#     idStudent = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
