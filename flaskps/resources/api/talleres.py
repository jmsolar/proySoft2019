from flask import request
from flask_restful import Resource
from flaskps.models.taller import TallerModel, EstudianteTallerModel
from flaskps.helpers.response_builder import success_response, error_response, build_response


class Talleres(Resource):

    def get(self):
        talleres = TallerModel.all({"column": "nombre", "dir": "asc"})
        result = []
        for taller in talleres:
            t = {
                "id": taller.id,
                "nombre": taller.nombre,
                "nombre_corto": taller.nombre_corto
            }
            result.append(t)
        return result


class EstudianteTaller(Resource):

    def get(self):
        horario = request.args["horario"]
        search = EstudianteTallerModel.get_by_horario(horario)
        estudiantes = []
        for est in search:
            e = {
                "id": est.id,
                "nombre": est.nombre,
                "apellido": est.apellido,
                "nivel": est.nivel.nombre
            }
            estudiantes.append(e)
        return build_response(estudiantes, estudiantes.__len__())

    def post(self):
        try:
            id_estudiante = request.form["estudiante"]
            id_horario = request.form["horario"]
            if id_horario == "":
                return error_response(422, "horario")
            if id_estudiante == "":
                return error_response(422, "estudiante")
            if EstudianteTallerModel.is_in_horario(id_estudiante, id_horario):
                return error_response(409, "El estudiante ya esta asignado al horario seleccionado")
            TallerModel.add_estudiante(id_estudiante, id_horario)
            return success_response("Se ha agregado correctamente el estudiante")
        except Exception as e:
            return error_response(500, "Ha ocurrido un error inesperado")
