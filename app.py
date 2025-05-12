from flask import Flask, render_template
from flask_login import LoginManager, login_required
from app.Models.usuario_model import UsuarioModel
from app.Routes.usuario_routes import usuario_bp
from app.Routes.curso_routes import curso_bp
from app.Routes.estudiante_routes import estudiante_bp
from app.Routes.inscripcion_routes import inscripcion_bp

def create_app():
    app = Flask(__name__, template_folder="app/templates")
    app.secret_key = 'codigo secreto'
    #Configurar Flask_login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'usuario.login'

    @login_manager.user_loader
    def load_user(user_id):
        return UsuarioModel.obtener_usuario(user_id)

    # Registrar blueprints
    app.register_blueprint(usuario_bp)
    app.register_blueprint(curso_bp)
    app.register_blueprint(estudiante_bp)
    app.register_blueprint(inscripcion_bp)
    
    # Rutas básicas
    @app.route('/')
    @login_required
    def index():
        return render_template('index.html')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)