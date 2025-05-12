from app.Models.curso_model import CursoModel
from app.Services.cursor_pool import CursorPool

class CursoService:


    def __init__(self):
        self.cursor = CursorPool()

    def listar_cursos(self):
        with self.cursor as cursor:
            sql = "SELECT * FROM cursos"            
            cursor.execute(sql)
            return cursor.fetchall()
    
    def insertar_curso(self, curso : CursoModel):
        with self.cursor as cursor:
            sql = "INSERT INTO cursos (descripcion, horas) VALUES (%s,%s)"
            cursor.execute(sql,(curso.descripccion,curso.horas))
            return cursor.lastrowid
    
    def actualizar_curso(self, curso : CursoModel):
        with self.cursor as cursor:
            sql = "UPDATE cursos SET descripcion = %s, horas = %s WHERE id = %s"
            cursor.execute(sql, (curso.descripccion, curso.horas, curso.id))
            return cursor.rowcount

    def obtener_curso(self, id):
        with self.cursor as cursor:
            sql = "SELECT * FROM cursos WHERE id = %s"
            cursor.execute(sql, (id, ))
            return cursor.fetchone()
    
    def eliminar_curso(self, id):
        with self.cursor as cursor:
            sql = "DELETE FROM cursos WHERE id = ?"
            cursor.execute(sql, (id,))
            return cursor.rowcount
