
"""
Crear una calculadora:
1.- Dos campos de Texto
2.- 4 botones para las Operaciones
3.- Mostrar el Resultado en una alerta
4.- Programación OO
5.- Implementar el MVC (patron de diseño modelo vista controlador)

"""
from view import interfaz
from tkinter import *

class App:
    def __init__(self,ventana):
        view=interfaz.Vistas(ventana)
        
        # interfaz.interfaz()
# def main():
#     interfaz.interfaz() #manda a llamar del modulo interfaz solo la funcion interfaz
    
if __name__=="__main__":
    ventana=Tk()   
    app=App(ventana)
    ventana.mainloop()