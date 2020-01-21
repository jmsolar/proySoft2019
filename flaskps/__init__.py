from os import path
from flask import Flask, render_template, g
from flask_restful import Api
from flask_session import Session
from flaskps.resources import user
from flaskps.resources import auth
from flaskps.resources import configuracion
from flaskps.resources import administracion
from flaskps.resources import ciclo_lectivo
from flaskps.resources import taller
from flaskps.resources import instrument
from flaskps.resources import asistencia
from flaskps.resources.api import ciclos_lectivos
from flaskps.resources.api import estudiantes
from flaskps.resources.api import docentes
from flaskps.resources.api.asistencia import Asistencia
from flaskps.resources.api.user import Users
from flaskps.resources.api.talleres import Talleres
from flaskps.resources.api.nucleos import Nucleos
from flaskps.resources.api.utils import DiaSemanaResource
from flaskps.resources.api.horarios import HorarioTallerResource
from flaskps.resources.api.talleres import EstudianteTaller
from flaskps.resources import student
from flaskps.resources import teacher
from flaskps.models.configuracion import Configuracion
from flaskps.models.horario_taller import HorarioTallerModel
from flaskps.config import Config
from flaskps.helpers import handler
from flaskps.helpers import auth as helper_auth
from flaskps.helpers.auth import authenticated
from flaskps.helpers.config import sitio_habilitado
from flaskps.helpers.enums import get_day
from flaskps.db import db
from flaskps.helpers.auth import authenticated, requiere_permiso

# Configuración inicial de la app
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Inicialización de base de datos con sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = Config.URI
db.init_app(app)

# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
app.jinja_env.globals.update(has_permission=helper_auth.has_permission)
app.jinja_env.globals.update(has_role=helper_auth.has_role)
app.jinja_env.globals.update(dia_semana=get_day)

# Autenticación
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
app.add_url_rule(
    "/autenticacion",
    'auth_authenticate',
    auth.authenticate,
    methods=['POST']
)

# Usuarios
app.add_url_rule("/usuarios", 'user_index', user.index)
app.add_url_rule("/usuarios", 'user_create', user.create, methods=['POST'])
app.add_url_rule("/usuarios/nuevo", 'user_new', user.new)
app.add_url_rule("/usuarios/inactivos", 'user_inactivos', user.inactivos)


@app.route("/usuarios/activar/<id>")
@sitio_habilitado()
def activar(id):
    return user.activar(id)


@app.route("/usuarios/activar/todos")
@sitio_habilitado()
def todos():
    return user.activar_todos()


@app.route("/usuarios/editar/<id>")
@sitio_habilitado()
def edit(id):
    return user.edit(id)


app.add_url_rule("/usuario/editar", 'user_save', user.save, methods=['POST'])


@app.route("/usuarios/eliminar/<id>")
@sitio_habilitado()
def usuario_eliminar(id):
    return user.delete(id)


# Configuracion
app.add_url_rule("/configuracion", 'configuration_index', configuracion.index)
app.add_url_rule("/configuracion/edit", 'configuration_edit', configuracion.edit)
app.add_url_rule("/configuracion/edit", 'configuracion_save', configuracion.save, methods=['POST'])
app.add_url_rule("/mantenimiento", 'mantenimiento')

# Estudiantes
app.add_url_rule("/estudiantes", 'student_index', student.index)
app.add_url_rule("/estudiantes", 'student_create', student.create, methods=['POST'])
app.add_url_rule("/estudiantes/nuevo", 'student_new', student.new)


@app.route("/estudiantes/detalle/<id>")
@sitio_habilitado()
@requiere_permiso("docente_show")
@requiere_permiso("preceptor_show")
def show(id):
    estudiante = Student.find_by_id(id)
    resp = requests.get(api_localidad.url + "/" + str(estudiante.localidad_id))
    result = resp.json()
    localidad = format(result['nombre'])
    nivel = Level.find_by_id(estudiante.nivel_id)
    genero = Gender.find_by_id(estudiante.genero_id)
    resp = requests.get(api_tipo_documento.url + "/" + str(estudiante.tipo_doc_id))
    result = resp.json()
    tipo_doc = format(result['nombre'])
    escuela = School.find_by_id(estudiante.escuela_id)
    barrio = Neighborhood.find_by_id(estudiante.barrio_id)
    return render_template('estudiante/show.html', estudiante=estudiante, localidad=localidad, tipo_doc=tipo_doc,
                           nivel=nivel, genero=genero, escuela=escuela, barrio=barrio)


@app.route("/estudiantes/eliminar/<id>")
@sitio_habilitado()
@requiere_permiso("administrador_destroy")
def estudiante_eliminar(id):
    return student.delete(id)


@app.route("/estudiantes/editar/<id>")
@sitio_habilitado()
@requiere_permiso("docente_show")
@requiere_permiso("preceptor_show")
def estudiante_editar(id):
    return student.update(id)


app.add_url_rule("/estudiante/editar", 'student_save', student.save, methods=['POST'])

# Docente
app.add_url_rule("/docentes", 'teacher_index', teacher.index)
app.add_url_rule("/docentes/nuevo", 'teacher_new', teacher.new)
app.add_url_rule("/docentes", 'teacher_create', teacher.create, methods=['POST'])


@app.route("/docentes/editar/<id>")
def editTeacher(id):
    return teacher.edit(id)


app.add_url_rule("/docentes/editar", 'teacher_save', teacher.save, methods=['POST'])


@app.route("/docentes/eliminar/<id>")
def docente_eliminar(id):
    return teacher.delete(id)


@app.route("/docentes/show/<id>")
def docente_show(id):
    return teacher.show(id)


# #########################
#  Módulo administracion  #
# #########################

# Index
app.add_url_rule("/administracion", "administracion_index", administracion.index)

# Ciclo lectivo
app.add_url_rule("/administracion/ciclos_lectivos", "ciclo_lectivo_index", ciclo_lectivo.index)
app.add_url_rule("/administracion/ciclos_lectivos", 'ciclo_lectivo_create', ciclo_lectivo.create, methods=['POST'])
app.add_url_rule("/administracion/ciclos_lectivos/nuevo", 'ciclo_lectivo_new', ciclo_lectivo.new)
app.add_url_rule("/administracion/ciclos_lectivos/<int:id>", "ciclo_lectivo_show", ciclo_lectivo.show)
app.add_url_rule("/administracion/ciclos_lectivos/<int:id>/talleres/nuevo", "ciclo_lectivo_add_taller"
                 , ciclo_lectivo.add_taller, methods=['POST'])
app.add_url_rule("/administracion/ciclos_lectivos/<int:id>/talleres/eliminar", "ciclo_lectivo_delete_taller"
                 , ciclo_lectivo.delete_taller, methods=['POST'])

# Taller
app.add_url_rule("/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>"
                 , "ciclo_lectivo_taller", taller.show)
app.add_url_rule("/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>"
                 , "taller_delete_sujeto", taller.delete_sujeto, methods=['POST'])
app.add_url_rule("/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>/estudiantes"
                 , "taller_new_estudiante", taller.new_estudiante)
app.add_url_rule("/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>/docentes"
                 , "taller_add_docente", taller.add_docente, methods=['POST'])

# Instrumentos
app.add_url_rule("/instrumentos", 'instrument_index', instrument.index)
app.add_url_rule("/instrumentos", 'instrument_create', instrument.create, methods=['POST'])
app.add_url_rule("/instrumentos/nuevo", 'instrument_new', instrument.new)


@app.route("/instrumentos/show/<id>")
@sitio_habilitado()
@requiere_permiso("docente_show")
def instrument_show(id):
    return instrument.show(id)


@app.route("/instrumentos/eliminar/<id>")
@sitio_habilitado()
@requiere_permiso("administrador_destroy")
def instrument_eliminar(id):
    return instrument.delete(id)


@sitio_habilitado()
@requiere_permiso("administrador_update")
@app.route("/instrumentos/editar/<id>")
def instrument_edit(id):
    return instrument.update(id)


app.add_url_rule("/instrumentos/editar", 'instrument_save', instrument.save, methods=['POST'])

# Horarios
app.add_url_rule("/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>/horarios"
                 , "taller_horarios", taller.horarios)
app.add_url_rule("/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>/horarios/nuevo",
                 "taller_add_horario", taller.add_horario, methods=['POST'])
app.add_url_rule("/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>/horarios/delete",
                 "taller_delete_horario", taller.delete_horario, methods=['DELETE'])

# Asistencia
app.add_url_rule(
    "/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>/horarios/<id_horario>/asistencia"
    , "taller_asistencia", asistencia.index)


# Ruta por defecto
@app.route("/")
@sitio_habilitado()
def home():
    configuracion = Configuracion.get_config()
    talleres_hoy = HorarioTallerModel.get_horarios_actuales()
    return render_template('home.html', configuracion=configuracion, talleres_hoy=talleres_hoy)


@app.route("/mantenimiento")
def mantenimiento():
    return render_template('mantenimiento.html')
#Calendario
@app.route("/calendario")
def calendario():
    return render_template('calendario/index.html')    


# APIs
api.add_resource(ciclos_lectivos.CicloLectivo, "/api/administracion/ciclos_lectivos")
api.add_resource(ciclos_lectivos.CicloLectivoTalleres, "/api/administracion/ciclos_lectivos/<int:id>/talleres")
api.add_resource(HorarioTallerResource
                 , "/api/administracion/ciclos_lectivos/<int:id_ciclo>/talleres/<int:id_taller>/horarios")
api.add_resource(EstudianteTaller,
                 "/api/administracion/ciclos_lectivos/talleres/estudiantes")
api.add_resource(Talleres, "/api/talleres")
api.add_resource(Users, "/api/usuarios")
api.add_resource(Nucleos, "/api/nucleos")
api.add_resource(DiaSemanaResource, "/api/dia_semana")
api.add_resource(estudiantes.EstudiantesSearch, "/api/estudiantes/search")
api.add_resource(docentes.DocentesSearch, "/api/docentes/search")
api.add_resource(Asistencia, "/api/asistencia")

# Handlers
app.register_error_handler(404, handler.not_found_error)
app.register_error_handler(401, handler.unauthorized_error)
# Implementar lo mismo para el error 500 y 401
