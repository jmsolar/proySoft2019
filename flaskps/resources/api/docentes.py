from flask_restful import Resource, request
from flaskps.models.teacher import Teacher
from flaskps.helpers.response_builder import build_response


class DocentesSearch(Resource):

    def get(self):
        filter = {}
        filter["apellido"] = request.args["apellido"] if not None else ""
        filter["numero"] = request.args["numero"] if not None else ""
        search = Teacher.search(filter)
        docentes = []
        for doc in search:
            d = {
                "id": doc.id,
                "nombre": doc.nombre,
                "apellido": doc.apellido,
                "numero": doc.numero
            }
            docentes.append(d)
        return build_response(docentes, search.__len__())
