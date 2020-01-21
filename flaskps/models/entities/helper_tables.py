from flaskps.db import db

rol_tiene_permiso = db.Table('rol_tiene_permiso',
                             db.Column("rol_id", db.Integer, db.ForeignKey("rol.id"), primary_key=True),
                             db.Column("permiso_id", db.Integer, db.ForeignKey("permiso.id"), primary_key=True))

usuario_tiene_rol = db.Table("usuario_tiene_rol",
                             db.Column("rol_id", db.Integer, db.ForeignKey("rol.id"), primary_key=True),
                             db.Column("usuario_id", db.Integer, db.ForeignKey("usuario.id"), primary_key=True))

# estudiante_taller = db.Table("estudiante_taller",
#                              db.Column("estudiante_id", db.Integer, db.ForeignKey("estudiante.id"), primary_key=True),
#                              db.Column("ciclo_lectivo_id", db.Integer, db.ForeignKey("ciclo_lectivo.id"), primary_key=True),
#                              db.Column("taller_id", db.Integer, db.ForeignKey("taller.id"), primary_key=True))

# docente_responsable_taller = db.Table("docente_responsable_taller",
#                              db.Column("docente_id", db.Integer, db.ForeignKey("docente.id"), primary_key=True),
#                              db.Column("ciclo_lectivo_id", db.Integer, db.ForeignKey("ciclo_lectivo.id"), primary_key=True),
#                              db.Column("taller_id", db.Integer, db.ForeignKey("taller.id"), primary_key=True))

responsable_estudiante = db.Table("responsable_estudiante",
                             db.Column("responsable_id", db.Integer, db.ForeignKey("responsable.id"), primary_key=True),
                             db.Column("estudiante_id", db.Integer, db.ForeignKey("estudiante.id"), primary_key=True))

ciclo_lectivo_taller = db.Table("ciclo_lectivo_taller",
                             db.Column("taller_id", db.Integer, db.ForeignKey("taller.id"), primary_key=True),
                             db.Column("ciclo_lectivo_id", db.Integer, db.ForeignKey("ciclo_lectivo.id"), primary_key=True))

preceptor_nucleo = db.Table("preceptor_nucleo",
                             db.Column("preceptor_id", db.Integer, db.ForeignKey("preceptor.id"), primary_key=True),
                             db.Column("nucleo_id", db.Integer, db.ForeignKey("nucleo.id"), primary_key=True))

asis_est_taller = db.Table("asis_est_taller",
                             db.Column("estudiante_id", db.Integer, db.ForeignKey("estudiante.id"), primary_key=True),
                             db.Column("ciclo_lectivo_id", db.Integer, db.ForeignKey("ciclo_lectivo.id"), primary_key=True),
                             db.Column("taller_id", db.Integer, db.ForeignKey("taller.id"), primary_key=True))