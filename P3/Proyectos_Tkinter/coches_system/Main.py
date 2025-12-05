'''
1.- Paradigma POO
2.- Implementar MVC
3.- App de escritorio con interfaz grafica
'''
from tkinter import *
from view import interfaz
class App():
    def __init__(self,ventana):
        interfaz.InterfacesMenu(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()