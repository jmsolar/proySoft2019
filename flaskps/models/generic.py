from flaskps.db import db
from flaskps.models.entities.configuracion import Config

class Generic(object):

    def get_entity():
        return None

    def get_registros_per_page():
        config = Config.query.first()
        return config.registros_por_pagina

    # Retorna todos los objetos. Si no se especifica paginado devuelve todos.
    # Al especificar paginado retorna objeto Paginator.
    #   Paginator.items -> objetos de la pagina, Paginator.total -> total de objetos encontrados
    @classmethod
    def all(cls, order=None):
        entity = cls.get_entity()
        result = entity.query.all()
        return result

    @classmethod
    def all_by_page(cls, page=1, order=None):
        entity = cls.get_entity()
        result = None
        if order is not None:
            query = entity.query
            if order['dir'] == 'asc':
                query = query.order_by(entity.__dict__[order['column']])
            else:
                query = query.order_by(entity.__dict__[order['column']].desc())
            result = query.paginate(page, cls.get_registros_per_page())
        else:
            result = entity.query.paginate(page, cls.get_registros_per_page())
        return result

    # Retorna un objeto buscado por id
    @classmethod
    def find_by_id(cls, id):
        entity = cls.get_entity()
        result = entity.query.filter_by(id=id).first()
        return result

    # Guarda un objeto
    @classmethod
    def save(cls, entity):
        db.session.add(entity)
        db.session.commit()
        return True

    # Elimina un objeto físicamente
    @classmethod
    def delete_by_id(cls, id):
        entity = cls.get_entity()
        t = entity.query.filter_by(id=id).first()
        db.session.delete(t)
        db.session.commit()
        return True
