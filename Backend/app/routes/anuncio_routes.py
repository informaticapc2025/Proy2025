from flask import Blueprint, request, jsonify
from app.controllers.anuncio_controller import crear_anuncio, obtener_anuncios

anuncio_bp = Blueprint('anuncio', __name__)

@anuncio_bp.route('/anuncios', methods=['GET'])
def listar_anuncios():
    anuncios = obtener_anuncios()
    return jsonify([
        {
            'id': a.id_publicacion,
            'descripcion': a.descripcion,
            'imagen': a.imagen,
            'fecha_publicacion': a.fecha_publicacion.strftime('%d/%m/%Y %H:%M')
        } for a in anuncios
    ])


@anuncio_bp.route('/anuncios', methods=['POST'])
def publicar_anuncio():
    data = request.get_json()
    nuevo = crear_anuncio(data)
    return jsonify({'mensaje': 'Anuncio publicado', 'id': nuevo.id_publicacion}), 201
    