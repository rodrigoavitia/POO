from conexionBD import Conexiones
from tkinter import messagebox
import io 

class Consultas_reportes:
    
    @staticmethod
    def buscar_reportes(termino="", rol="Todos", fecha_ini="", fecha_fin=""):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            
            if conexion and cursor:
                sql = """
                SELECT 
                    r.fecha,
                    CONCAT(u.nombre, ' ', u.apellido_paterno) as nombre_completo,
                    u.rol as rol_usuario,
                    u.id as matricula_usuario, 
                    v.placa,
                    'A-01' as espacio, 
                    r.hora as entrada,
                    ADDTIME(r.hora, '04:00:00') as salida,
                    r.tipo_evento as reporte_tipo,
                    r.id as id_reporte
                FROM registros r
                JOIN vehiculos v ON r.id_vehiculo = v.id
                JOIN usuarios u ON v.id_usuario = u.id
                WHERE (
                    v.placa LIKE %s OR 
                    u.nombre LIKE %s OR 
                    u.apellido_paterno LIKE %s
                )
                AND u.rol NOT IN ('Sudote', 'Administrador', 'Sudito (Admin)')
                """
                
                t = f"%{termino}%"
                params = [t, t, t]

                if rol != "Todos" and rol != "Tipo de usuario":
                    sql += " AND u.rol = %s"
                    params.append(rol)

                if fecha_ini:
                    sql += " AND r.fecha >= %s"
                    params.append(fecha_ini)
                if fecha_fin:
                    sql += " AND r.fecha <= %s"
                    params.append(fecha_fin)

                sql += " ORDER BY r.fecha DESC, r.hora DESC LIMIT 50"
                
                cursor.execute(sql, tuple(params))
                resultados = cursor.fetchall()
                cursor.close(); conexion.close()
                return resultados
            return []
        except Exception as e:
            print(f"Error reportes: {e}")
            return []

    @staticmethod
    def obtener_detalle(id_reporte):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                sql = """
                SELECT r.imagen_evidencia, r.fecha, r.hora, r.tipo_evento, v.placa, v.modelo, v.color,
                       CONCAT(u.nombre, ' ', u.apellido_paterno) as nombre, u.rol as rol
                FROM registros r
                JOIN vehiculos v ON r.id_vehiculo = v.id
                JOIN usuarios u ON v.id_usuario = u.id
                WHERE r.id = %s
                """
                cursor.execute(sql, (id_reporte,))
                res = cursor.fetchone()
                cursor.close(); conexion.close()
                return res
        except: return None