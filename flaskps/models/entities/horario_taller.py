from flaskps.db import db
from flaskps.models.entities.nucleo import Nucleo
from flaskps.models.entities.ciclo_lectivo import CicloLectivo
from flaskps.models.entities.taller import Taller


class HorarioTaller(db.Model):
    __tablename__ = "horario_taller"

    id = db.Column(db.Integer, primary_key=True)

    ciclo_lectivo_id = db.Column(db.Integer, db.ForeignKey('ciclo_lectivo.id'))
    ciclo_lectivo = db.relationship(CicloLectivo, uselist=False)

    taller_id = db.Column(db.Integer, db.ForeignKey('taller.id'))
    taller = db.relationship(Taller, uselist=False)

    nucleo_id = db.Column(db.Integer, db.ForeignKey('nucleo.id'))
    nucleo = db.relationship("Nucleo", uselist=False)

    dia_semana = db.Column(db.String, nullable=False)

    hora_inicio = db.Column(db.String, nullable=False)
    hora_fin = db.Column(db.String, nullable=False)

    def __init__(self, nucleo_id, ciclo_lectivo_id, taller_id, dia_semana, hora_inicio, hora_fin):
        self.nucleo_id = nucleo_id
        self.ciclo_lectivo_id = ciclo_lectivo_id
        self.taller_id = taller_id
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
