"""
1.-Paradigma OO
2.- Implementar el MVC
3.- App de Escritorio con interfaz gráfica

"""
from tkinter import *

class App:
    def __init__(self,ventana):
        from view.menu_principal import InterfacesMenu
        self.ventana=ventana
        self.menu=InterfacesMenu(ventana)
    
if __name__=="__main__":
    ventana=Tk() 
    app=App(ventana)
    ventana.mainloop()   