from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.models.user import User
from flaskps.helpers.config import sitio_habilitado

@sitio_habilitado()
def login():
    return render_template('auth/login.html')

@sitio_habilitado()
def authenticate():
    params = request.form
    user = User.find_by_username_and_pass(params['username'], params['password'])

    if not user:
        mensaje = "Verifique los datos ingresados, el usuario o clave son incorrectos"
        return render_template('auth/login.html', mensaje = mensaje)

    session['user'] = user.username
    return redirect(url_for('home'))

@sitio_habilitado()
def logout():
    del session['user']
    session.clear()
    return redirect(url_for('auth_login'))