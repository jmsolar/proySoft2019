from flaskps.models.generic import Generic
from flaskps.models.entities.genero import Genero
from flaskps.db import db, Session
from datetime import datetime

class Gender(Generic):

    def get_entity():
        return Genero

    def all(page=1):
        result = Genero.query
        return result

    def find_by_name(name):
        result = Genero.query.filter_by(nombre=name).first()
        return result