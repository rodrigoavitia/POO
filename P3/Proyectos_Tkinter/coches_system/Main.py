import tkinter as tk
from view.Interfaz import VentanaApp
from controller.funciones import Controlador

"""
1 Diciembre
1)Implementacion de MVC
2)POO
3) INTERFACES NECESARIAS:
    3.1 menu_principal()
    3.2 menu_acciones()
    3.3 insertar_autos()
    3.4 consultar_autos()
    3.5 cambiar_autos()
    3.6 borrar_autos()

3 Diciembre 
    Interfaces necesarias:
        insertar_camionetas()
        consultar_camionetas(
        cambiar_camionetas()
        borrar_camionetas

        *LO MISMO PARA CAMIONES*

        
4 Diciembre
    LA CONEXION CON BASE DE DATOS DEBE FUNCIONAR
        insertar
        consultar
        cambiar
        borrar

        *PARA TODOS LOS VEHICULOS*
"""




if __name__ == "__main__":
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema CRUD de Vehículos")
    
    controlador = Controlador()
    
    aplicacion = VentanaApp(ventana_principal, controlador)
    
    ventana_principal.mainloop()