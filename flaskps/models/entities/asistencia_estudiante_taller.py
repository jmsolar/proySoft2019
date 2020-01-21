import datetime
from flaskps.db import db
from sqlalchemy.orm import backref
from flaskps.models.entities.estudiante import Estudiante
from flaskps.models.entities.ciclo_lectivo import CicloLectivo
from flaskps.models.entities.taller import Taller

class AsistenciaEstudianteTaller(db.Model):
    __tablename__ = "asistencia_estudiante_taller"

    id = db.Column(db.Integer, primary_key=True)
    
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'))
    estudiante = db.relationship(Estudiante, backref = backref('asistencia_estudiante_taller_estudiante', uselist = True, cascade = 'delete,all'))

    ciclo_lectivo_id = db.Column(db.Integer, db.ForeignKey('ciclo_lectivo.id'))
    ciclo_lectivo = db.relationship(CicloLectivo, backref = backref('asistencia_estudiante_taller_ciclo_lectivo', uselist = True, cascade = 'delete,all'))

    taller_id = db.Column(db.Integer, db.ForeignKey('taller.id'))
    taller = db.relationship(Taller, backref = backref("asistencia_estudiante_taller_taller", uselist = True, cascade = 'delete,all'))

    fecha = db.Column(db.DateTime, nullable=False)

    def __init__(self, estudiante_id, ciclo_lectivo_id, taller_id, fecha):
        self.estudiante_id = estudiante_id
        self.ciclo_lectivo_id = ciclo_lectivo_id
        self.taller_id = taller_id
        self.fecha = fecha