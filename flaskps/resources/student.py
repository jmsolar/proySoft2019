from flask import redirect, render_template, request, url_for, session, abort
from flaskps.models.neighborhood import Neighborhood
from flaskps.models.student import Student
from flaskps.models.level import Level
from flaskps.models.gender import Gender
from flaskps.models.school import School
from flaskps.models.entities.mappers.student_mapper import to_estudiante
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.apis import api_localidad, api_tipo_documento
from flaskps.helpers.config import sitio_habilitado
import requests

@sitio_habilitado()
@requiere_permiso("docente_index")
@requiere_permiso("preceptor_index")
def index():
    estudiantes = Student.all()
    localidades = []
    for estudiante in estudiantes:
        resp = requests.get(api_localidad.url + "/" + str(estudiante.localidad_id))
        if resp.status_code != 200:
            localidades.append("Error al obtener la localidad")
        else:
            result = resp.json()
            localidades.append(format(result['nombre']))
    return render_template('estudiante/index.html', estudiantes = estudiantes, localidades = localidades)

@sitio_habilitado()
@requiere_permiso("docente_show")
@requiere_permiso("preceptor_show")
def show():
    return render_template('estudiante/show.html')

@sitio_habilitado()
@requiere_permiso("docente_update")
@requiere_permiso("preceptor_update")
def update(id):
    estudiante = Student.find_by_id(id)
    resp = requests.get(api_localidad.url + "/" + str(estudiante.localidad_id))
    result = resp.json()
    localidad = format(result['nombre'])
    nivel = Level.find_by_id(estudiante.nivel_id)
    genero = Gender.find_by_id(estudiante.genero_id)
    resp = requests.get(api_tipo_documento.url + "/" + str(estudiante.tipo_doc_id))
    result = resp.json()
    tipoDoc = format(result['nombre'])
    escuela = School.find_by_id(estudiante.escuela_id)
    barrio = Neighborhood.find_by_id(estudiante.barrio_id)

    resp = requests.get(api_localidad.url)
    localidades = []
    if resp.status_code != 200:
        localidades.append("Error al obtener la localidad")
    else:
        localidades = resp.json()
    niveles = Level.all()
    generos = Gender.all()
    escuelas = School.all()
    barrios = Neighborhood.all()

    resp = requests.get(api_tipo_documento.url)
    tiposDoc = []
    if resp.status_code != 200:
        tiposDoc.append("Error al obtener la localidad")
    else:
        tiposDoc = resp.json()
    return render_template('estudiante/update.html', estudiante = estudiante, localidad = localidad, localidades = localidades, tipoDoc = tipoDoc, tiposDoc = tiposDoc, nivel = nivel, niveles = niveles, genero = genero, generos = generos, escuela = escuela, escuelas = escuelas, barrio = barrio, barrios = barrios, id = estudiante.id)

@sitio_habilitado()
@requiere_permiso("administrador_destroy")	
def delete(id):
    Student.delete_by_id(id)
    return redirect (url_for('student_index'))

@sitio_habilitado()
@requiere_permiso("docente_update")
@requiere_permiso("preceptor_update")
def save():
    localidad_param = request.form['localidad']
    resp = requests.get(api_localidad.url)
    localidades = resp.json()
    
    for localidad in localidades:
        if format(localidad['nombre']) == localidad_param:
            localidad_id = localidad['id']
            localidad_id = localidad_id
            break

    nivel = request.form["nivel"]
    nivel = Level.find_by_name(nivel)
    nivel_id = nivel.id

    genero = request.form["genero"]
    genero = Gender.find_by_name(genero)
    genero_id = genero.id

    escuela = request.form["escuela"]
    escuela = School.find_by_name(escuela)
    escuela_id = escuela.id

    tipodoc_param = request.form['tipo_doc']
    resp = requests.get(api_tipo_documento.url)
    documentos = resp.json()
    
    for doc in documentos:
        if format(doc['nombre']) == tipodoc_param:
            tipo_doc_id = doc['id']
            tipo_doc_id = tipo_doc_id
            break

    barrio = request.form["barrio"]
    barrio = Neighborhood.find_by_name(barrio)
    barrio_id = barrio.id

    apellido = request.form['apellido']
    nombre = request.form['nombre']
    fecha_nac = request.form["fecha_nac"]
    domicilio = request.form["domicilio"]
    numero = request.form["numero"]
    tel = request.form["tel"]

    requestNew = (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id)
    edit_student = to_estudiante(requestNew)
    id = request.form.get('id')
    Student.update(edit_student, id)
    return redirect(url_for('student_index'))

@sitio_habilitado()
@requiere_permiso("administrador_new")
def new():
    resp = requests.get(api_localidad.url)
    localidades = []
    if resp.status_code != 200:
        localidades.append("Error al obtener la localidad")
    else:
        localidades = resp.json()
    niveles = Level.all()
    generos = Gender.all()
    escuelas = School.all()
    barrios = Neighborhood.all()

    resp = requests.get(api_tipo_documento.url)
    tiposDoc = []
    if resp.status_code != 200:
        tiposDoc.append("Error al obtener la localidad")
    else:
        tiposDoc = resp.json()
    
    return render_template('estudiante/new.html', localidades = localidades, niveles = niveles, generos = generos, escuelas = escuelas, tiposDoc = tiposDoc, barrios = barrios)

@sitio_habilitado()
@requiere_permiso("administrador_new")
def create():
    if not authenticated(session):
        abort(401)

    localidad_param = request.form['localidad']
    resp = requests.get(api_localidad.url)
    localidades = resp.json()
    
    for localidad in localidades:
        if format(localidad['nombre']) == localidad_param:
            localidad_id = localidad['id']
            break

    nivel = request.form["nivel"]
    nivel = Level.find_by_name(nivel)
    nivel_id = nivel.id

    genero = request.form["genero"]
    genero = Gender.find_by_name(genero)
    genero_id = genero.id

    escuela = request.form["escuela"]
    escuela = School.find_by_name(escuela)
    escuela_id = escuela.id

    tipodoc_param = request.form['tipo_doc']
    resp = requests.get(api_tipo_documento.url)
    documentos = resp.json()
    
    for doc in documentos:
        if format(doc['nombre']) == tipodoc_param:
            tipo_doc_id = doc['id']
            break

    barrio = request.form["barrio"]
    barrio = Neighborhood.find_by_name(barrio)
    barrio_id = barrio.id

    apellido = request.form['apellido']
    nombre = request.form['nombre']
    fecha_nac = request.form["fecha_nac"]
    domicilio = request.form["domicilio"]
    numero = request.form["numero"]
    tel = request.form["tel"]
    requestNew = (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id)

    new_estudiante = to_estudiante(requestNew)
    Student.save(new_estudiante)
    return redirect(url_for('student_index'))