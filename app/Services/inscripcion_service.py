from app.Services.cursor_pool import CursorPool

from app.Models.inscripcion_model import InscripcionModel

class InscripcionService:
    _TABLE_NAME = 'inscripciones'

    def __init__(self):
        self.cursor = CursorPool()

    def listar_inscripciones(self):
        with self.cursor as cursor:
            sql = f"""SELECT i.id, i.fecha, e.nombre as estudiante, c.descripcion as curso
                      FROM {self._TABLE_NAME} i
                      INNER JOIN estudiantes e ON i.estudiante_id = e.id
                      INNER JOIN cursos c ON i.curso_id = c.id"""
            cursor.execute(sql)
            return cursor.fetchall()

    def insertar_inscripcion(self, inscripcion: InscripcionModel):
        with self.cursor as cursor:
            sql = f"INSERT INTO {self._TABLE_NAME} (fecha, estudiante_id, curso_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (inscripcion.fecha, inscripcion.estudiante, inscripcion.curso))
            return cursor.lastrowid

    def actualizar_inscripcion(self, inscripcion: InscripcionModel):
        with self.cursor as cursor:
            sql = f"UPDATE {self._TABLE_NAME} SET fecha = %s, estudiante_id = %s, curso_id = %s WHERE id = %s"
            cursor.execute(sql, (inscripcion.fecha, inscripcion.estudiante, inscripcion.curso, inscripcion.id))
            return inscripcion.id

    def eliminar_inscripcion(self, id: int):
        with self.cursor as cursor:
            sql = f"DELETE FROM {self._TABLE_NAME} WHERE id = %s"
            cursor.execute(sql, (id,))
            return id
        
    def obtener_inscripcion(self, id):
        with self.cursor as cursor:
            sql = f"SELECT * FROM {self._TABLE_NAME} WHERE id = %s"
            cursor.execute(sql, (id,))
            return cursor.fetchone()
