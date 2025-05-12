from app import db
from datetime import datetime

class Anuncio(db.Model):
    __tablename__ = 'anuncios'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=False)
    imagen = db.Column(db.String(255))  # puede ser una URL o nombre de archivo
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
