from flask_restful import Resource
from flask_restful import request
from flaskps.models.ciclo_lectivo import CicloLectivoModel
from flaskps.models.configuracion import Configuracion


class CicloLectivo(Resource):

    def get(self):
        datatables = False
        page = None
        if request.args.__len__() == 0:
            ciclos = CicloLectivoModel.all()
        else:
            datatables = True
            start = int(request.args['start'])
            page = 1
            if start != 0:
                page = start / Configuracion.get_config().registros_por_pagina + 1
            order = {'column': request.args['columns[' + request.args['order[0][column]'] + '][data]'],
                     'dir': request.args['order[0][dir]']}
            page = CicloLectivoModel.all_by_page(page, order)
            ciclos = page.items
        ciclos_lectivos = []
        for ciclo in ciclos:
            semestre = "Primero" if (ciclo.semestre == 0) else "Segundo"
            c = {
                "id": ciclo.id,
                "fecha_ini": ciclo.fecha_ini.strftime("%d/%m/%Y"),
                "fecha_fin": ciclo.fecha_fin.strftime("%d/%m/%Y"),
                "semestre": semestre
            }
            ciclos_lectivos.append(c)
        if datatables:
            return {
                "draw": request.args['draw'],
                "recordsTotal": page.total,
                "recordsFiltered": page.total,
                "data": ciclos_lectivos
            }
        else:
            return ciclos_lectivos


class CicloLectivoTalleres(Resource):

    def get(self, id):
        ciclo = CicloLectivoModel.find_by_id(id)
        talleres = []
        for taller in ciclo.talleres:
            t = {
                "id": taller.id,
                "nombre": taller.nombre
            }
            talleres.append(t)
        return {
            "talleres": talleres
        }
