from flask import Blueprint, request, jsonify
from app.controllers.reconocimiento_controller import crear_reconocimiento

reconocimiento_bp = Blueprint("reconocimiento", __name__)

@reconocimiento_bp.route("/reconocimientos", methods=["POST"])
def crear():
    data = request.json
    reconocimiento = crear_reconocimiento(data)
    return jsonify({
        "id": reconocimiento.id_reconocimiento,
        "mensaje": "Reconocimiento creado correctamente"
    }), 201
