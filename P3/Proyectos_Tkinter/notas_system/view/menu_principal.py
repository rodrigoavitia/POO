
from tkinter import *
from tkinter import messagebox
from controller import controlador
class InterfacesMenu():
    def __init__(self,ventana):
        ventana.title("Gestion de Notas")
        ventana.geometry("600x400")
        InterfacesMenu.menu_interfaz(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_interfaz(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Menu principal")
        lblTitulo.pack(pady=5)
        btnRegistro=Button(ventana,text="1.-Registro",command=lambda: InterfacesMenu.menu_registrar(ventana))
        btnRegistro.pack(pady=5)
        btnLogin=Button(ventana,text="2.-Login",command=lambda: InterfacesMenu.menu_login(ventana))
        btnLogin.pack(pady=5)
        btnSalir=Button(ventana,text="3.-Salir",command=ventana.quit)
        btnSalir.pack(pady=5)

    @staticmethod
    def menu_registrar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Inicio de sesion")
        lblTitulo.pack(pady=5)

        nomb=StringVar()
        lblNomb=Label(ventana,text="Cual es tu nombre?")
        lblNomb.pack(pady=5)
        txtNomb=Entry(ventana,textvariable=nomb)
        txtNomb.pack(pady=5)

        apelli=StringVar()
        lblApelli=Label(ventana,text="Cuales son tus apellidos?")
        lblApelli.pack(pady=5)
        txtApelli=Entry(ventana,textvariable=apelli)
        txtApelli.pack(pady=5)

        email=StringVar()
        lblEmail=Label(ventana,text="Ingresa tu email:")
        lblEmail.pack(pady=5)
        txtEmail=Entry(ventana,textvariable=email)
        txtEmail.pack(pady=5)

        passw=StringVar()
        lblPassw=Label(ventana,text="Ingresa tu contraseña")
        lblPassw.pack(pady=5)
        txtPassw=Entry(ventana,textvariable=passw,show="*")
        txtPassw.pack(pady=5)

        btnRegistrar=Button(ventana,text="Registrar",command=lambda: (controlador.Controladores.registrar(nomb.get(),apelli.get(),email.get(),passw.get()),InterfacesMenu.menu_login(ventana)))
        btnRegistrar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_interfaz(ventana))
        btnVolver.pack(pady=5)
    
    @staticmethod
    def menu_login(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Registro del sistema")
        lblTitulo.pack(pady=5)

        email=StringVar()
        lblEmail=Label(ventana,text="Ingresa tu email:")
        lblEmail.pack(pady=5)
        txtEmail=Entry(ventana,textvariable=email)
        txtEmail.pack(pady=5)

        passw=StringVar()
        lblPassw=Label(ventana,text="Ingresa tu contraseña")
        lblPassw.pack(pady=5)
        txtPassw=Entry(ventana,textvariable=passw,show="*")
        txtPassw.pack(pady=5)

        btnEntrar=Button(ventana,text="Entrar",command=lambda: controlador.Controladores.login(ventana,email.get(),passw.get()))
        btnEntrar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_interfaz(ventana))
        btnVolver.pack(pady=5)

    @staticmethod
    def menu_notas(ventana,uid,nombre,apellidos):
        global id_user,nom_user,ape_user
        id_user=uid
        nom_user=nombre
        ape_user=apellidos
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Bienvenido {nombre} {apellidos}, has iniciado sesion",justify=CENTER)
        lblTitulo.pack(pady=5)
        btnCrear=Button(ventana,text="1.-Crear",command=lambda: InterfacesMenu.menu_crear_nota(ventana))
        btnCrear.pack(pady=5)
        btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: InterfacesMenu.menu_mostrar_nota(ventana))
        btnMostrar.pack(pady=5)
        btnCambiar=Button(ventana,text="3.-Cambiar",command=lambda: InterfacesMenu.menu_cambiar_nota(ventana))
        btnCambiar.pack(pady=5)
        btnEliminar=Button(ventana,text="4.-Eliminar",command=lambda: InterfacesMenu.menu_eliminar_nota(ventana))
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="5.-Volver",command=lambda: InterfacesMenu.menu_login(ventana))
        btnVolver.pack(pady=5)

    @staticmethod
    def menu_crear_nota(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Crear nota")
        lblTitulo.pack(pady=5)

        titulo=StringVar()
        lblTit=Label(ventana,text="Titulo")
        lblTit.pack(pady=5)
        txtTit=Entry(ventana,textvariable=titulo)
        txtTit.focus()
        txtTit.pack(pady=5)

        desc=StringVar()
        lblDesc=Label(ventana,text="Descripcion")
        lblDesc.pack(pady=5)
        txtDesc=Entry(ventana,textvariable=desc)
        txtDesc.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command=lambda: controlador.Controladores.crear_nota(titulo.get(),desc.get(),id_user))
        btnGuardar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_notas(ventana,id_user,nom_user,ape_user))
        btnVolver.pack(pady=5)
    
    @staticmethod
    def menu_mostrar_nota(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"{nom_user} {ape_user}, tus notas son:")
        lblTitulo.pack(pady=5)
        filas=""
        registros=controlador.Controladores.mostrar_nota(id_user)
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"Nota: {num_notas}\nId: {fila[0]},Titulo:{fila[2]} Fecha de creacion: {fila[4]}\nDescripcion:{fila[3]}\n"
                num_notas+=1
        else:
            messagebox.showinfo(message="No existen notas en el sistema")

        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_notas(ventana,id_user,nom_user,ape_user))
        btnVolver.pack(pady=5)
  
    @staticmethod
    def menu_cambiar_nota(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"{nom_user} {ape_user}, vamos a modificar una nota")
        lblTitulo.pack(pady=5)

        id=IntVar()
        lblId=Label(ventana,text="Id de la nota a cambiar")
        lblId.pack(pady=5)
        txtId=Entry(ventana,textvariable=id,justify=CENTER)
        txtId.pack(pady=5)

        titulo=StringVar()
        lblTit=Label(ventana,text="Titulo")
        lblTit.pack(pady=5)
        txtTit=Entry(ventana,textvariable=titulo)
        txtTit.pack(pady=5)

        desc=StringVar()
        lblDesc=Label(ventana,text="Descripcion")
        lblDesc.pack(pady=5)
        txtDesc=Entry(ventana,textvariable=desc)
        txtDesc.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command=lambda: controlador.Controladores.modificar_nota(id.get(),titulo.get(),desc.get()))
        btnGuardar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_notas(ventana,id_user,nom_user,ape_user))
        btnVolver.pack(pady=5)
   
    @staticmethod
    def menu_eliminar_nota(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"{nom_user} {ape_user}, vamos a eliminar una nota")
        lblTitulo.pack(pady=5)

        id=IntVar()
        lblId=Label(ventana,text="Id de la nota a eliminar")
        lblId.pack(pady=5)
        txtId=Entry(ventana,textvariable=id,justify=CENTER)
        txtId.pack(pady=5)

        btnEliminar=Button(ventana,text="Eliminar",command=lambda: controlador.Controladores.eliminar_nota(id.get()))
        btnEliminar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_notas(ventana,id_user,nom_user,ape_user))
        btnVolver.pack(pady=5)