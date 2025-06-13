from app.models.actividad import Actividad
from app import db
from datetime import datetime
from flask import request
from app.models.actividad import Actividad
from app import db
from datetime import datetime
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))

def crear_actividad_con_archivo(aprobado_por_admin=False):
    tipo = request.form.get('tipo')
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    fecha_actividad = datetime.strptime(request.form.get('fecha_actividad'), '%Y-%m-%d')
    id_usuario = request.form.get('id_usuario')
    archivo = None

    # Guardar archivo si lo hay
    if 'archivo' in request.files:
        archivo_file = request.files['archivo']
        if archivo_file.filename != '':
            filename = secure_filename(archivo_file.filename)
            archivo_file.save(os.path.join(UPLOAD_FOLDER, filename))
            archivo = filename

    nueva = Actividad(
        tipo=tipo,
        titulo=titulo,
        descripcion=descripcion,
        fecha_actividad=fecha_actividad,
        archivo=archivo,
        id_usuario=id_usuario,
        estado='Aprobado' if aprobado_por_admin else 'Pendiente'
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

