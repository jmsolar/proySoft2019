from os.path import dirname, realpath
from flask import redirect, render_template, request, url_for, session, abort
from werkzeug.utils import secure_filename

from flaskps.models.instrument import Instrument
from flaskps.models.instrument_type import InstrumentType
from flaskps.models.entities.mappers.instrument_mapper import to_instrumento
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.helpers.config import sitio_habilitado
import os

upload_route = "./flaskps/static/uploads/"

@sitio_habilitado()
@requiere_permiso("docente_index")
def index():
    instrumentos = Instrument.all()
    return render_template('instrumento/index.html', instrumentos=instrumentos)

@sitio_habilitado()
@requiere_permiso("administrador_new")
def new():
    instrument_types = InstrumentType.all()
    return render_template('instrumento/new.html', tipos=instrument_types)

@sitio_habilitado()
@requiere_permiso("administrador_new")
def create():
    if not authenticated(session):
        abort(401)
        
    nombre_ruta = ""
    # Captura de la imagen
    if request.files:
        image = request.files["image"]
        nombre_ruta = secure_filename(image.filename)
        ruta = os.path.join(upload_route, nombre_ruta)
        image.save(ruta)


    nombre = request.form["nombre"]
    tipo_instrumento = request.form["tipo_instrumento"]

    tipo_instrumento_id = InstrumentType.get_by_name(tipo_instrumento).id
    requestNew = (nombre, tipo_instrumento_id, nombre_ruta)
    new_instrument = to_instrumento(requestNew)
    Instrument.save(new_instrument)
    return redirect(url_for('instrument_index'))

@sitio_habilitado()
@requiere_permiso("docente_show")
def show(id):
    instrument = Instrument.get_by_id(id)
    ruta = url_for('static', filename = 'uploads/' + instrument.ruta_imagen)
    instrument_type = InstrumentType.get_by_id(instrument.tipo_instrumento_id)
    return render_template('instrumento/show.html', nombre = instrument.nombre, tipo = instrument_type.nombre, ruta = ruta, id = id)

@sitio_habilitado()
@requiere_permiso("administrador_update")
def update(id):
    instrument = Instrument.get_by_id(id)
    ruta = url_for('static', filename = 'uploads/' + instrument.ruta_imagen)
    instrument_type = InstrumentType.get_by_id(instrument.tipo_instrumento_id)
    instrument_types = InstrumentType.all()
    return render_template('instrumento/update.html', id = id, nombre = instrument.nombre, tipo = instrument_type, tipos = instrument_types, ruta = ruta)

@sitio_habilitado()
@requiere_permiso("administrador_update")
def save():
    instrument_id = request.form.get("id")
    instrument = Instrument.get_by_id(instrument_id)
    nombre = request.form["nombre"]
    tipo_instrumento = request.form["tipo"]

    nombre_ruta = ""
    # Captura de la imagen
    if request.files and request.files["image"].filename != "":
        image = request.files["image"]
        nombre_ruta = image.filename
        ruta = os.path.join(upload_route, nombre_ruta)
        image.save(ruta)
    else:
        nombre_ruta = instrument.ruta_imagen

    tipo_instrumento_id = InstrumentType.get_by_name(tipo_instrumento).id
    requestEdit = (nombre, tipo_instrumento_id, nombre_ruta)
    edit_instrument = to_instrumento(requestEdit)
    Instrument.update(edit_instrument, instrument_id)
    return redirect(url_for('instrument_index'))

@sitio_habilitado()
@requiere_permiso("administrador_destroy")
def delete(id):
    Instrument.delete_by_numero_inventario(id)
    return redirect(url_for('instrument_index'))
