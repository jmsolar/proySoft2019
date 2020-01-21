from flaskps.models.generic import Generic
from flaskps.models.entities.configuracion import Config
from flaskps.db import db


class Configuracion(Generic):

    def get_entity():
        return Config

    def get_config():
        return Config.query.first()

    def update_config(config):
        configuracion = Config.query.first()
        configuracion.titulo = config.titulo
        configuracion.descripcion = config.descripcion
        configuracion.habilitado = config.habilitado
        configuracion.email = config.email
        configuracion.registros_por_pagina = config.registros_por_pagina
        db.session.commit()
