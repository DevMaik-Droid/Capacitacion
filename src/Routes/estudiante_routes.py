from flask import Blueprint, render_template, request, url_for, redirect

from app.Models.estudiante_model import EstudianteModel
from app.Services.estudiante_service import EstudianteService


estudiante_bp = Blueprint('estudiante', __name__, url_prefix='/estudiante')

@estudiante_bp.route('/listar')
def listar():
    estudiante_service = EstudianteService()
    estudiantes = estudiante_service.listar_estudiantes()  # Cambiado a plural
    return render_template('estudiante/estudiantes.html', estudiantes=estudiantes)


@estudiante_bp.route('/crear', methods=['GET', 'POST'])
def crear():

    if request.method == 'GET':
        return render_template('estudiante/form_estudiante.html')

    
    estudiante = EstudianteModel(
            nombre=request.form['txt_nombre'],
            apellido=request.form['txt_apellido'],
            fecha_nacimiento=request.form['txt_fecha_nacimiento']
        )
    estudianteService = EstudianteService()
    estudianteService.insertar_estudiante(estudiante)
    return redirect(url_for('estudiante.listar'))    
 


@estudiante_bp.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'GET':
        estudianteService = EstudianteService()
        estudiante = estudianteService.obtener_estudiante(id)
        return render_template('estudiante/form_estudiante.html', estudiante=estudiante)
    estudiante = EstudianteModel(
        id=id,
        nombre=request.form['txt_nombre'],
        apellido=request.form['txt_apellido'],
        fecha_nacimiento=request.form['txt_fecha_nacimiento']
    )
    estudianteService = EstudianteService()
    estudianteService.actualizar_estudiante(estudiante)
    return redirect(url_for('estudiante.listar'))

@estudiante_bp.route('/eliminar/<id>')
def eliminar(id):
    estudianteService = EstudianteService()
    estudianteService.eliminar_estudiante(id)
    return redirect(url_for('estudiante.listar'))

