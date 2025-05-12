from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
import threading
class Database:

    load_dotenv()
    __url = urlparse(os.getenv('DATABASE_URL'))
    _DATABASE = __url.path[1:]
    _USERNAME = __url.username
    _PASSWORD = __url.password
    _HOST = __url.hostname
    _PORT = __url.port
    _pool = None
    _minconn = 1
    _maxconn = 5
    
    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                                                    cls._minconn,
                                                    cls._maxconn,
                                                    host=cls._HOST,
                                                    port=cls._PORT,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    database=cls._DATABASE,
                                                    cursor_factory=RealDictCursor)
                print("Conectado a la base de datos")
                
            except Exception as e:
                print(f"Error al establecer la conexion con la base de datos: {e}")
                raise e
        return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()