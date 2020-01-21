from flaskps.models.entities.instrumento import Instrumento
from flaskps.models.entities.tipo_instrumento import TipoInstrumento
from flaskps.models.generic import Generic
from flaskps.db import db, Session
from datetime import datetime

class Instrument(Generic):

    def get_entity():
        return Instrumento

    def get_by_id(id):
        return Instrumento.query.filter_by(numero_inventario=id).first()
    
    def delete_by_numero_inventario(id):
        instrument = Instrumento.query.filter_by(numero_inventario=id).first()
        db.session.delete(instrument)
        db.session.commit()
        return True
    
    def update(entity, id):
        instrument = Instrumento.query.filter_by(numero_inventario=id).first()
        instrument.nombre = entity.nombre
        instrument.tipo_instrumento_id = entity.tipo_instrumento_id
        instrument.ruta_imagen = entity.ruta_imagen
        db.session.commit()
        return True