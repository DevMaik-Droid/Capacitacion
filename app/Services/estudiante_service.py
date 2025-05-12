from app.Models.estudiante_model import EstudianteModel
from app.Services.cursor_pool import CursorPool


class EstudianteService:
    def __init__(self):
        self.cursor = CursorPool()

    def listar_estudiantes(self):
        with self.cursor as cursor:
            sql = "SELECT * FROM estudiantes"
            cursor.execute(sql)
            return cursor.fetchall()

    def insertar_estudiante(self, estudiante: EstudianteModel):
        with self.cursor as cursor:
            sql = "INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento) VALUES (%s, %s, %s)"
            cursor.execute(sql, (estudiante.nombre, estudiante.apellido, estudiante.fecha_nacimiento))
            return cursor.lastrowid

    def obtener_estudiante(self, id):
        with self.cursor as cursor:
            sql = "SELECT * FROM estudiantes WHERE id = %s"
            cursor.execute(sql, (id,))
            return cursor.fetchone()

    def actualizar_estudiante(self, estudiante: EstudianteModel):
        with self.cursor as cursor:
            sql = "UPDATE estudiantes SET nombre = %s, apellido = %s, fecha_nacimiento = %s WHERE id = %s"
            cursor.execute(
                sql, (estudiante.nombre, estudiante.apellido, estudiante.fecha_nacimiento, estudiante.id)
            )
            return estudiante.id

    def eliminar_estudiante(self, id):
        with self.cursor as cursor:
            sql = "DELETE FROM estudiantes WHERE id = %s"
            cursor.execute(sql, (id,))
            return cursor.rowcount

