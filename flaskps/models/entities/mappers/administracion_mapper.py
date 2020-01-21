from flaskps.models.entities.ciclo_lectivo import CicloLectivo


def to_ciclo_lectivo(form):
    return CicloLectivo(form["fecha_ini"],
                        form["fecha_fin"],
                        form["semestre"])
