from flaskps.models.generic import Generic
from flaskps.models.entities.rol import Rol


class RolModel(Generic):

    def get_entity():
        return Rol

    def get_admin():
        return Rol.query.filter_by(nombre="Administrador").first()