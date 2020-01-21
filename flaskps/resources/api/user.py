from flask_restful import Resource
from flask_restful import request
from flaskps.models.configuracion import Configuracion
from flaskps.models.user import User


class Users(Resource):

    def get(self):
        start = int(request.args['start'])
        page = 1
        if start != 0:
            page = start / Configuracion.get_config().registros_por_pagina + 1
        order = {'column': request.args['columns[' + request.args['order[0][column]'] + '][data]'],
                 'dir': request.args['order[0][dir]']}
        users = User.all(page, order)
        usuarios = []
        for user in users.items:
            u = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            }
            usuarios.append(u)
        return {
            "draw": request.args['draw'],
            "recordsTotal": users.total,
            "recordsFiltered": users.total,
            "data": usuarios
        }

    def inactivos(self):
        start = int(request.args['start'])
        page = 1
        if start != 0:
            page = start / Configuracion.get_config().registros_por_pagina + 1
        order = {'column': request.args['columns[' + request.args['order[0][column]'] + '][data]'],
                 'dir': request.args['order[0][dir]']}
        users = User.find_blocked(page, order)
        usuarios = []
        for user in users.items:
            u = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            }
            usuarios.append(u)
        return {
            "draw": request.args['draw'],
            "recordsTotal": users.total,
            "recordsFiltered": users.total,
            "data": usuarios
        }