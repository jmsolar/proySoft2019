from flaskps.db import db
from flaskps.models.entities.docente import Docente

class DocenteResponsableTaller(db.Model):
    __tablename__= "docente_responsable_taller"

    docente_id = db.Column(db.Integer, db.ForeignKey("docente.id"), primary_key=True)
    docente = db.relationship("Docente")

    ciclo_lectivo_id = db.Column(db.Integer, db.ForeignKey("ciclo_lectivo.id"), primary_key=True)
    ciclo_lectivo = db.relationship("CicloLectivo")

    taller_id = db.Column(db.Integer, db.ForeignKey("taller.id"), primary_key=True)
    taller = db.relationship("Taller")

    def __init__(self, docente_id, ciclo_lectivo_id, taller_id):
        self.docente_id = docente_id
        self.ciclo_lectivo_id = ciclo_lectivo_id
        self.taller_id = taller_id