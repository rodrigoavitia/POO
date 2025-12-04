import mysql.connector
from mysql.connector import Error
from ConexionBD import GestorConexion 

class VehiculoDB:
    def __init__(self):
        self.gestor_conexion = GestorConexion()
        
    def ejecutar_consulta(self, sql, parametros=None, es_select=False):
        conexion, cursor = self.gestor_conexion.obtener_conexion()
        resultado = None
        
        if conexion and cursor:
            try:
                cursor.execute(sql, parametros or ())
                if es_select:
                    resultado = cursor.fetchall()
                else:
                    conexion.commit()
                    resultado = cursor.rowcount
            except Error as e:
                resultado = f"Error en la consulta: {e}"
            finally:
                self.gestor_conexion.desconectar()
        else:
             resultado = "Error: No se pudo conectar a la base de datos."
        return resultado

    # CRUD AUTOS
    def insertar_auto(self, marca, color, modelo, velocidad, caballaje, plazas):
        sql = "INSERT INTO autos (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s, %s, %s, %s, %s, %s)"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int) and filas_afectadas > 0:
            return "Auto insertado con éxito."
        return filas_afectadas
        
    def consultar_autos(self):
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas FROM autos"
        registros = self.ejecutar_consulta(sql, es_select=True)
        if isinstance(registros, str) and registros.startswith("Error"):
            return []
        return registros

    def cambiar_auto(self, id_auto, marca, color, modelo, velocidad, caballaje, plazas):
        sql = "UPDATE autos SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas, id_auto)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int):
            if filas_afectadas > 0:
                return "Auto actualizado con éxito."
            else:
                return "ID no encontrado o no se realizaron cambios."
        return filas_afectadas

    def borrar_auto(self, id_auto):
        sql = "DELETE FROM autos WHERE id=%s"
        parametros = (id_auto,)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int):
            if filas_afectadas > 0:
                return "Auto eliminado con éxito."
            else:
                return "ID no encontrado."
        return filas_afectadas

    # CRUD CAMIONETAS
    def insertar_camioneta(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        sql = "INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int) and filas_afectadas > 0:
            return "Camioneta insertada con éxito."
        return filas_afectadas

    def consultar_camionetas(self):
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada FROM camionetas"
        registros = self.ejecutar_consulta(sql, es_select=True)
        if isinstance(registros, str) and registros.startswith("Error"):
            return []
        return registros

    def cambiar_camioneta(self, id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        sql = "UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id=%s"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int):
            if filas_afectadas > 0:
                return "Camioneta actualizada con éxito."
            else:
                return "ID no encontrado o no se realizaron cambios."
        return filas_afectadas

    def borrar_camioneta(self, id_camioneta):
        sql = "DELETE FROM camionetas WHERE id=%s"
        parametros = (id_camioneta,)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int):
            if filas_afectadas > 0:
                return "Camioneta eliminada con éxito."
            else:
                return "ID no encontrado."
        return filas_afectadas

    # CRUD CAMIONES
    def insertar_camion(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        sql = "INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int) and filas_afectadas > 0:
            return "Camión insertado con éxito."
        return filas_afectadas

    def consultar_camiones(self):
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga FROM camiones"
        registros = self.ejecutar_consulta(sql, es_select=True)
        if isinstance(registros, str) and registros.startswith("Error"):
            return []
        return registros

    def cambiar_camion(self, id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        sql = "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadcarga=%s WHERE id=%s"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga, id_camion)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int):
            if filas_afectadas > 0:
                return "Camión actualizado con éxito."
            else:
                return "ID no encontrado o no se realizaron cambios."
        return filas_afectadas

    def borrar_camion(self, id_camion):
        sql = "DELETE FROM camiones WHERE id=%s"
        parametros = (id_camion,)
        filas_afectadas = self.ejecutar_consulta(sql, parametros)
        if isinstance(filas_afectadas, int):
            if filas_afectadas > 0:
                return "Camión eliminado con éxito."
            else:
                return "ID no encontrado."
        return filas_afectadas