from flaskps.models.horario_taller import HorarioTallerModel
from flaskps.models.entities.asistencia_estudiante_taller import AsistenciaEstudianteTaller
from flaskps.models.taller import EstudianteTallerModel
from flaskps.models.generic import Generic
import datetime


class AsistenciaModel(Generic):
    def get_entity():
        return AsistenciaEstudianteTaller

    def set_presente(id_estudiante, id_horario, fecha=None):
        if fecha is None:
            fecha = datetime.date.today()
        horario = HorarioTallerModel.find_by_id(id_horario)
        asist = AsistenciaEstudianteTaller(id_estudiante, horario.ciclo_lectivo_id, horario.taller_id, fecha)
        Generic.save(asist)

    def get_asistencia_by(fecha, ciclo=None, taller=None):
        asist = AsistenciaEstudianteTaller
        query = asist.query
        if ciclo is None:
            query = query.filter(asist.fecha == fecha).all()
        else:
            if taller is None:
                query = query.filter(asist.fecha == fecha, asist.ciclo_lectivo.id == ciclo)
            else:
                query = query.filter(asist.fecha == fecha, asist.ciclo_lectivo.id == ciclo, asist.taller.id == taller)
        return query.all()

    def get_asistencia_by_horario(horario, fecha=None):
        asist = AsistenciaEstudianteTaller
        if fecha is None:
            fecha = datetime.date.today()
        return asist.query.filter(asist.ciclo_lectivo == horario.ciclo_lectivo,
                                  asist.taller == horario.taller,
                                  EstudianteTallerModel.is_in_horario(asist.estudiante_id, horario.id),
                                  asist.fecha == fecha)
