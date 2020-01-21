from flaskps.models.entities.configuracion import Config


def to_config(form):
    habilitado = form.get("habilitado") == "on"
    return Config(form.get("titulo"),
                  form.get("email"),
                  form.get("registros_por_pagina"),
                  form.get("descripcion"),
                  habilitado)
