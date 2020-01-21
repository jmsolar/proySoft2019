from flask import redirect, render_template, request, url_for, session, abort
from flaskps.models.configuracion import Configuracion
from flaskps.models.entities.mappers.config_mapper import to_config
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.helpers.config import sitio_habilitado

@sitio_habilitado()
@requiere_permiso("configuracion_index")
def index():
    configuracion = Configuracion.get_config()
    return render_template('configuracion/index.html', configuracion=configuracion)

@sitio_habilitado()
@requiere_permiso("configuracion_edit")
def edit():
    configuracion = Configuracion.get_config()
    return render_template('configuracion/edit.html', configuracion=configuracion)

@sitio_habilitado()
@requiere_permiso("configuracion_save")
def save():
    config = to_config(request.form)
    Configuracion.update_config(config)
    return redirect(url_for('configuration_index'))