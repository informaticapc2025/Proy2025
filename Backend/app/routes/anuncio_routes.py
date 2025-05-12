from flask import Blueprint, request, jsonify
from app.controllers import anuncio_controller

anuncio_bp = Blueprint("anuncio", __name__)

@anuncio_bp.route("/anuncios", methods=["GET"])
def listar_anuncios():
    anuncios = anuncio_controller.obtener_anuncios()
    return jsonify([
        {
            "id": a.id,
            "descripcion": a.descripcion,
            "imagen": a.imagen,
            "fecha_creacion": a.fecha_creacion.isoformat()
        } for a in anuncios
    ])

@anuncio_bp.route("/anuncios", methods=["POST"])
def crear_anuncio():
    data = request.get_json()
    anuncio = anuncio_controller.crear_anuncio(data)
    return jsonify({"id": anuncio.id}), 201
