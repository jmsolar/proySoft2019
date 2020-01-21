from flaskps.db import db


class Config(db.Model):
    __tablename__= "configuracion"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    registros_por_pagina = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)

    def __init__(self, titulo, email, registros_por_pagina, descripcion, habilitado=True):
        self.titulo = titulo
        self.email = email
        self.habilitado = habilitado
        self.registros_por_pagina = registros_por_pagina
        self.descripcion = descripcion