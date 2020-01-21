from flaskps.models.entities.estudiante import Estudiante

def to_estudiante(form):
    return Estudiante(form[0], form[1], form[2], form[3], form[4], form[5], form[6], form[7], form[8], form[9], form[10], form[11])