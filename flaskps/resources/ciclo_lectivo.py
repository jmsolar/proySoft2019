from flask import redirect, render_template, request, url_for, session, abort
from flaskps.models.entities.mappers.administracion_mapper import to_ciclo_lectivo
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.models.ciclo_lectivo import CicloLectivoModel
from flaskps.models.taller import TallerModel
from flaskps.helpers.GCalendar import createEventCiclo
from datetime import datetime

@requiere_permiso("administracion_show")
def index():
    ciclo_actual = CicloLectivoModel.ciclo_actual()
    ciclo_proximo = None
    if ciclo_actual is not None:
        ciclo_proximo = CicloLectivoModel.ciclo_proximo()
    return render_template('ciclo_lectivo/index.html', ciclo_actual=ciclo_actual, ciclo_proximo=ciclo_proximo)


@requiere_permiso("administracion_show")
def show(id):

    ciclo_lectivo = CicloLectivoModel.find_by_id(id)

    return render_template('ciclo_lectivo/show.html', ciclo_lectivo=ciclo_lectivo)


@requiere_permiso("administracion_new")
def new():
    return render_template("ciclo_lectivo/new.html")


@requiere_permiso("administracion_new")
def create():

    form = request.form
    if form["fecha_fin"] == "" or form["fecha_ini"] == "":
        error_msg = "Por favor ingrese las fechas"
        error = "fechas"
        return render_template("ciclo_lectivo/new.html", error=error, error_msg=error_msg)

    if "semestre" not in form:
        error_msg = "Por favor seleccione un semestre"
        error = "semestre"
        return render_template("ciclo_lectivo/new.html", error=error, error_msg=error_msg)

    new_ciclo = to_ciclo_lectivo(form)
    if CicloLectivoModel.invalid(new_ciclo):
        error_msg = "Las fechas se superponen con otro ciclo lectivo"
        error = "fechas"
        return render_template("ciclo_lectivo/new.html", error=error, error_msg=error_msg)
    if new_ciclo.fecha_ini > new_ciclo.fecha_fin:
        error_msg = "Fecha de inicio no puede ser mayor que la fecha de fin"
        error = "fechas"
        return render_template("ciclo_lectivo/new.html", error=error, error_msg=error_msg)
    createEventCiclo(form["fecha_ini"],form["fecha_fin"])  
    CicloLectivoModel.save(new_ciclo)
    return render_template("ciclo_lectivo/index.html")


@requiere_permiso("administracion_update")
def add_taller(id):
    taller = TallerModel.find_by_id(request.form["taller"])
    CicloLectivoModel.add_taller(id, taller)


@requiere_permiso("administracion_update")
def delete_taller(id):
    taller = TallerModel.find_by_id(request.form["id"])
    CicloLectivoModel.delete_taller(id, taller)

