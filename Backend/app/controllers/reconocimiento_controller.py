from datetime import datetime
from app import db
from app.models.reconocimiento import Reconocimiento

def crear_reconocimiento(data):
    nuevo = Reconocimiento(
        id_alumno=data.get("id_alumno"),
        descripcion=data.get("descripcion"),
        fecha_reconocimiento=datetime.now(),
        id_usuario=data.get("id_usuario")  # el admin que crea el reconocimiento
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo
