from flask import redirect, render_template, request, url_for, session, abort
from flaskps.helpers.auth import authenticated, requiere_permiso
from flaskps.helpers.enums import DiaSemana
from flaskps.models.taller import TallerModel
from flaskps.models.horario_taller import HorarioTallerModel
from flaskps.models.entities.horario_taller import HorarioTaller
from flaskps.models.configuracion import Configuracion


def show(id_ciclo, id_taller):
    taller = TallerModel.find_by_id(id_taller)
    ciclo_lectivo = next((x for x in taller.ciclos_lectivos if x.id == id_ciclo), None)
    docentes = TallerModel.get_docentes(id_ciclo, id_taller)
    estudiantes = TallerModel.get_estudiantes(id_ciclo, id_taller)
    config = Configuracion.get_config()

    return render_template("taller/index.html", taller=taller, config=config
                           , ciclo_lectivo=ciclo_lectivo
                           , docentes=docentes, estudiantes=estudiantes)


def new_estudiante(id_ciclo, id_taller):
    taller = TallerModel.find_by_id(id_taller)
    ciclo_lectivo = next((x for x in taller.ciclos_lectivos if x.id == id_ciclo), None)
    config = Configuracion.get_config()
    return render_template("taller/add_estudiante.html", taller=taller, ciclo_lectivo=ciclo_lectivo, config=config)


def add_estudiante(id_ciclo, id_taller):
    id_estudiante = int(request.form["estudiante"])
    id_horario = int(request.form["horario"])
    TallerModel.add_estudiante(id_estudiante, id_horario)
    return show(id_ciclo, id_taller)


def add_docente(id_ciclo, id_taller):
    id_docente = int(request.form["id_docente"])
    TallerModel.add_docente(id_docente, id_ciclo, id_taller)


def delete_sujeto(id_ciclo, id_taller):
    sujeto = request.form["sujeto"]
    id = int(request.form['id'])
    if sujeto == "estudiante":
        TallerModel.delete_estudiante(id, id_ciclo, id_taller)
    if sujeto == "docente":
        TallerModel.delete_docente(id, id_ciclo, id_taller)
    return show(id_ciclo, id_taller)


def horarios(id_ciclo, id_taller):
    horarios_list = HorarioTallerModel.get_horarios_by_taller_ciclo(id_ciclo, id_taller)
    taller = TallerModel.find_by_id(id_taller)
    ciclo_lectivo = next((x for x in taller.ciclos_lectivos if x.id == id_ciclo), None)
    config = Configuracion.get_config()

    return render_template("taller/horarios.html", taller=taller, horarios=horarios_list
                           , ciclo_lectivo=ciclo_lectivo, config=config)


def add_horario(id_ciclo, id_taller):
    nucleo = request.form["nucleo"]
    dia_semana = request.form["dia_semana"]
    horario = HorarioTaller(nucleo, id_ciclo, id_taller, dia_semana)
    HorarioTallerModel.save(horario)


def delete_horario(id_ciclo, id_taller):
    HorarioTallerModel.delete_by_id(request.form['horario'])
