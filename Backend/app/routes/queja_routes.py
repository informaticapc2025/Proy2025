from flask import Blueprint, request, jsonify
from app.controllers.queja_controller import crear_queja, obtener_quejas_por_usuario, obtener_todas_quejas, actualizar_estado_queja

queja_bp = Blueprint('queja', __name__)

@queja_bp.route('/quejas', methods=['POST'])
def registrar_queja():
    data = request.get_json()
    nueva = crear_queja(data)
    return jsonify({'mensaje': 'Queja registrada', 'codigo': nueva.codigo_reporte}), 201

@queja_bp.route('/quejas/usuario/<int:id_usuario>', methods=['GET'])
def listar_quejas_usuario(id_usuario):
    quejas = obtener_quejas_por_usuario(id_usuario)
    return jsonify([{
        'codigo': q.codigo_reporte,
        'asunto': q.asunto,
        'motivo': q.motivo,
        'descripcion': q.descripcion,
        'fecha': q.fecha.strftime('%d/%m/%Y'),
        'estado': q.estado,
        'prueba': q.prueba
    } for q in quejas])

@queja_bp.route('/quejas', methods=['GET'])
def listar_todas_quejas():
    quejas = obtener_todas_quejas()
    return jsonify([{
        'id': q.id_queja,
        'codigo': q.codigo_reporte,
        'asunto': q.asunto,
        'motivo': q.motivo,
        'descripcion': q.descripcion,
        'fecha': q.fecha.strftime('%d/%m/%Y'),
        'estado': q.estado,
        'prueba': q.prueba
    } for q in quejas])

@queja_bp.route('/quejas/<int:id_queja>/estado', methods=['PUT'])
def cambiar_estado_queja(id_queja):
    data = request.get_json()
    nuevo_estado = data.get('estado')
    queja_actualizada = actualizar_estado_queja(id_queja, nuevo_estado)
    if queja_actualizada:
        return jsonify({'mensaje': 'Estado actualizado'}), 200
    return jsonify({'error': 'Queja no encontrada'}), 404
