from flask_login import UserMixin

from app.Services.cursor_pool import CursorPool

class UsuarioModel(UserMixin):
    def __init__(self, id=None,nombre=None, apellido=None, email=None, usuario=None, contrasenia=None):
        self.id = id
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    @staticmethod
    def obtener_usuario(id):
        with CursorPool() as cursor:
            sql = "SELECT * FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id, ))
            fila = cursor.fetchone()
            if fila:
                return UsuarioModel(**fila)
            return None