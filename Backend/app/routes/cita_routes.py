from flask import Blueprint, request, jsonify
from datetime import datetime

from app.controllers.cita_controller import (
    crear_cita,
    obtener_citas_por_alumno,
    obtener_citas_pendientes,
    obtener_citas_culminadas,
    actualizar_estado_cita,
    obtener_cita,
    actualizar_citas_ausentes,
    reprogramar_cita
)

cita_bp = Blueprint('cita', __name__)

@cita_bp.route('/citas', methods=['POST'])
def registrar_cita():
    data = request.get_json()
    return crear_cita(data)

@cita_bp.route('/citas/alumno/<int:id_alumno>', methods=['GET'])
def ver_citas_alumno(id_alumno):
    citas = obtener_citas_por_alumno(id_alumno)
    return jsonify([{
        'id': c.id_cita,
        'motivo': c.motivo,
        'descripcion': c.descripcion,
        'area': c.area,
        'fecha': c.fecha.strftime('%Y-%m-%d'),
        'horario': c.horario,
        'estado': c.estado
    } for c in citas])

@cita_bp.route('/citas/pendientes', methods=['GET'])
def ver_pendientes():
    citas = obtener_citas_pendientes()
    return jsonify([{
        'id': c.id_cita,
        'nombre': c.alumno.nombre,
        'motivo': c.motivo,
        'area': c.area,
        'fecha': c.fecha.strftime('%Y-%m-%d'),
        'horario': c.horario,
        'estado': c.estado
    } for c in citas])

@cita_bp.route('/citas/culminadas', methods=['GET'])
def ver_culminadas():
    citas = obtener_citas_culminadas()
    return jsonify([{
        'id': c.id_cita,
        'nombre': c.alumno.nombre,
        'motivo': c.motivo,
        'area': c.area,
        'fecha': c.fecha.strftime('%Y-%m-%d'),
        'horario': c.horario,
        'estado': c.estado
    } for c in citas])

@cita_bp.route('/citas/<int:id_cita>/estado', methods=['PUT'])
def cambiar_estado(id_cita):
    data = request.get_json()
    return actualizar_estado_cita(id_cita, data.get('estado'))

@cita_bp.route('/citas/<int:id_cita>', methods=['GET'])
def ver_detalle_cita(id_cita):
    c = obtener_cita(id_cita)
    if c:
        return jsonify({
            'id': c.id_cita,
            'nombre': c.alumno.nombre,
            'motivo': c.motivo,
            'descripcion': c.descripcion,
            'area': c.area,
            'fecha': c.fecha.strftime('%Y-%m-%d'),
            'horario': c.horario,
            'estado': c.estado
        })
    return jsonify({'error': 'No encontrada'}), 404

@cita_bp.route('/citas/verificar-ausentes', methods=['PUT'])
def verificar_y_actualizar_ausentes():
    return actualizar_citas_ausentes()

@cita_bp.route('/citas/<int:id_cita>/reprogramar', methods=['PUT'])
def reprogramar(id_cita):
    data = request.get_json()
    try:
        nueva_fecha = datetime.strptime(data.get('fecha'), '%Y-%m-%d').date()
        nuevo_horario = data.get('horario')
        return reprogramar_cita(id_cita, nueva_fecha, nuevo_horario)
    except Exception as e:
        return jsonify({'error': 'Formato de fecha inválido o datos faltantes'}), 400