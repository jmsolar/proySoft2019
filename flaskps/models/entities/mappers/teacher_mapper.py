from flaskps.models.entities.docente import Docente

def to_docente(form):
	return Docente(form.get("apellido"),
		form.get("nombre"),
		form.get("fecha_nac"),
		form.get("localidad"),
		form.get("domicilio"),
		form.get("genero"),
		form.get("tipo_doc"),
		form.get("numero"),
		form.get("tel"))
