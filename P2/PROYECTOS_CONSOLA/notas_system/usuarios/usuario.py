from conexionBD import *
import datetime

class Usuario():
    def registrar(nom, ape, mail, cont):
        try:
            fecha=datetime.datetime.now()
            cursor.execute("INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)", (nom, ape, mail, cont, fecha))
            conexion.commit()
            return True
        except:
            return False
        
    def inicio_sesion(mail, cont):
        try:
            cursor.execute("SELECT * FROM usuarios WHERE email=%s and password=%s", (mail, cont))
            return cursor.fetchone()
        except:
            return []


    


        

