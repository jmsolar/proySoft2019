import datetime

from flaskps.db import db
from flaskps.models.entities.helper_tables import usuario_tiene_rol
from flaskps.models.entities.rol import Rol

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, nullable=False)
    updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    roles = db.relationship("Rol", secondary=usuario_tiene_rol, lazy="subquery")

    def __init__(self, email, username, password, first_name, last_name):
        self.email = email
        self.username = username
        self.password = password
        self.activo = True
        self.created_at = datetime.datetime.now()
        self.first_name = first_name
        self.last_name = last_name