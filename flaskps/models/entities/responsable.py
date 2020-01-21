import datetime
from sqlalchemy.orm import backref
from flaskps.db import db
from flaskps.models.entities.genero import Genero

class Responsable(db.Model):
    __tablename__ = "responsable"

    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    fecha_nac = db.Column(db.DateTime, nullable=False)
    localidad = db.Column(db.String(255), nullable=False)
    domicilio = db.Column(db.String(255), nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey('genero.id'))
    genero = db.relationship(Genero, backref = backref('estudiantes', uselist = True, cascade = 'delete,all'))
    tipo_documento = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.Integer, nullable=False, unique=True)
    telefono = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, apellido, nombre, fecha_nac, localidad, domicilio, genero, tipo_documento, numero, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.localidad = localidad
        self.domicilio = domicilio
        self.genero = genero
        self.tipo_documento = tipo_documento
        self.numero = numero
        self.telefono = telefono