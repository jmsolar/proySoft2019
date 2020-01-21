from flaskps.models.horario_taller import HorarioTallerModel, HorarioTaller
from flaskps.helpers.response_builder import error_response, success_response
from flask_restful import Resource, request
from flaskps.helpers.enums import get_day
from flaskps.helpers.GCalendar import createEventTaller,createEventCiclo
from flaskps.models.taller import TallerModel
from flaskps.models.ciclo_lectivo import CicloLectivoModel
from flaskps.models.nucleo import NucleoModel
from datetime import datetime,timedelta
import logging


class HorarioTallerResource(Resource):

    def post(self, id_ciclo, id_taller):
        try:
            nucleo = request.form['nucleo']
            dia_semana = request.form['dia_semana']
            hora_inicio = request.form['hora_inicio']
            hora_fin = request.form['hora_fin']
            if hora_fin == "" or hora_inicio == "":
                return error_response(409, "Debe ingresar una franja horaria válida")
            if hora_inicio >= hora_fin:
                return error_response(409, "Debe ingresar una hora de inicio menor que hora de fin")
            new_horario = HorarioTaller(nucleo, id_ciclo, id_taller, dia_semana, hora_inicio, hora_fin)
            if HorarioTallerModel.existe_horario(new_horario):
                return error_response(409, "Ya existe el horario")
            #print(hora_inicio)
            print(hora_fin)   
            tallerRec = TallerModel.find_by_id(id_taller)
            cicloRec = CicloLectivoModel.find_by_id(id_ciclo)
            nucleoRec = NucleoModel.find_by_id(nucleo)
            dias = timedelta(days=int(dia_semana)-1)
            fechaEvento = cicloRec.fecha_ini+dias
            fechaEventoFin = cicloRec.fecha_fin.date().strftime("%Y-%m-%d")
            #logging.debug('This is a debug message')
            createEventTaller(tallerRec.nombre,nucleoRec.nombre,fechaEvento.date().strftime("%Y-%m-%d"),fechaEventoFin,hora_inicio,hora_fin)
            #print(tallerRec)
            HorarioTallerModel.save(new_horario)
            return success_response()
        except Exception as e:
            return error_response(500, format(e))

    def get(self, id_ciclo, id_taller):
        try:
            nucleo = request.args['nucleo']
            horarios = HorarioTallerModel.get_horarios_by(id_ciclo, id_taller, nucleo)
            response = []
            for horario in horarios:
                n = {
                    "id": horario.id,
                    "dia": get_day(horario.dia_semana) + " (" + horario.hora_inicio + " - " + horario.hora_fin + ")"
                }
                response.append(n)
            return response
        except Exception as e:
            return error_response(500, "Ha ocurrido un error")
