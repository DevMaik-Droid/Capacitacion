from flask import Blueprint, render_template, request, redirect, url_for

from app.Models.inscripcion_model import InscripcionModel
from app.Services.curso_service import CursoService
from app.Services.estudiante_service import EstudianteService
from app.Services.inscripcion_service import InscripcionService

inscripcion_bp = Blueprint('inscripcion', __name__, url_prefix='/inscripcion')

@inscripcion_bp.route('/listar', methods=['GET'])
def listar():
    inscripcion_service= InscripcionService()
    inscripciones = inscripcion_service.listar_inscripciones()
    print(inscripciones)
    return render_template('inscripcion/inscripciones.html', inscripciones=inscripciones)

@inscripcion_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    inscripcion_service = InscripcionService()

    if request.method == 'POST':
        fecha = request.form.get('txt_fecha')
        estudiante_id = request.form.get('txt_estudiante_id')
        curso_id = request.form.get('txt_curso_id')

        inscripcion = InscripcionModel(fecha=fecha, estudiante=estudiante_id, curso=curso_id)
        inscripcion_service.insertar_inscripcion(inscripcion)

        return redirect(url_for('inscripcion.listar'))

    estudiantes = EstudianteService().listar_estudiantes()
    cursos = CursoService().listar_cursos()

    return render_template('inscripcion/form_inscripcion.html', estudiantes=estudiantes, cursos=cursos)

@inscripcion_bp.route('/editar/<id>',methods=['GET', 'POST'])
def editar(id):

    if request.method == 'GET':
        inscripciones = InscripcionService().obtener_inscripcion(id)
        estudiantes = EstudianteService().listar_estudiantes()
        cursos = CursoService().listar_cursos()
        
        return render_template('inscripcion/form_inscripcion.html', inscripcion=inscripciones, cursos=cursos, estudiantes=estudiantes)
    
    if request.method == 'POST':
        fecha = request.form.get('txt_fecha')
        estudiante_id = request.form.get('txt_estudiante_id')
        curso_id = request.form.get('txt_curso_id')

        inscripcion = InscripcionModel(id=id, fecha=fecha, estudiante=estudiante_id, curso=curso_id)
        InscripcionService().actualizar_inscripcion(inscripcion)

        return redirect(url_for('inscripcion.listar'))

@inscripcion_bp.route('/eliminar/<id>')
def eliminar(id):
    InscripcionService().eliminar_inscripcion(id)
    return redirect(url_for('inscripcion.listar'))