"""
1ER DICIEMBRE
    1)Implementacion de MVC
    2)POO
    3)INTERFACES:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar autos()

    Productos Entregables:
        ++Estructura del proyecto basado en MVC
        ++Modulo principal "main"
        ++Interacción con las interfaces
        ++ Nombre del Commit "commit_01_12_25"

"""
from view import Interfaz
from tkinter import *

class App:
    def __init__(self,ventana):
        view = Interfaz.Vistas(ventana)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()
