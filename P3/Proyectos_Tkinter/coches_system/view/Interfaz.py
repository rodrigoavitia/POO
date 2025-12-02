from tkinter import *
from tkinter import messagebox


class Vistas():
    def __init__(self,ventana):
        ventana.geometry("800x600")
        ventana.title("Coches system")
        self.menu_principal(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=".:: Menu principal ::.")
        lblTitulo.pack(pady=5)
        btnCoches=Button(ventana,text="1.- Coches",command=lambda : self.menu_acciones(ventana,"coches"))
        btnCoches.pack(pady=5)
        btnCamiones=Button(ventana,text="2.- Camiones",command=lambda: "self.menu_acciones(ventana,camiones)")
        btnCamiones.pack(pady=5)
        btnCamionetas=Button(ventana,text="3.- Camionetas",command=lambda: "self.menu_acciones(ventana,camionetas)")
        btnCamionetas.pack(pady=5)
        btnSalir=Button(ventana,text="4.- Salir",command=ventana.quit)
        btnSalir.pack(pady=5)

    def menu_acciones(self,ventana,vehiculo):
        global tipo
        tipo=vehiculo
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Menu de {tipo}")
        lblTitulo.pack(pady=5)
        btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: self.insertar_autos(ventana))
        btnAgregar.pack(pady=5)
        btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: self.consultar_autos()(ventana))
        btnMostrar.pack(pady=5)
        btnCambiar=Button(ventana,text="3.-Cambiar",command=lambda: self.cambiar_autos(ventana))
        btnCambiar.pack(pady=5)
        btnEliminar=Button(ventana,text="4.-Eliminar",command=lambda: self.borrar_autos()(ventana))
        btnEliminar.pack(pady=5)
        btnSalir=Button(ventana,text="5.-Volver",command=lambda: self.menu_principal(ventana))
        btnSalir.pack(pady=5)


    def insertar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Agregar coches")
        lblTitulo.pack(pady=5)
        lblMarca=Label(ventana,text="Inserte marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        btnAgregar=Button(ventana,text="Agregar",command= lambda: "")
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def consultar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Coches agregados")
        lblTitulo.pack(pady=5)
        filas=""
        registros=[("1","Toyota","Rojo","2019","180","300","4"),("2","Renoult","Gris","2019","300","400","4")]
        if len(registros)>0:
          num_autos=1
          for fila in registros:
            filas=filas+f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]}"
            num_autos+=1
        else:
            messagebox.showinfo(message="No hay coches por el momento en el sistema")

        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command=lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def cambiar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Modificar el coche")
        lblTitulo.pack(pady=5)

        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()

        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command= lambda: "")
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def borrar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Eliminar un coche")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        btnEliminar=Button(ventana,text="Eliminar",command= lambda:"")
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)