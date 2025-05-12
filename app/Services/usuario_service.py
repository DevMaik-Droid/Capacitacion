
from app.Models.usuario_model import UsuarioModel
from app.Services.cursor_pool import CursorPool


class UsuarioService():


    def __init__(self):
        self.cursor = CursorPool()

    def obtener_usuario_by_id(self, id):
        with self.cursor as cursor:
            sql = "SELECT * FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id, ))
            return cursor.fetchone()
        
    def crear_usuario(self, usuario : UsuarioModel):
        with self.cursor as cursor:
            sql = "INSERT INTO usuarios (nombre, apellido, email, usuario, contrasenia) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, (usuario.nombre, usuario.apellido, usuario.email, usuario.usuario, usuario.contrasenia))
            return cursor.lastrowid
        
    def obtener_usuario(self, username):
        with self.cursor as cursor:
            sql = "SELECT * FROM usuarios WHERE usuario = %s"
            cursor.execute(sql, (username, ))
            fila = cursor.fetchone()
            if fila:
                return UsuarioModel(**fila)
            return None
