from flaskps.models.entities.instrumento import Instrumento

def to_instrumento(form):
    return Instrumento(form[0],
                   form[1], form[2])