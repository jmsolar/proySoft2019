from flaskps.db import db

class Barrio(db.Model):
    __tablename__ = "barrio"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=False)

    def __init__(self, nombre):
        self.nombre = nombre