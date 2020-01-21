import datetime
from flaskps.db import db

class TipoInstrumento(db.Model):
    __tablename__ = "tipo_instrumento"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre