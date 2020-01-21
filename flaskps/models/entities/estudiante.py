import datetime
from sqlalchemy.orm import backref
from flaskps.db import db
from flaskps.models.entities.helper_tables import asis_est_taller, responsable_estudiante
from flaskps.models.entities.rol import Rol
from flaskps.models.entities.barrio import Barrio
from flaskps.models.entities.genero import Genero
from flaskps.models.entities.escuela import Escuela
from flaskps.models.entities.nivel import Nivel
from flaskps.models.entities.responsable import Responsable

class Estudiante(db.Model):
    __tablename__ = "estudiante"

    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String(255), nullable=False, unique=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)
    fecha_nac = db.Column(db.DateTime, nullable=False)

    localidad_id = db.Column(db.Integer, primary_key=False)
    domicilio = db.Column(db.String(255), nullable=False, unique=True)

    barrio_id = db.Column(db.Integer, db.ForeignKey('barrio.id'))
    barrio = db.relationship(Barrio, backref = backref('estudiantes_barrio', uselist = True, cascade = 'delete,all'))

    genero_id = db.Column(db.Integer, db.ForeignKey('genero.id'))
    genero = db.relationship(Genero, backref = backref('estudiantes_genero', uselist = True, cascade = 'delete,all'))

    tipo_doc_id = db.Column(db.Integer,nullable=False,unique=True)
    numero = db.Column(db.Integer,nullable=False,unique=True)
    tel = db.Column(db.String(255), nullable=False, unique=True)
    
    escuela_id = db.Column(db.Integer, db.ForeignKey('escuela.id'))
    escuela = db.relationship(Escuela, backref = backref('estudiantes_escuela', uselist = True, cascade = 'delete,all'))
    
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.id'))
    nivel = db.relationship(Nivel, backref = backref('estudiantes_nivel', uselist = True, cascade = 'delete,all'))

    def __init__(self, apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id):
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.localidad_id = localidad_id
        self.nivel_id = nivel_id
        self.domicilio = domicilio
        self.genero_id = genero_id
        self.escuela_id = escuela_id
        self.tipo_doc_id = tipo_doc_id
        self.numero = numero
        self.tel = tel
        self.barrio_id = barrio_id