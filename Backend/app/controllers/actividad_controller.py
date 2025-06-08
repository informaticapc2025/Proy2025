from app.models.actividad import Actividad
from app import db
from datetime import datetime

def crear_actividad(data):
    nueva = Actividad(
        tipo=data.get('tipo'),
        titulo=data.get('titulo'),
        descripcion=data.get('descripcion'),
        fecha_actividad=datetime.strptime(data.get('fecha_actividad'), '%Y-%m-%d'),
        archivo=data.get('archivo'),
        id_usuario=data.get('id_usuario')
    )
    db.session.add(nueva)
    db.session.commit()
    return nueva

def listar_por_usuario(id_usuario):
    return Actividad.query.filter_by(id_usuario=id_usuario).order_by(Actividad.fecha_solicitud.desc()).all()

def listar_todas():
    return Actividad.query.order_by(Actividad.fecha_solicitud.desc()).all()

def cambiar_estado(id_actividad, nuevo_estado):
    actividad = Actividad.query.get(id_actividad)
    if actividad:
        actividad.estado = nuevo_estado
        db.session.commit()
        return actividad
    return None

def listar_aprobadas():
    return Actividad.query.filter_by(estado='Aprobado').order_by(Actividad.fecha_solicitud.desc()).all()

