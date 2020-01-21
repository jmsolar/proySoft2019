from flask import redirect, render_template, request, url_for, session, abort
from flaskps.models.entities.mappers.user_mapper import to_usuario
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.helpers.config import sitio_habilitado
from flaskps.apis import api_localidad, api_tipo_documento
from flaskps.models.gender import Gender
from flaskps.models.teacher import Teacher
from flaskps.models.entities.mappers.teacher_mapper import to_docente
import requests

@sitio_habilitado()
@requiere_permiso("docente_index")
def index():
	docentes = Teacher.all().items
	localidades = []
	for docente in docentes:
		resp = requests.get(api_localidad.url + "/" + str(docente.localidad_id))
		if resp.status_code != 200:
			localidades.append("Error al obtener la localidad")
		else:
			result = resp.json()
			localidades.append(format(result['nombre']))
	return render_template('docente/index.html', docentes = docentes, localidades = localidades)

@sitio_habilitado()
@requiere_permiso("docente_new")
def new():
	#Ver - https://hackersandslackers.com/forms-in-flask-wtforms/
	#Ver - https://flask-wtf.readthedocs.io/en/stable/
	#Ver - https://www.youtube.com/watch?v=vzaXBm-ZVOQ
	#Ver - https://www.youtube.com/watch?v=UIJKdCIEXUQ
	#Ver - https://plataforma.josedomingo.org/pledin/cursos/flask/curso/u19/

	#https://leafletjs.com/
	#https://www.adictosaltrabajo.com/2016/06/22/mapas-interactivos-con-leaflet-js/
	#https://mappinggis.com/2013/06/como-crear-un-mapa-con-leaflet/

	resp = requests.get(api_localidad.url)
	localidades = []
	if resp.status_code != 200:
		localidades.append("Error al obtener la localidad")
	else:
		localidades = resp.json()
	generos = Gender.all()

	resp = requests.get(api_tipo_documento.url)
	tiposDoc = []
	if resp.status_code != 200:
		tiposDoc.append("Error al obtener la localidad")
	else:
		tiposDoc = resp.json()
	return render_template('docente/new.html', localidades = localidades, generos = generos, tiposDoc = tiposDoc)

@sitio_habilitado()
@requiere_permiso("docente_new")
def create():
	if not authenticated(session):
		abort(401)
	new_teacher = to_docente(request.form)
	Teacher.save(new_teacher)
	return redirect(url_for('teacher_index'))

@sitio_habilitado()
@requiere_permiso("docente_update")
def edit(id):
	aDocente = Teacher.find_by_id(id)
	resp = requests.get(api_localidad.url)
	localidades = []
	if resp.status_code != 200:
		localidades.append("Error al obtener la localidad")
	else:
		localidades = resp.json()
	generos = Gender.all()

	resp = requests.get(api_tipo_documento.url)
	tiposDoc = []
	if resp.status_code != 200:
		tiposDoc.append("Error al obtener la localidad")
	else:
		tiposDoc = resp.json()
	return render_template('docente/edit.html',docente = aDocente,localidades = localidades, generos = generos, tiposDoc = tiposDoc)

@sitio_habilitado()
@requiere_permiso("docente_update")
def save():
	edit_doc = to_docente(request.form)
	id= request.form.get("id")
	Teacher.update(edit_doc,id)
	return redirect (url_for('teacher_index'))

@sitio_habilitado()
@requiere_permiso("docente_destroy")	
def delete(id):
	Teacher.delete_by_id(id)
	return redirect (url_for('teacher_index'))

def show(id):
	aDocente = Teacher.find_by_id(id)
	resp = requests.get(api_localidad.url)
	localidades = []
	if resp.status_code != 200:
		localidades.append("Error al obtener la localidad")
	else:
		localidades = resp.json()
	generos = Gender.all()

	resp = requests.get(api_tipo_documento.url)
	tiposDoc = []
	if resp.status_code != 200:
		tiposDoc.append("Error al obtener la localidad")
	else:
		tiposDoc = resp.json()
	return render_template('docente/show.html',docente = aDocente,localidades = localidades, generos = generos, tiposDoc = tiposDoc)
