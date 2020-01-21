from flaskps.db import db
from flaskps.models.entities.helper_tables import rol_tiene_permiso
from flaskps.models.entities.permiso import Permiso

class Rol(db.Model):
    __tablename__ = "rol"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    permisos = db.relationship("Permiso", secondary=rol_tiene_permiso, lazy='subquery')