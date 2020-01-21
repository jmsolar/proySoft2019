import datetime

from flaskps.db import db
from flaskps.models.entities.helper_tables import ciclo_lectivo_taller
from flaskps.models.entities.taller import Taller
# from flaskps.models.entities.asistencia_estudiante_taller import AsistenciaEstudianteTaller

class CicloLectivo(db.Model):
    __tablename__ = "ciclo_lectivo"

    id = db.Column(db.Integer, primary_key=True)
    fecha_ini = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    talleres = db.relationship("Taller", secondary=ciclo_lectivo_taller, lazy='subquery')
    # asistencia_estudiante_taller = db.relationship("AsistenciaEstudianteTaller", secondary=asistencia_estudiante_taller, lazy='subquery')
    # asistencia_estudiante_taller = db.relationship("AsistenciaEstudianteTaller", back_populates="ciclo_lectivo")

    def __init__(self, fecha_ini, fecha_fin, semestre):
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        self.semestre = semestre