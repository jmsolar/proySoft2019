from functools import wraps
from flask import url_for, redirect
from flaskps.models.configuracion import Configuracion

def sitio_habilitado():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            conf = Configuracion.get_config()
            if conf.habilitado == 0:
                return redirect(url_for('mantenimiento'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator