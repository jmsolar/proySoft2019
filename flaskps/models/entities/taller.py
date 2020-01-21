import datetime

from flaskps.db import db
from flaskps.models.entities.helper_tables import ciclo_lectivo_taller
# from flaskps.models.entities.ciclo_lectivo import CicloLectivo
# import flaskps.models.entities.ciclo_lectivo
# import flaskps.models.entities.asistencia_estudiante_taller
# from flaskps.models.entities.helper_tables import asistencia_estudiante_taller

class Taller(db.Model):
    __tablename__ = "taller"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)
    nombre_corto = db.Column(db.String(255), nullable=False)
    ciclos_lectivos = db.relationship("CicloLectivo", secondary=ciclo_lectivo_taller, lazy='subquery')

    def __init__(self, nombre, nombre_corto):
        self.nombre = nombre
        self.nombre_corto = nombre_corto