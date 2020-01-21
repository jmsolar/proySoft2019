import datetime
from flaskps.db import db

class Genero(db.Model):
    __tablename__ = "genero"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre