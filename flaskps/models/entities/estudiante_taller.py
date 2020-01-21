from flaskps.db import db
from flaskps.models.entities.estudiante import Estudiante
from flaskps.models.entities.horario_taller import HorarioTaller


class EstudianteTaller(db.Model):
    __tablename__= "estudiante_taller"

    id = db.Column(db.Integer, primary_key=True)

    estudiante_id = db.Column(db.Integer, db.ForeignKey("estudiante.id"))
    estudiante = db.relationship("Estudiante")

    # ciclo_lectivo_id = db.Column(db.Integer, db.ForeignKey("ciclo_lectivo.id"), primary_key=True)
    # ciclo_lectivo = db.relationship("CicloLectivo")
    #
    # taller_id = db.Column(db.Integer, db.ForeignKey("taller.id"), primary_key=True)
    # taller = db.relationship("Taller")

    horario_id = db.Column(db.Integer, db.ForeignKey("horario_taller.id"))
    horario = db.relationship("HorarioTaller")

    def __init__(self, estudiante_id, horario_id):
        self.estudiante_id = estudiante_id
        self.horario_id = horario_id
