from flask import redirect, render_template, request, url_for, session, abort
from flaskps.models.configuracion import Configuracion
from flaskps.models.entities.mappers.administracion_mapper import to_ciclo_lectivo
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.models.ciclo_lectivo import CicloLectivoModel
from flaskps.models.taller import TallerModel


@requiere_permiso("administracion_index")
def index():
    return render_template('administracion/index.html')


@requiere_permiso("administracion_show")
def ciclo_lectivo():
    ciclo_actual = CicloLectivoModel.ciclo_actual()
    ciclo_proximo = CicloLectivoModel.ciclo_proximo()
    return render_template('ciclo_lectivo/index.html', ciclo_actual=ciclo_actual, ciclo_proximo=ciclo_proximo)


@requiere_permiso("administracion_show")
def ciclo_lectivo_show(id):

    ciclo_lectivo = CicloLectivoModel.find_by_id(id)

    return render_template('ciclo_lectivo/show.html', ciclo_lectivo=ciclo_lectivo)


def ciclo_lectivo_new():
    return render_template("ciclo_lectivo/new.html")


def ciclo_lectivo_create():

    new_ciclo = to_ciclo_lectivo(request.form)
    if(CicloLectivoModel.invalid(new_ciclo)):
        error = "Las fechas se superponen con otro ciclo lectivo"
        return render_template("ciclo_lectivo/new.html", error=error)

    CicloLectivoModel.save(new_ciclo)
    return render_template("ciclo_lectivo/index.html")


def ciclo_lectivo_add_taller(id):
    taller = TallerModel.find_by_id(request.form["taller"])
    CicloLectivoModel.add_taller(id, taller)

    return render_template('ciclo_lectivo/show.html', ciclo_lectivo=ciclo_lectivo)
