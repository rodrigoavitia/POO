import mysql.connector
from mysql.connector import Error

class GestorConexion:
    HOST = "localhost"
    DATABASE = "bd_coches"
    USER = "root"
    PASSWORD = ""

    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.HOST,
                database=self.DATABASE,
                user=self.USER,
                password=self.PASSWORD
            )
            if self.conexion.is_connected():
                self.cursor = self.conexion.cursor()
                return True
            return False
        except Error as e:
            return False

    def desconectar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            
    def obtener_conexion(self):
        if self.conectar():
            return self.conexion, self.cursor
        return None, None