from flaskps.models.entities.nucleo import Nucleo
from flaskps.models.entities.horario_taller import HorarioTaller
from flaskps.models.generic import Generic


class NucleoModel(Generic):

    def get_entity():
        return Nucleo

    def get_all(filter):
        if len(filter) == 0:
            return NucleoModel.all()
        else:
            return Nucleo.query.filter(
                Nucleo.id.in_(HorarioTaller.query.with_entities(HorarioTaller.nucleo_id).filter(
                    HorarioTaller.ciclo_lectivo_id == filter["ciclo_lectivo"],
                    HorarioTaller.taller_id == filter["taller"]))).all()
