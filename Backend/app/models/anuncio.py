from app import db
from datetime import datetime

class Publicacion(db.Model):
    __tablename__ = 'publicaciones'

    id_publicacion = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=False)
    imagen = db.Column(db.String(255))  # opcional
    fecha_publicacion = db.Column(db.DateTime, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
