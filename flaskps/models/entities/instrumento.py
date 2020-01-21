import datetime
from sqlalchemy.orm import backref
from flaskps.db import db
from flaskps.models.entities.tipo_instrumento import TipoInstrumento

class Instrumento(db.Model):
    __tablename__ = "instrumento"

    numero_inventario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)

    tipo_instrumento_id = db.Column(db.Integer, db.ForeignKey('tipo_instrumento.id'))
    tipo_instrumento = db.relationship(TipoInstrumento, backref = backref('instrumento_tipo_instrumento', uselist = True, cascade = 'delete,all'))

    ruta_imagen = db.Column(db.String(255))

    def __init__(self, nombre, tipo_instrumento_id, ruta_imagen):
        self.nombre = nombre
        self.tipo_instrumento_id = tipo_instrumento_id
        self.ruta_imagen = ruta_imagen