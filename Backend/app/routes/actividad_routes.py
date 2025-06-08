from flask import Blueprint, request, jsonify
from app.controllers.actividad_controller import crear_actividad, listar_por_usuario, listar_todas, cambiar_estado, listar_aprobadas

actividad_bp = Blueprint('actividad', __name__)

@actividad_bp.route('/actividades', methods=['POST'])
def registrar():
    data = request.get_json()
    actividad = crear_actividad(data)
    return jsonify({'mensaje': 'Solicitud registrada', 'id': actividad.id_actividad}), 201

@actividad_bp.route('/actividades/usuario/<int:id_usuario>', methods=['GET'])
def ver_por_usuario(id_usuario):
    actividades = listar_por_usuario(id_usuario)
    return jsonify([{
        'id': a.id_actividad,
        'tipo': a.tipo,
        'titulo': a.titulo,
        'descripcion': a.descripcion,
        'fecha_actividad': a.fecha_actividad.strftime('%d/%m/%Y'),
        'fecha_solicitud': a.fecha_solicitud.strftime('%d/%m/%Y'),
        'estado': a.estado,
        'archivo': a.archivo
    } for a in actividades])

@actividad_bp.route('/actividades/admin', methods=['GET'])
def ver_todas():
    actividades = listar_todas()
    return jsonify([{
        'id': a.id_actividad,
        'usuario': a.id_usuario,
        'tipo': a.tipo,
        'titulo': a.titulo,
        'descripcion': a.descripcion,
        'fecha_actividad': a.fecha_actividad.strftime('%d/%m/%Y'),
        'fecha_solicitud': a.fecha_solicitud.strftime('%d/%m/%Y'),
        'estado': a.estado,
        'archivo': a.archivo
    } for a in actividades])

@actividad_bp.route('/actividades/<int:id_actividad>/estado', methods=['PUT'])
def actualizar_estado(id_actividad):
    data = request.get_json()
    nueva = cambiar_estado(id_actividad, data.get('estado'))
    if nueva:
        return jsonify({'mensaje': f'Estado cambiado a {nueva.estado}'})
    return jsonify({'mensaje': 'Actividad no encontrada'}), 404

@actividad_bp.route('/actividades/aprobadas', methods=['GET'])
def ver_aprobadas():
    actividades = listar_aprobadas()
    return jsonify([{
        'id': a.id_actividad,
        'titulo': a.titulo,
        'descripcion': a.descripcion,
        'fecha_actividad': a.fecha_actividad.strftime('%d/%m/%Y'),
    } for a in actividades])
