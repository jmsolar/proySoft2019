from flaskps.models.entities.tipo_instrumento import TipoInstrumento
from flaskps.models.generic import Generic
from flaskps.db import db, Session
from datetime import datetime

class InstrumentType(Generic):

    def get_entity():
        return TipoInstrumento
    
    def get_by_id(id):
        return TipoInstrumento.query.filter_by(id=id).first()

    def get_by_name(nombre):
        return TipoInstrumento.query.filter_by(nombre=nombre).first()