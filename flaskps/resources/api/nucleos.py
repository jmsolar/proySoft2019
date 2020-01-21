from flask import request

from flaskps.models.nucleo import NucleoModel
from flask_restful import Resource


class Nucleos(Resource):

    def get(self):
        filter = {}
        if request.args.__len__() != 0:
            filter["ciclo_lectivo"] = request.args["ciclo_lectivo"]
            filter["taller"] = request.args["taller"]
        nucleos = NucleoModel.get_all(filter)
        response = []
        for nucleo in nucleos:
            n = {
                "id": nucleo.id,
                "nombre": nucleo.nombre
            }
            response.append(n)
        return response
