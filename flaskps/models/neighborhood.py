from flaskps.models.generic import Generic
from flaskps.models.entities.barrio import Barrio
from flaskps.db import db, Session
from datetime import datetime

class Neighborhood(Generic):

    def get_entity():
        return Barrio

    def all(page=1):
        result = Barrio.query
        return result

    def find_by_name(name):
        result = Barrio.query.filter_by(nombre=name).first()
        return result