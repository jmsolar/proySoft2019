from datetime import datetime
from flaskps.models.generic import Generic
from flaskps.models.entities.ciclo_lectivo import CicloLectivo
from flaskps.db import db, Session


class CicloLectivoModel(Generic):

    def get_entity():
        return CicloLectivo

    def add_taller(id, taller):
        ciclo = CicloLectivo.query.filter_by(id=id).first()
        ciclo.talleres.append(taller)

        db.session.commit()

    def ciclo_actual():
        today = datetime.now()
        ciclo = CicloLectivo.query\
            .filter((CicloLectivo.fecha_ini < today) & (today < CicloLectivo.fecha_fin))\
            .first()
        return ciclo

    def ciclo_proximo():
        actual = CicloLectivoModel.ciclo_actual()
        proximo = CicloLectivo.query\
            .filter(CicloLectivo.fecha_ini > actual.fecha_fin)\
            .order_by(CicloLectivo.fecha_ini)\
            .first()
        return proximo

    def invalid(ciclo):
        result = CicloLectivo.query\
            .filter((CicloLectivo.fecha_ini <= ciclo.fecha_fin) & (ciclo.fecha_fin <= CicloLectivo.fecha_fin)
                    & (CicloLectivo.fecha_ini <= ciclo.fecha_ini) & (ciclo.fecha_ini <= CicloLectivo.fecha_fin))\
            .first()
        return result is not None
