from functools import wraps
from flask import url_for, session, redirect, abort
from flaskps.models.user import User

def authenticated(sesion):
    return sesion.get('user')

def has_permission(permiso):
    return User.tiene_permiso(authenticated(session), permiso)

def has_role(rol):
    return User.tiene_rol(authenticated(session), rol)

def requiere_permiso(permiso):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not authenticated(session):
                return redirect(url_for('auth_login'))

            elif not User.tiene_permiso(authenticated(session), permiso):
                abort(401)
            return f(*args, **kwargs)

        return decorated_function
    return decorator