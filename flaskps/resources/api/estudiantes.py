from flask_restful import Resource, request
from flaskps.models.student import Student
from flaskps.helpers.response_builder import build_response

class EstudiantesSearch(Resource):

    def get(self):
        filter = {}
        filter["apellido"] = request.args["apellido"] if not None else ""
        filter["numero"] = request.args["numero"] if not None else ""
        search = Student.search(filter)
        estudiantes = []
        for est in search:
            e = {
                "id": est.id,
                "nombre": est.nombre,
                "apellido": est.apellido,
                "numero": est.numero
            }
            estudiantes.append(e)
        return build_response(estudiantes, estudiantes.__len__())
