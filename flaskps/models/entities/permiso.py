from flaskps.db import db

class Permiso(db.Model):
    __tablename__= "permiso"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)