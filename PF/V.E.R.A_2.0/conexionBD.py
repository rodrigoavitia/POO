import mysql.connector
from tkinter import messagebox

class Conexiones:
    def conexion_bd(self):
        try:
            # Aumentamos el timeout para que espere y siga intenando la conexion despues de 60 segundos se rinde
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bd_estacionamiento",
                autocommit=True,
                connect_timeout=60    
            )

            if conexion.is_connected():
                cursor = conexion.cursor(buffered=True)
                return conexion, cursor
            else:
                return None, None
                
        except mysql.connector.Error as e:
            print(f"Error Crítico MySQL: {e}")
            if e.errno == 2006 or e.errno == 2013:
                try:
                    print("Reconectando...")
                    conexion.reconnect(attempts=3, delay=2)
                    return conexion, conexion.cursor(buffered=True)
                except:
                    return None, None
            return None, None