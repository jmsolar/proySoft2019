import datetime

from flaskps.db import db
from flaskps.models.entities.genero import Genero
from flaskps.models.entities.estudiante import Estudiante
from flaskps.models.entities.helper_tables import responsable_estudiante

class Docente(db.Model):
    __tablename__ = "docente"

    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    fecha_nac = db.Column(db.DateTime, nullable=False)
    localidad_id = db.Column(db.Integer, nullable=False)
    domicilio = db.Column(db.String(255), nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey('genero.id'))
    #genero = db.relationship(Genero, backref = backref('docente_genero', uselist = False, cascade = 'delete,all'))
    #genero = db.Column(db.Integer,nullable=False)
    #genero_id = db.Column(db.Integer, db.ForeignKey('genero.id'))
    #genero = db.relationship(Genero, backref = backref('docente_genero', uselist = True, cascade = 'delete,all'))
    #genero = db.relationship("Genero", uselist=True, back_populates="genero")
    tipo_doc_id = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False, unique=True)
    tel = db.Column(db.Integer, nullable=False, unique=True)
    #estudiantes = db.relationship("Estudiante", secondary=responsable_estudiante, lazy='subquery')

    def __init__(self, apellido, nombre, fecha_nac, localidad, domicilio, genero, tipo_documento, numero, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.localidad_id = localidad
        self.domicilio = domicilio
        self.genero_id = genero
        self.tipo_doc_id = tipo_documento
        self.numero = numero
        self.tel = telefono