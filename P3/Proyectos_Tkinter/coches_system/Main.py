import tkinter as tk
from view.Interfaz import VentanaApp
from controller.funciones import Controlador

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema CRUD de Vehículos")
    
    controlador = Controlador()
    
    aplicacion = VentanaApp(ventana_principal, controlador)
    
    ventana_principal.mainloop()