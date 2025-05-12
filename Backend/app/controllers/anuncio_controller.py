from app.models.anuncio import Anuncio
from app import db

def crear_anuncio(data):
    nuevo = Anuncio(
        descripcion=data.get("descripcion"),
        imagen=data.get("imagen")
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def obtener_anuncios():
    return Anuncio.query.order_by(Anuncio.fecha_creacion.desc()).all()
