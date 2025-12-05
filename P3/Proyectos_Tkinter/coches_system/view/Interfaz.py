from tkinter import *
from tkinter import messagebox
# Asegúrate de que tus controladores se llamen así en tu archivo controller/controlador.py
from controller.controlador import AutosControlador, CamionetasControlador, CamionesControlador 

class InterfacesMenu():
    def __init__(self,ventana):
        ventana.geometry("800x600")
        ventana.title("Coches system")
        InterfacesMenu.menu_principal(ventana)
        
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
            
    @staticmethod
    def menu_principal(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Menu principal")
        lblTitulo.pack(pady=5)
        btnCoches=Button(ventana,text="1.-Coches",command=lambda : InterfacesMenu.menu_acciones(ventana,"coches"))
        btnCoches.pack(pady=5)
        btnCamiones=Button(ventana,text="2.-Camiones",command=lambda: InterfacesMenu.menu_acciones(ventana,"camiones"))
        btnCamiones.pack(pady=5)
        btnCamionetas=Button(ventana,text="3.-Camionetas",command=lambda: InterfacesMenu.menu_acciones(ventana,"camionetas"))
        btnCamionetas.pack(pady=5)
        btnSalir=Button(ventana,text="4.-Salir",command=ventana.quit)
        btnSalir.pack(pady=5)
    
    @staticmethod
    def menu_acciones(ventana,vehiculo):
        global tipo
        tipo=vehiculo
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Menu de {tipo}")
        lblTitulo.pack(pady=5)
        
        # Asignación correcta de botones según el tipo
        if tipo=="coches":
            btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: InterfacesMenu.coches_agregar(ventana))
            btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: InterfacesMenu.coches_mostrar(ventana))
        elif tipo=="camionetas":
            btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: InterfacesMenu.camionetas_agregar(ventana)) 
            btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: InterfacesMenu.camionetas_mostrar(ventana))
        elif tipo=="camiones":
            btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: InterfacesMenu.camiones_agregar(ventana))
            btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: InterfacesMenu.camiones_mostrar(ventana))
        
        btnAgregar.pack(pady=5)
        btnMostrar.pack(pady=5)

        btnCambiar=Button(ventana,text="3.-Cambiar",command=lambda: InterfacesMenu.intrfaz_buscar_cambiar(ventana))
        btnCambiar.pack(pady=5)
        btnEliminar=Button(ventana,text="4.-Eliminar",command=lambda: InterfacesMenu.intrfaz_buscar_eliminar(ventana))
        btnEliminar.pack(pady=5)
        btnSalir=Button(ventana,text="5.-Volver",command=lambda: InterfacesMenu.menu_principal(ventana))
        btnSalir.pack(pady=5)


# --- COCHES ---

    @staticmethod
    def coches_agregar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Agregar coches")
        lblTitulo.pack(pady=5)
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

        btnAgregar=Button(ventana,text="Agregar",command= lambda: AutosControlador.insertar_coche(txtMarca.get(),txtColor.get(),txtModelo.get(),txtVelocidad.get(),txtPotencia.get(),txtPlazas.get()))
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def coches_mostrar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Coches agregados")
        lblTitulo.pack(pady=5)
        filas=""
        registros=AutosControlador.mostrar_coche() 
        num_autos=1
        if registros:
            for fila in registros:
                filas=filas+f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]}"
                num_autos+=1
        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def coches_cambiar(ventana,opid):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Cambiar coche")
        lblTitulo.pack(pady=5)

        lblId=Label(ventana,text="ID a Modificar:")
        lblId.pack(pady=5)
        
        # CORRECCIÓN: Usar StringVar y borrar contenido previo
        id_modificar=StringVar() 
        txtId=Entry(ventana,textvariable=id_modificar)
        txtId.delete(0,END)
        txtId.insert(0,opid) # Insertar el ID limpio
        txtId.config(state="readonly")
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

        btnGuardar=Button(ventana,text="Guardar",command= lambda: AutosControlador.actualizar_coche(txtMarca.get(),txtColor.get(),txtModelo.get(),txtVelocidad.get(),txtPotencia.get(),txtPlazas.get(),id_modificar.get()))
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def coches_eliminar(ventana,opid):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Eliminar un coche")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="ID a Eliminar:")
        lblId.pack(pady=5)
        
        # CORRECCIÓN: Usar StringVar
        id_eliminar=StringVar() 
        txtId=Entry(ventana,textvariable=id_eliminar)
        txtId.delete(0,END)
        txtId.insert(0,opid) 
        txtId.config(state="readonly")
        txtId.pack()
        
        btnEliminar=Button(ventana,text="Eliminar",command= lambda:AutosControlador.eliminar_coche(id_eliminar.get()))
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)


# --- CAMIONES ---

    @staticmethod
    def camiones_agregar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Agregar {tipo}")
        lblTitulo.pack(pady=5)
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

        lblEje=Label(ventana,text="Ingrese el eje")
        lblEje.pack(pady=5)
        txtEje=Entry(ventana)
        txtEje.pack()

        lblCapacidad=Label(ventana,text="Ingrese la capacidad")
        lblCapacidad.pack(pady=5)
        txtCapacidad=Entry(ventana)
        txtCapacidad.pack()

        btnAgregar=Button(ventana,text="Agregar",command= lambda: CamionesControlador.insertar_camion(txtMarca.get(),txtColor.get(),txtModelo.get(),txtVelocidad.get(),txtPotencia.get(),txtPlazas.get(),txtEje.get(),txtCapacidad.get()))
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def camiones_mostrar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Mostrar {tipo}")
        lblTitulo.pack(pady=5)
        filas=""
        registros=CamionesControlador.mostrar_camion()
        
        if registros:
            num_camion=1
            for fila in registros:
                filas=filas+f"\nCamion #{num_camion} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]} Eje: {fila[7]} Capacidad: {fila[8]}"
                num_camion+=1
        
        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def camiones_eliminar(ventana, opid=None):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Eliminar un {tipo}")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="ID a eliminar:")
        lblId.pack(pady=5)
        
        # CORRECCIÓN: Usar StringVar
        id_eliminar=StringVar()
        txtId=Entry(ventana,textvariable=id_eliminar)
        if opid is not None:
            txtId.delete(0,END)
            txtId.insert(0,opid)
            txtId.config(state="readonly")
        txtId.pack()
        
        btnEliminar=Button(ventana,text="Eliminar",command= lambda: CamionesControlador.eliminar_camion(id_eliminar.get()))
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def camiones_cambiar(ventana, opid=None):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Modificar {tipo}")
        lblTitulo.pack(pady=5)
        
        lblId=Label(ventana,text="ID a modificar:")
        lblId.pack(pady=5)
        # CORRECCIÓN: Usar StringVar
        id_modificar=StringVar()
        txtId=Entry(ventana,textvariable=id_modificar)
        if opid is not None:
            txtId.delete(0,END)
            txtId.insert(0,opid)
            txtId.config(state="readonly")
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

        lblEje=Label(ventana,text="Ingrese el eje")
        lblEje.pack(pady=5)
        txtEje=Entry(ventana)
        txtEje.pack()

        lblCapacidad=Label(ventana,text="Ingrese la capacidad")
        lblCapacidad.pack(pady=5)
        txtCapacidad=Entry(ventana)
        txtCapacidad.pack()

        btnGuardar=Button(ventana,text="Guardar",command= lambda: CamionesControlador.actualizar_camion(txtMarca.get(),txtColor.get(),txtModelo.get(),txtVelocidad.get(),txtPotencia.get(),txtPlazas.get(),txtEje.get(),txtCapacidad.get(), id_modificar.get()))
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)


# --- CAMIONETAS ---

    # Función auxiliar para Listbox
    @staticmethod
    def obtener_seleccion_lbx(listbox):
        try:
            indice = listbox.curselection()[0]
            return listbox.get(indice)
        except IndexError:
            messagebox.showinfo(message="Debe seleccionar una opción en Tracción y Cerrada.", title="Error de Selección", icon="warning")
            return None

    @staticmethod
    def camionetas_agregar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Agregar {tipo}")
        lblTitulo.pack(pady=5)
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

        lblTraccion=Label(ventana,text="Ingrese la traccion")
        lblTraccion.pack(pady=5)
        lbxTraccion=Listbox(ventana,width=10,height=3,selectmode="single",exportselection=False)
        traccion=["Trasera","Delantera","Total"]
        for i in traccion:
            lbxTraccion.insert(END,i)
        lbxTraccion.pack()

        lblCerrada=Label(ventana,text="Es cerrada?")
        lblCerrada.pack(pady=5)
        lbxCerrada=Listbox(ventana,width=10,height=2,selectmode="single",exportselection=False)
        eleccion=["Si","No"]
        for i in eleccion:
            lbxCerrada.insert(END,i)
        lbxCerrada.pack()

        btnAgregar=Button(ventana,text="Agregar",command= lambda: CamionetasControlador.insertar_camioneta(txtMarca.get(),txtColor.get(),txtModelo.get(),txtVelocidad.get(),txtPotencia.get(),txtPlazas.get(),InterfacesMenu.obtener_seleccion_lbx(lbxTraccion),InterfacesMenu.obtener_seleccion_lbx(lbxCerrada)))
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def camionetas_mostrar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Mostrar {tipo}")
        lblTitulo.pack(pady=5)
        filas=""
        registros=CamionetasControlador.mostrar_camioneta()
        
        if registros:
            num_camion=1
            for fila in registros:
                cerrada_txt = "Sí" if fila[8] == 1 else "No"
                filas=filas+f"\nAuto #{num_camion} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]} Tracción: {fila[7]} Cerrada: {cerrada_txt}"
                num_camion+=1
        
        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def camionetas_eliminar(ventana, opid=None):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Eliminar una {tipo}")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="ID a eliminar:")
        lblId.pack(pady=5)
        
        # CORRECCIÓN: Usar StringVar
        id_eliminar=StringVar()
        txtId=Entry(ventana,textvariable=id_eliminar)
        if opid is not None:
            txtId.delete(0,END)
            txtId.insert(0,opid)
            txtId.config(state="readonly")
        txtId.pack()
        
        btnEliminar=Button(ventana,text="Eliminar",command= lambda: CamionetasControlador.eliminar_camioneta(id_eliminar.get()))
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    @staticmethod
    def camionetas_cambiar(ventana, opid=None):
        InterfacesMenu.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Modificar {tipo}")
        lblTitulo.pack(pady=5)
        
        lblId=Label(ventana,text="ID a modificar:")
        lblId.pack(pady=5)
        # CORRECCIÓN: Usar StringVar
        id_modificar=StringVar()
        txtId=Entry(ventana,textvariable=id_modificar)
        if opid is not None:
            txtId.delete(0,END)
            txtId.insert(0,opid)
            txtId.config(state="readonly")
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
        
        lblTraccion=Label(ventana,text="Ingrese la traccion")
        lblTraccion.pack(pady=5)
        lbxTraccion=Listbox(ventana,width=10,height=3,selectmode="single",exportselection=False)
        traccion=["Trasera","Delantera","Total"]
        for i in traccion:
            lbxTraccion.insert(END,i)
        lbxTraccion.pack()

        lblCerrada=Label(ventana,text="Es cerrada?")
        lblCerrada.pack(pady=5)
        lbxCerrada=Listbox(ventana,width=10,height=2,selectmode="single",exportselection=False)
        eleccion=["Si","No"]
        for i in eleccion:
            lbxCerrada.insert(END,i)
        lbxCerrada.pack()
        
        btnGuardar=Button(ventana,text="Guardar",command= lambda: CamionetasControlador.actualizar_camioneta(txtMarca.get(),txtColor.get(),txtModelo.get(),txtVelocidad.get(),txtPotencia.get(),txtPlazas.get(),InterfacesMenu.obtener_seleccion_lbx(lbxTraccion),InterfacesMenu.obtener_seleccion_lbx(lbxCerrada), id_modificar.get()))
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)
        
    # --- BÚSQUEDA GENERAL ---
    @staticmethod
    def intrfaz_buscar_cambiar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        
        lblTitulo=Label(ventana,text=f".:Buscar un vehículo:.")
        lblTitulo.pack(pady=10)

        lblId=Label(ventana,text=f"ID del vehículo:")
        lblId.pack(pady=10)

        # CORRECCIÓN CRÍTICA: Usar StringVar evita el "0" inicial
        id_val=StringVar()
        txtId=Entry(ventana,textvariable=id_val)
        txtId.pack(pady=10)
        txtId.focus()
        
        # Seleccionar controlador
        if tipo=="coches":
            Controlador = AutosControlador
        elif tipo=="camiones":
            Controlador = CamionesControlador
        elif tipo=="camionetas":
            Controlador = CamionetasControlador
        else:
            return

        # Convertimos a int() al enviar al controlador
        btnCambiar=Button(ventana,text=f"Buscar",command=lambda:Controlador.buscarId_modificar(ventana,int(id_val.get()) if id_val.get().isdigit() else 0, tipo))
        btnCambiar.pack(pady=10)
        
        btnVolver=Button(ventana,text=f"Volver",command=lambda:InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=10)

    @staticmethod
    def intrfaz_buscar_eliminar(ventana):
        InterfacesMenu.borrarPantalla(ventana)
        
        lblTitulo=Label(ventana,text=f".:Buscar un vehículo:.")
        lblTitulo.pack(pady=10)

        lblId=Label(ventana,text=f"ID del vehículo:")
        lblId.pack(pady=10)

        # CORRECCIÓN CRÍTICA: Usar StringVar evita el "0" inicial
        id_val=StringVar()
        txtId=Entry(ventana,textvariable=id_val)
        txtId.pack(pady=10)
        txtId.focus()
        
        if tipo=="coches":
            Controlador = AutosControlador
        elif tipo=="camiones":
            Controlador = CamionesControlador
        elif tipo=="camionetas":
            Controlador = CamionetasControlador
        else:
            return

        # Convertimos a int() al enviar al controlador
        btnEliminar=Button(ventana,text=f"Buscar",command=lambda: Controlador.buscarId_eliminar(ventana,int(id_val.get()) if id_val.get().isdigit() else 0, tipo))
        btnEliminar.pack(pady=10)

        btnVolver=Button(ventana,text=f"Volver",command=lambda:InterfacesMenu.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=10)