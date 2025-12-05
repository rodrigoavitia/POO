import mysql.connector

class ConexionBD:
    """Clase para gestionar la conexión a la base de datos."""
    
    @staticmethod
    def conectar():
        try:
            # **¡IMPORTANTE!** Reemplaza esto con tus datos reales de conexión
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bd_coches" 
            )
            return conexion
        except Exception as e:
            # En una aplicación real, se debería manejar este error mejor
            print(f"Error al conectar a la BD: {e}") 
            return None