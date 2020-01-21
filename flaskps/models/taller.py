from flaskps.models.entities.taller import Taller
from flaskps.db import db
from flaskps.models.generic import Generic
from flaskps.models.entities.docente_responsable_taller import DocenteResponsableTaller
from flaskps.models.entities.estudiante_taller import EstudianteTaller
from flaskps.models.horario_taller import HorarioTaller, HorarioTallerModel


class TallerModel(Generic):

    def get_entity():
        return Taller

    def get_docentes(ciclo_id, taller_id):
        docente = DocenteResponsableTaller.query \
            .filter(DocenteResponsableTaller.taller_id == taller_id,
                    DocenteResponsableTaller.ciclo_lectivo_id == ciclo_id) \
            .all()
        docentes= []
        for doc in docente:
            docentes.append(doc.docente)
        return docentes

    def get_estudiantes(ciclo_id, taller_id):
        estudiantes_taller = EstudianteTaller.query\
            .join(HorarioTaller)\
            .filter(HorarioTaller.taller_id == taller_id,
                    HorarioTaller.ciclo_lectivo_id == ciclo_id)\
            .all()
        estudiantes = []
        for est in estudiantes_taller:
            if est.estudiante not in estudiantes:
                estudiantes.append(est.estudiante)
        return estudiantes

    def add_estudiante(id_estudiante, id_horario):
        est_taller = EstudianteTaller(id_estudiante, id_horario)
        EstudianteTallerModel.save(est_taller)

    def add_docente(id_docente, id_ciclo, id_taller):
        doc_resp = DocenteResponsableTaller(id_docente, id_ciclo, id_taller)
        DocenteResponsableTallerModel.save(doc_resp)

    def delete_estudiante(id_estudiante, id_ciclo, id_taller):
        horarios = HorarioTallerModel.get_horarios_by_taller_ciclo(id_ciclo, id_taller)
        for horario in horarios:
            if EstudianteTallerModel.is_in_horario(id_estudiante, horario.id):
                EstudianteTallerModel.delete(id_estudiante, horario.id)

    def delete_docente(id_docente, id_ciclo, id_taller):
        DocenteResponsableTallerModel.delete(id_docente, id_ciclo, id_taller)


class EstudianteTallerModel(Generic):
    def get_entity():
        return EstudianteTaller

    def is_in_horario(id_estudiante, id_horario):
        query = EstudianteTaller.query.filter(EstudianteTaller.horario_id == id_horario,
                                              EstudianteTaller.estudiante_id == id_estudiante)
        return query.first() is not None

    def get_by_horario(id_horario):
        query = EstudianteTaller.query.filter(EstudianteTaller.horario_id == id_horario)
        estudiantes = []
        for est in query.all():
            estudiantes.append(est.estudiante)
        return estudiantes

    def delete(id_estudiante, id_horario):
        e = EstudianteTaller
        t = e.query.filter(e.estudiante_id == id_estudiante
                                          , e.horario_id == id_horario).first()
        db.session.delete(t)
        db.session.commit()
        return True


class DocenteResponsableTallerModel(Generic):
    def get_entity():
        return DocenteResponsableTaller

    def delete(id_docente, id_ciclo, id_taller):
        e = DocenteResponsableTaller
        t = e.query.filter(e.docente_id == id_docente
                           , e.ciclo_lectivo_id == id_ciclo
                           , e.taller_id == id_taller).first()
        db.session.delete(t)
        db.session.commit()
        return True
