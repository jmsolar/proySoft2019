from flask import redirect, render_template, request, url_for, session, abort
from flaskps.models.user import User
from flaskps.models.rol import RolModel
from flaskps.models.entities.mappers.user_mapper import to_usuario
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.helpers.config import sitio_habilitado

@sitio_habilitado()
@requiere_permiso("usuario_index")
def index():
    users = User.all()
    return render_template('user/index.html', users=users.items)

@sitio_habilitado()
@requiere_permiso("usuario_new")
def new():
    roles = RolModel.all()
    return render_template('user/new.html', roles=roles)

@sitio_habilitado()
@requiere_permiso("usuario_new")
def create():
    if not authenticated(session):
        abort(401)

    new_user = to_usuario(request.form)
    user = User.find_by_username(new_user.username)
    if user is None:
        User.save(new_user, request.form.getlist("rol"))
        return redirect(url_for('user_index'))
    else:
        mensaje = "El usuario ya existe"
        return render_template('user/new.html', mensaje = mensaje, roles = RolModel.all(), nombre = new_user.first_name, apellido = new_user.last_name, usuario = new_user.username, correo = new_user.email)

@sitio_habilitado()
@requiere_permiso("usuario_update")
def edit(id):
    aUser = User.find_by_id(id)
    roles = RolModel.all()
    return render_template('user/edit.html',aUser=aUser,roles=roles)

@sitio_habilitado()
@requiere_permiso("usuario_update")
def save():
    id = request.form["id"]
    edit_user = to_usuario(request.form)
    user = User.find_by_username(edit_user.username)
    user_same = User.find_by_id(id)
    if user is None:
        User.update(edit_user, request.form.getlist("rol"), id)
        return redirect(url_for('user_index'))
    elif (user_same.username == edit_user.username or user_same.email == edit_user.email) and user is None:
        User.update(edit_user, request.form.getlist("rol"), edit_user.id)
        return redirect(url_for('user_index'))
    else:
        mensaje = "El usuario ya existe"
        return render_template('user/index.html', mensaje = mensaje)

@sitio_habilitado()
@requiere_permiso("usuario_destroy")
def delete(id):
    User.delete_by_id(id) 
    return redirect(url_for('user_index'))

@sitio_habilitado()
def inactivos():
    users = User.find_blocked()
    return render_template('user/inactivos.html', users=users.items)

@sitio_habilitado()
def activar(id):
    User.activate_by_id(id)
    return redirect(url_for('user_index'))

@sitio_habilitado()
def activar_todos():
    User.activate_all()
    return redirect(url_for('user_index'))