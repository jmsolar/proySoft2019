from flask_restful import Resource
from flaskps.helpers.enums import DiaSemana


class DiaSemanaResource(Resource):

    def get(self):
        dias = DiaSemana._member_map_
        response = []
        for dia in dias:
            response.append(
                {
                    "id": dias.get(dia),
                    "dia": dia,
                }
            )
        return response
