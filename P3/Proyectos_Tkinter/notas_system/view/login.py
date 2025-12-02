
from tkinter import *
from view import menu_principal
class InterfacesLogin():
    def __init__(self,ventana):
        ventana.title("Inicio de sesion")
        ventana.geometry("600x400")
        
    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_login(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Inicio de sesion")
        lblTitulo.pack(pady=5)

        lblNomb=Label(ventana,text="Cual es tu nombre?")
        lblNomb.pack(pady=5)
        txtNomb=Entry(ventana)
        txtNomb.pack(pady=5)

        lblApelli=Label(ventana,text="Cuales son tus apellidos?")
        lblApelli.pack(pady=5)
        txtApelli=Entry(ventana)
        txtApelli.pack(pady=5)

        lblEmail=Label(ventana,text="Ingresa tu email:")
        lblEmail.pack(pady=5)
        txtEmail=Entry(ventana)
        txtEmail.pack(pady=5)

        lblPassw=Label(ventana,text="Ingresa tu contraseña")
        lblPassw.pack(pady=5)
        txtPassw=Entry(ventana)
        txtPassw.pack(pady=5)

        btnRegistrar=Button(ventana,text="Registrar",command="")
        btnRegistrar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=menu_principal.InterfacesMenu(ventana))
        btnVolver.pack(pady=5)