from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.Models.usuario_model import UsuarioModel
from app.Services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')
usuario_service = UsuarioService()

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('usuario/login.html')
    
    user : UsuarioModel = usuario_service.obtener_usuario(request.form['txt_usuario'])
    if user and check_password_hash(user.contrasenia, request.form['txt_contrasenia']):
        login_user(user)
        return redirect(url_for('index'))

    return redirect(url_for('usuario.login'))

@usuario_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template('usuario/form_usuario.html')
    
    password_hash = generate_password_hash(request.form['txt_contrasenia'])
    usuario = UsuarioModel(
        usuario=request.form['txt_usuario'],
        contrasenia=password_hash,
        nombre=request.form['txt_nombre'],
        apellido=request.form['txt_apellido'],
        email=request.form['txt_email']
    )
    usuario_service.crear_usuario(usuario)
    return redirect(url_for('usuario.login'))

@usuario_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuario.login'))