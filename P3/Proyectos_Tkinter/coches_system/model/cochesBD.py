from ConexionBD import *

class Autos:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "INSERT INTO autos (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s, %s, %s, %s, %s, %s)"
        datos = (marca, color, modelo, velocidad, caballaje, plazas)
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar auto: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()
    
    @staticmethod
    def consultar():
        conexion = ConexionBD.conectar()
        if not conexion: return []
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas FROM autos"
        cursor = conexion.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar autos: {e}"); return []
        finally:
            cursor.close(); conexion.close()

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id_auto):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "UPDATE autos SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s"
        datos = (marca, color, modelo, velocidad, caballaje, plazas, id_auto)
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar auto: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()

    @staticmethod
    def eliminar(id_auto):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "DELETE FROM autos WHERE id = %s"
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, (id_auto,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar auto: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()

# --- Camionetas ---
class Camionetas:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar camioneta: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()
    
    @staticmethod
    def consultar():
        conexion = ConexionBD.conectar()
        if not conexion: return []
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada FROM camionetas"
        cursor = conexion.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar camionetas: {e}"); return []
        finally:
            cursor.close(); conexion.close()

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id=%s"
        datos = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta)
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar camioneta: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()

    @staticmethod
    def eliminar(id_camioneta):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "DELETE FROM camionetas WHERE id = %s"
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, (id_camioneta,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar camioneta: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()

# --- Camiones ---
class Camiones:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga)
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar camión: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()
    
    @staticmethod
    def consultar():
        conexion = ConexionBD.conectar()
        if not conexion: return []
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga FROM camiones"
        cursor = conexion.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar camiones: {e}"); return []
        finally:
            cursor.close(); conexion.close()

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga, id_camion):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadcarga=%s WHERE id=%s"
        datos = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga, id_camion)
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar camión: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()

    @staticmethod
    def eliminar(id_camion):
        conexion = ConexionBD.conectar()
        if not conexion: return False
        sql = "DELETE FROM camiones WHERE id = %s"
        cursor = conexion.cursor()
        try:
            cursor.execute(sql, (id_camion,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar camión: {e}"); conexion.rollback(); return False
        finally:
            cursor.close(); conexion.close()