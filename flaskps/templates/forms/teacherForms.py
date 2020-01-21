from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields import DateField
from wtforms.fields import SelectField
from wtforms.fields import IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class TeacherForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired("Debe Ingresar un Nombre Valido")])
	apellido = StringField('Apellido', validators=[DataRequired("Debe Ingresar un Apellido Valido")])
	fecha_nac = DateField('Fecha nacimiento', validators=[DataRequired("Debe Ingresar una Fecha Valida")])
	genero = SelectField('Genero', choices[])
	localidad = SelectField('Localidad', choices[])
	domicilio = StringField('Domicilio', validators=[DataRequired("Debe Ingresar un Domicilio")])
	tipo_doc = SelectField('Tipo de Documento', choices[])
	numero = IntegerField('Numero de Documento', validators=[DataRequired("Debe Ingresar un Numero Valido"),length(max=8)])
	tel = IntegerField('Ingresa un número telefónico',validators=[DataRequired("Debe Ingresar un Telefono Valido"),length(max=10)])
	aceptar = SubmitField('Aceptar')
		