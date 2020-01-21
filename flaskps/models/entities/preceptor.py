from flaskps.db import db
from flaskps.models.entities.helper_tables import preceptor_nucleo


class Preceptor(db.Model):
    __tablename__ = "preceptor"

    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    tel = db.Column(db.String(255), nullable=False, unique=True)
    nucleos = db.relationship("Nucleo", secondary=preceptor_nucleo, lazy='subquery')

    def __init__(self, apellido, nombre, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono