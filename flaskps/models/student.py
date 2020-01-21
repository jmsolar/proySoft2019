from flaskps.models.entities.estudiante import Estudiante
from flaskps.models.generic import Generic
from flaskps.db import db, Session
from datetime import datetime

class Student(Generic):

    def get_entity():
        return Estudiante

    def all(page=1):
        # result = Estudiante.query.paginate(page, Generic.get_registros_per_page())
        result = Estudiante.query
        return result

    # Elimina el estudiante por id
    def delete_by_id(id):
        estudiante = Estudiante.query.filter_by(id=id).first()
        db.session.delete(estudiante)
        db.session.commit()
        return True

    def find_by_id(id):
        estudiante = Estudiante.query.filter_by(id=id).first()
        return estudiante

    def update(entity, id):
        estudiante = Estudiante.query.filter_by(id=id).first()
        estudiante.apellido = entity.apellido
        estudiante.nombre = entity.nombre
        estudiante.fecha_nac = entity.fecha_nac
        estudiante.localidad_id = entity.localidad_id
        estudiante.nivel_id = entity.nivel_id
        estudiante.domicilio = entity.domicilio
        estudiante.genero_id = entity.genero_id
        estudiante.escuela_id = entity.escuela_id
        estudiante.tipo_doc_id = entity.tipo_doc_id
        estudiante.numero = entity.numero
        estudiante.tel = entity.tel
        estudiante.barrio_id = entity.barrio_id
        db.session.commit()

    def search(filter):
        nombre = "%{}%".format(filter["apellido"])
        numero = "%{}%".format(filter["numero"])
        estudiantes = Estudiante.query\
            .filter(Estudiante.apellido.like(nombre)
                    & Estudiante.numero.like(numero)).all()
        return estudiantes

    @classmethod
    def tiene_permiso(cls, username, permiso):
        user = cls.find_by_username(username)
        for rol in user.roles:
            for p in rol.permisos:
                if permiso == p.nombre:
                    return True
        return False

    @classmethod
    def tiene_rol(cls, username, role):
        user = cls.find_by_username(username)
        for rol in user.roles:
            if role == rol.nombre:
                return True
        return False