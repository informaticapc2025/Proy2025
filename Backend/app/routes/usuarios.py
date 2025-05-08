from flask import Blueprint, jsonify, request
from app.models.usuarios import Usuario
from app import db

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        "id": u.id_usuario,
        "nombre": u.nombre,
        "correo": u.correo,
        "rol": u.rol
    } for u in usuarios])
