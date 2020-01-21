from flaskps.models.generic import Generic
from flaskps.models.entities.horario_taller import HorarioTaller
from flaskps.models.ciclo_lectivo import CicloLectivoModel
import datetime


class HorarioTallerModel(Generic):

    def get_entity():
        return HorarioTaller

    def existe_horario(horario):
        query = HorarioTaller.query.filter(HorarioTaller.nucleo_id == horario.nucleo_id,
                                           HorarioTaller.ciclo_lectivo_id == horario.ciclo_lectivo_id,
                                           HorarioTaller.taller_id == horario.taller_id,
                                           HorarioTaller.dia_semana == horario.dia_semana,
                                           HorarioTaller.hora_inicio == horario.hora_inicio,
                                           HorarioTaller.hora_fin == horario.hora_fin)
        return query.first() is not None

    def get_horarios_by(id_ciclo, id_taller, id_nucleo):
        query = HorarioTaller.query.filter(HorarioTaller.ciclo_lectivo_id == id_ciclo,
                                           HorarioTaller.taller_id == id_taller,
                                           HorarioTaller.nucleo_id == id_nucleo)
        result = query.all()
        return result

    def get_horarios_by_taller_ciclo(id_ciclo, id_taller):
        query = HorarioTaller.query.filter(HorarioTaller.ciclo_lectivo_id == id_ciclo,
                                           HorarioTaller.taller_id == id_taller)
        result = query.all()
        return result

    def get_horarios_actuales():
        hoy = datetime.date.today().weekday() + 1
        ciclo_actual = CicloLectivoModel.ciclo_actual()
        query = HorarioTaller.query.filter(HorarioTaller.dia_semana == hoy,
                                           HorarioTaller.ciclo_lectivo == ciclo_actual)
        return query.all()
