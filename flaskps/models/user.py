from flaskps.models.entities.usuario import Usuario
from flaskps.models.generic import Generic
from flaskps.db import db, Session
from datetime import datetime
from flaskps.models.rol import RolModel


class User(Generic):

    def get_entity():
        return Usuario

    # Retorna todos los usuarios activos. Si no se especifica pagina devuelve la primera.
    # Retorna objeto Paginator.
    #   Paginator.items -> objetos de la pagina, Paginator.total -> total de objetos encontrados
    def all(page=1, order=None):
        result = None
        if order != None:
            query = Usuario.query.filter_by(activo=True)
            if order['dir'] == 'asc':
                query = query.order_by(Usuario.__dict__[order['column']])
            else:
                query = query.order_by(Usuario.__dict__[order['column']].desc())
            result = query.paginate(page, Generic.get_registros_per_page())
        else:
            result = Usuario.query.filter_by(activo=True).paginate(page, Generic.get_registros_per_page())
        return result

    # Bloquea al usuario por id
    def delete_by_id(id):
        user = Usuario.query.filter_by(id=id).first()
        user.activo = False
        db.session.commit()
        return True

    # Bloquea al usuario por username
    def delete_by_username(username):
        Session.query(Usuario).filter_by(username=username, activo=True).update({Usuario.activo: False})
        return True

    def update(entity, roles, id):
        user = Usuario.query.filter_by(id=id).first()
        user.email = entity.email
        user.password = entity.password
        user.first_name = entity.first_name
        user.last_name = entity.last_name
        user.updated_at = datetime.now()
        user.activo = entity.activo

        user.roles.clear()
        for id_rol in roles:
            rol = RolModel.find_by_id(id_rol)
            user.roles.append(rol)

        if not roles:
            adminRol = RolModel.get_admin()
            user.roles.append(adminRol)

        db.session.commit()

    # Guarda un nuevo usuario
    def save(entity, roles):
        result = Usuario.query.filter_by(username=entity.username, email=entity.email).first()
        if result is None:
            if not roles:
                adminRol = RolModel.get_admin()
                entity.roles.append(adminRol)
            for id_rol in roles:
                rol = RolModel.find_by_id(id_rol)
                entity.roles.append(rol)
            db.session.add(entity)
            db.session.commit()
            return True
        else:
            return False

    # Activa al usuario por username
    def activate_by_username(username):
        Session.query(Usuario).filter_by(username=username, activo=False).update({Usuario.activo: True})
        return True

    # Activa al usuario por id
    def activate_by_id(id):
        user = Usuario.query.filter_by(id=id,activo=False).first()
        user.activo = True
        db.session.commit()
        return True

    def activate_all():
        users = Usuario.query.filter_by(activo=False)
        for user in users:
            user.activo=True
        db.session.commit()
        return True

    def find_by_username(username):
        result = Usuario.query.filter_by(username=username).first()
        return result

    def find_by_id(id):
        usr = Usuario.query.filter_by(id=id, activo=True).first()
        return usr

    def find_by_username_and_pass(username, psw):
        usr = Usuario.query.filter_by(username=username, password=psw, activo=True).first()
        return usr

    def find_by_username_and_email(username, email):
        usr = Usuario.query.filter_by(username=username, activo=True).first()
        if usr is not None:
            return usr
        else:
            usr = Usuario.query.filter_by(email=email, activo=True).first()
            return usr

    def find_blocked(page=1):
        result = Usuario.query.filter_by(activo=False).paginate(page, Generic.get_registros_per_page())
        return result

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
