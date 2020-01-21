from flaskps.models.asistencia import AsistenciaModel
from flaskps.models.taller import EstudianteTallerModel
from flaskps.models.horario_taller import HorarioTallerModel
from flask import render_template, request
import datetime


def index(id_ciclo, id_taller, id_horario):
    horario = HorarioTallerModel.find_by_id(id_horario)
    estudiantes = EstudianteTallerModel.get_by_horario(id_horario)

    hoy = datetime.date.today()
    return render_template("asistencia/index.html", horario=horario, hoy=hoy, estudiantes=estudiantes)
