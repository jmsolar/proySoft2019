from flaskps.models.generic import Generic
from flaskps.models.entities.escuela import Escuela
from flaskps.db import db, Session
from datetime import datetime

class School(Generic):

    def get_entity():
        return Escuela

    def all(page=1):
        result = Escuela.query
        return result

    def find_by_name(name):
        result = Escuela.query.filter_by(nombre=name).first()
        return result