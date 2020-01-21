from flask_restful import Resource
import datetime
from flaskps.helpers.response_builder import error_response, success_response
from flask import request
from flaskps.models.asistencia import AsistenciaModel


class Asistencia(Resource):

    def post(self):
        try:
            ids = request.form["ids_estudiantes"]
            horario = request.form["horario"]
            fecha = datetime.datetime.strptime(request.form["fecha"], "%Y%m%d")
            for id in ids.split(","):
                AsistenciaModel.set_presente(id, horario, fecha)
            return success_response("Se ha enviado la asistencia correctamente")
        except Exception as e:
            return error_response(500, "Ha ocurrido un error inesperado")
