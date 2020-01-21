import datetime

from flaskps.db import db
from flaskps.models.entities.helper_tables import preceptor_nucleo
from flaskps.models.entities.preceptor import Preceptor


class Nucleo(db.Model):
    __tablename__ = "nucleo"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    preceptores = db.relationship(Preceptor, secondary=preceptor_nucleo, lazy='subquery')

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono