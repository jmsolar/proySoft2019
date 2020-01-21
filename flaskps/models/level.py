from flaskps.models.generic import Generic
from flaskps.models.entities.nivel import Nivel
from flaskps.db import db, Session
from datetime import datetime

class Level(Generic):

    def get_entity():
        return Nivel

    def all(page=1):
        result = Nivel.query
        return result

    def find_by_name(name):
        result = Nivel.query.filter_by(nombre=name).first()
        return result