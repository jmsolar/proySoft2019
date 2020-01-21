from flaskps.models.generic import Generic
from flaskps.db import db, Session
from datetime import datetime
from flaskps.models.entities.docente import Docente


class Teacher(Generic):

    def getEntity():
        return Docente

    def all(page=1):
        result = Docente.query.paginate(page, Generic.get_registros_per_page())
        return result

    def save(entity):
        result = Docente.query.filter_by(numero=entity.numero).first()
        if result is None:
            db.session.add(entity)
            db.session.commit()
            return True
        else:
            return False

    def update(entity, id):
        docente = Docente.query.filter_by(id=id).first()
        docente.nombre = entity.nombre
        docente.apellido = entity.apellido
        docente.fecha_nac = entity.fecha_nac
        docente.localidad_id = entity.localidad_id
        docente.domicilio = entity.domicilio
        docente.genero_id = entity.genero_id
        docente.tipo_doc_id = entity.tipo_doc_id
        docente.numero = entity.numero
        docente.tel = entity.tel
        db.session.commit()

    def find_by_id(id):
        doc = Docente.query.filter_by(id=id).first()
        return doc

    def delete_by_id(id):
        doc = Docente.query.filter_by(id=id).first()
        db.session.delete(doc)
        db.session.commit()
        return True

    def search(filter):
        nombre = "%{}%".format(filter["apellido"])
        numero = "%{}%".format(filter["numero"])
        docente = Docente.query \
            .filter(Docente.apellido.like(nombre)
                    & Docente.numero.like(numero)).all()
        return docente
