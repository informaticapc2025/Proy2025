from app import db  


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    fecha_cumpleaños = db.Column(db.Date)
    codigo_alumno = db.Column(db.String(20), unique=True)

