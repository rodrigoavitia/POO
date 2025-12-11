from conexionBD import Conexiones
from tkinter import messagebox
import hashlib # PARA LA ENCRIPTACIÓN

class Consulta_usuarios:
    @staticmethod
    def _encriptar(password):
        """Convierte texto plano a Hash SHA256"""
        if not password: return ""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def login(email, password):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                # 1. Encriptamos la contraseña ingresada para compararla
                pass_hash = Consulta_usuarios._encriptar(password)
                
                # 2. Buscamos coincidencia con la encriptacion en la BD
                sql = "SELECT nombre, rol FROM usuarios WHERE email = %s AND password = %s AND estado = 1"
                cursor.execute(sql, (email, pass_hash))
                
                resultado = cursor.fetchone()
                cursor.close(); conexion.close()
                return resultado
        except: return None

    @staticmethod
    def registrar_persona(nombre, ape_pat, ape_mat, rol, estado, email=None, password=None):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            
            if conexion and cursor:
                estado_int = 1 if estado else 0
                pass_final = Consulta_usuarios._encriptar(password) if password else None
                
                sql = """
                INSERT INTO usuarios 
                (nombre, apellido_paterno, apellido_materno, rol, estado, email, password) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                valores = (nombre, ape_pat, ape_mat, rol, estado_int, email, pass_final)
                
                cursor.execute(sql, valores)
                nuevo_id = cursor.lastrowid
                
                conexion.commit()
                cursor.close(); conexion.close()
                return nuevo_id
        except Exception as e:
            messagebox.showerror("Error BD", f"{e}")
            return None

    @staticmethod
    def actualizar_usuario(uid, nombre, ape_pat, ape_mat, rol, estado, email, password):
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                estado_int = 1 if estado else 0
                
                if password:
                    pass_hash = Consulta_usuarios._encriptar(password)
                    sql = """
                    UPDATE usuarios SET 
                    nombre=%s, apellido_paterno=%s, apellido_materno=%s, rol=%s, estado=%s, email=%s, password=%s 
                    WHERE id=%s
                    """
                    vals = (nombre, ape_pat, ape_mat, rol, estado_int, email, pass_hash, uid)
                else:
                    
                    if password == "":
                         sql = """
                        UPDATE usuarios SET 
                        nombre=%s, apellido_paterno=%s, apellido_materno=%s, rol=%s, estado=%s, email=%s
                        WHERE id=%s
                        """
                         vals = (nombre, ape_pat, ape_mat, rol, estado_int, email, uid)
                    else:
                         pass_hash = Consulta_usuarios._encriptar(password)
                         sql = """
                        UPDATE usuarios SET 
                        nombre=%s, apellido_paterno=%s, apellido_materno=%s, rol=%s, estado=%s, email=%s, password=%s 
                        WHERE id=%s
                        """
                         vals = (nombre, ape_pat, ape_mat, rol, estado_int, email, pass_hash, uid)

                cursor.execute(sql, vals)
                conexion.commit()
                cursor.close(); conexion.close()
                return True
        except Exception as e:
            print(e)
            return False

    # ... (El resto de los métodos obtener_todos, eliminar, contar, etc. se quedan IGUAL) ...
    @staticmethod
    def obtener_todos():
        try:
            mi_conexion = Conexiones()
            conexion, cursor = mi_conexion.conexion_bd()
            if conexion and cursor:
                sql = "SELECT id, nombre, apellido_paterno, apellido_materno, rol, estado FROM usuarios ORDER BY id DESC"
                cursor.execute(sql)
                res = cursor.fetchall()
                cursor.close(); conexion.close()
                return res
        except: return []

    @staticmethod
    def cambiar_estado(uid, nuevo_estado):
        try:
            c = Conexiones(); con, cur = c.conexion_bd()
            if con:
                cur.execute("UPDATE usuarios SET estado = %s WHERE id = %s", (nuevo_estado, uid))
                con.commit(); cur.close(); con.close(); return True
        except: return False

    @staticmethod
    def eliminar_usuario(uid):
        try:
            c = Conexiones(); con, cur = c.conexion_bd()
            if con:
                cur.execute("DELETE FROM usuarios WHERE id = %s", (uid,))
                con.commit(); cur.close(); con.close(); return True
        except: return False
    
    @staticmethod
    def contar_total():
        try:
            c = Conexiones(); con, cur = c.conexion_bd()
            if con:
                cur.execute("SELECT COUNT(*) FROM usuarios")
                r = cur.fetchone()[0]; cur.close(); con.close(); return r
        except: return 0

    @staticmethod
    def contar_por_rol(rol_buscado):
        try:
            c = Conexiones(); con, cur = c.conexion_bd()
            if con:
                cur.execute("SELECT COUNT(*) FROM usuarios WHERE rol LIKE %s", (f"%{rol_buscado}%",))
                r = cur.fetchone()[0]; cur.close(); con.close(); return r
        except: return 0

    @staticmethod
    def contar_activos():
        try:
            c = Conexiones(); con, cur = c.conexion_bd()
            if con:
                cur.execute("SELECT COUNT(*) FROM usuarios WHERE estado=1")
                r = cur.fetchone()[0]; cur.close(); con.close(); return r
        except: return 0