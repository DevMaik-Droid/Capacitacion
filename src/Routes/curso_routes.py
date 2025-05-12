from flask import Blueprint, render_template, request, url_for, redirect

from src.Models.curso_model import CursoModel
from src.Services.curso_service import CursoService

curso_bp = Blueprint('curso',__name__,url_prefix='/curso')
curso_service = CursoService() #Variable global

@curso_bp.route('/listar', methods=['GET', 'POST'])
def listar():
    return render_template('cursos/cursos.html', cursos=curso_service.listar_cursos())
    
@curso_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'GET':
        return render_template('cursos/form_curso.html')
    
    curso = CursoModel(
        descripccion=request.form['txt_descripcion'], horas=request.form['txt_horas'])
    curso_service.insertar_curso(curso)
    return redirect(url_for('curso.listar'))

@curso_bp.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'GET':
        return render_template('cursos/form_curso.html', curso=curso_service.obtener_curso(id))
    
    curso = CursoModel(id=id,descripccion=request.form['txt_descripcion'], horas=request.form['txt_horas'])
    curso_service.actualizar_curso(curso)
    return redirect(url_for('curso.listar'))

@curso_bp.route('/eliminar/<id>')
def eliminar(id):
    curso_service.eliminar_curso(id)
    return redirect(url_for('curso.listar'))
