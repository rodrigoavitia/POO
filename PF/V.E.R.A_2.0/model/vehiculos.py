from conexionBD import Conexiones
from tkinter import messagebox

class Consultas_vehiculos:
    @staticmethod
    def buscar_propietario(termino):
        """Busca usuarios para el registro, excluyendo administradores."""
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            
            if conexion and cursor:
                sql = """
                SELECT id, nombre, apellido_paterno, apellido_materno, rol 
                FROM usuarios 
                WHERE (nombre LIKE %s OR apellido_paterno LIKE %s)
                AND rol NOT IN ('Sudote', 'Administrador', 'Sudito (Admin)')
                LIMIT 10
                """
                param = f"%{termino}%"
                cursor.execute(sql, (param, param))
                res = cursor.fetchall()
                cursor.close(); conexion.close()
                return res
        except Exception as e:
            print(f"Error buscador: {e}")
            return []
    
    @staticmethod
    def buscar_usuarios_like(termino):
        return Consultas_vehiculos.buscar_propietario(termino)

    @staticmethod
    def registrar_vehiculo(marca, modelo, color, placa, anio, id_usuario):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                sql = "INSERT INTO vehiculos (marca, modelo, color, placa, anio, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (marca, modelo, color, placa, anio, id_usuario))
                conexion.commit()
                cursor.close(); conexion.close()
                return True
        except Exception as e:
            if "Duplicate" in str(e):
                messagebox.showerror("Error", f"La placa {placa} ya existe.")
            else:
                messagebox.showerror("Error BD", f"No se pudo registrar: {e}")
            return False

    @staticmethod
    def verificar_placa_autorizada(placa):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                sql = "SELECT 1 FROM vehiculos v JOIN usuarios u ON v.id_usuario = u.id WHERE v.placa = %s AND u.estado = 1"
                cursor.execute(sql, (placa,))
                res = cursor.fetchone()
                cursor.close(); conexion.close()
                return res is not None
        except: return False

    @staticmethod
    def obtener_todos_detallado():
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                sql = """
                SELECT v.id, v.placa, v.marca, v.modelo, 
                       CONCAT(u.nombre, ' ', u.apellido_paterno) as dueno
                FROM vehiculos v
                JOIN usuarios u ON v.id_usuario = u.id
                ORDER BY v.id DESC
                """
                cursor.execute(sql)
                datos = cursor.fetchall()
                cursor.close(); conexion.close()
                return datos
        except Exception as e:
            print(f"Error obteniendo vehículos: {e}")
            return []

    @staticmethod
    def eliminar_vehiculo(id_vehiculo):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                sql = "DELETE FROM vehiculos WHERE id = %s"
                cursor.execute(sql, (id_vehiculo,))
                conexion.commit()
                cursor.close(); conexion.close()
                return True
        except Exception as e:
            print(f"Error eliminando vehículo: {e}")
            return False