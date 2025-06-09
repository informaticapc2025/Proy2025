from flask import Blueprint, request, jsonify
from app.controllers.anuncio_controller import crear_anuncio, obtener_anuncios
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
anuncio_bp = Blueprint('anuncio', __name__)

from flask import request

@anuncio_bp.route('/anuncios', methods=['GET'])
def listar_anuncios():
    anuncios = obtener_anuncios()
    return jsonify([
        {
            'id': a.id_publicacion,
            'descripcion': a.descripcion,
            'imagen': f"{request.host_url}uploads/{a.imagen}" if a.imagen else None,
            'fecha_publicacion': a.fecha_publicacion.isoformat()
        } for a in anuncios
    ])



@anuncio_bp.route('/anuncios', methods=['POST'])
def publicar_anuncio():
    descripcion = request.form.get('descripcion')
    id_usuario = request.form.get('id_usuario')
    imagen = None

    if 'imagen' in request.files:
        imagen_file = request.files['imagen']
        if imagen_file.filename != '':
            from werkzeug.utils import secure_filename
            filename = secure_filename(imagen_file.filename)
            imagen = filename
            imagen_file.save(os.path.join(UPLOAD_FOLDER, filename))
            print("Guardando imagen en:", os.path.join(UPLOAD_FOLDER, filename))


    nuevo = crear_anuncio({
        'descripcion': descripcion,
        'imagen': imagen,
        'id_usuario': id_usuario
    })

    return jsonify({'mensaje': 'Anuncio publicado', 'id': nuevo.id_publicacion}), 201


@anuncio_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

