from flaskps.models.entities.usuario import Usuario

def to_usuario(form):
    return Usuario(form.get("email"),
                   form.get("username"),
                   form.get("password"),
                   form.get("first_name"),
                   form.get("last_name"))
