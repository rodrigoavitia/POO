import tkinter as tk
from tkinter import ttk, messagebox
from controller.funciones import Controlador 

class VentanaApp:
    def __init__(self, contenedor_principal: tk.Tk, controlador: Controlador):
        self.contenedor_principal = contenedor_principal 
        self.controlador = controlador 
        self.contenedor_principal.title("Sistema CRUD Vehículos (Autos, Camionetas y Camiones)")
        self.contenedor_principal.geometry("950x550")
        
        self.id_var = tk.StringVar()
        self.marca_var = tk.StringVar()
        self.color_var = tk.StringVar()
        self.modelo_var = tk.StringVar()
        self.velocidad_var = tk.StringVar()
        self.caballaje_var = tk.StringVar()
        self.plazas_var = tk.StringVar()
        
        self.traccion_var = tk.StringVar()
        self.cerrada_var = tk.StringVar()
        self.eje_var = tk.StringVar()
        self.capacidad_carga_var = tk.StringVar()
        
        self.notebook = None
        self.tabla_activa = None
        
        self.crear_notebook()
        self.inicializar_tablas()

    def crear_notebook(self):
        self.notebook = ttk.Notebook(self.contenedor_principal)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")
        
        self.frame_autos = ttk.Frame(self.notebook, padding="10")
        self.frame_camionetas = ttk.Frame(self.notebook, padding="10")
        self.frame_camiones = ttk.Frame(self.notebook, padding="10")
        
        self.frame_autos.pack(fill='both', expand=True)
        self.frame_camionetas.pack(fill='both', expand=True)
        self.frame_camiones.pack(fill='both', expand=True)
        
        self.notebook.add(self.frame_autos, text='  Autos  ')
        self.notebook.add(self.frame_camionetas, text='  Camionetas  ')
        self.notebook.add(self.frame_camiones, text='  Camiones  ')
        
        self.crear_widgets_autos(self.frame_autos)
        self.crear_widgets_camionetas(self.frame_camionetas)
        self.crear_widgets_camiones(self.frame_camiones)
        
    def inicializar_tablas(self):
        self.notebook.bind("<<NotebookTabChanged>>", self.cargar_datos_pestaña_activa)
        self.consultar_autos()
        self.tabla_activa = self.tabla_autos
        
    def cargar_datos_pestaña_activa(self, event):
        pestaña_actual = self.notebook.tab(self.notebook.select(), "text").strip()
        self.limpiar_campos()
        
        if "Autos" in pestaña_actual:
            self.consultar_autos()
            self.tabla_activa = self.tabla_autos
        elif "Camionetas" in pestaña_actual:
            self.consultar_camionetas()
            self.tabla_activa = self.tabla_camionetas
        elif "Camiones" in pestaña_actual:
            self.consultar_camiones()
            self.tabla_activa = self.tabla_camiones

    def limpiar_campos(self):
        self.id_var.set("")
        self.marca_var.set("")
        self.color_var.set("")
        self.modelo_var.set("")
        self.velocidad_var.set("")
        self.caballaje_var.set("")
        self.plazas_var.set("")
        self.traccion_var.set("")
        self.cerrada_var.set("")
        self.eje_var.set("")
        self.capacidad_carga_var.set("")

    def crear_label_entry(self, contenedor, texto, variable, fila, columna):
        ttk.Label(contenedor, text=texto).grid(row=fila, column=columna, padx=5, pady=5, sticky="w")
        ttk.Entry(contenedor, textvariable=variable, width=15 if 'ID' in texto or 'Año' in texto else 20).grid(row=fila, column=columna + 1, padx=5, pady=5)

    def crear_tabla(self, contenedor, columnas):
        tabla = ttk.Treeview(contenedor, columns=columnas, show="headings")
        
        for col in columnas:
            tabla.heading(col, text=col)
            if col == "id": tabla.column(col, width=40, anchor=tk.CENTER)
            elif col == "marca" or col == "modelo" or col == "color" or col == "traccion": tabla.column(col, width=100, anchor=tk.W)
            else: tabla.column(col, width=80, anchor=tk.CENTER)

        barra_desplazamiento = ttk.Scrollbar(contenedor, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=barra_desplazamiento.set)
        
        barra_desplazamiento.pack(side=tk.RIGHT, fill=tk.Y)
        tabla.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        return tabla

    # INTERFAZ AUTOS
    def crear_widgets_autos(self, contenedor):
        marco_entrada = ttk.Frame(contenedor, padding="10")
        marco_entrada.pack(side=tk.TOP, fill=tk.X)
        
        self.crear_label_entry(marco_entrada, "ID Auto:", self.id_var, 0, 0)
        self.crear_label_entry(marco_entrada, "Marca:", self.marca_var, 1, 0)
        self.crear_label_entry(marco_entrada, "Color:", self.color_var, 1, 2)
        self.crear_label_entry(marco_entrada, "Modelo (Año):", self.modelo_var, 2, 0)
        self.crear_label_entry(marco_entrada, "Velocidad:", self.velocidad_var, 2, 2)
        self.crear_label_entry(marco_entrada, "Caballaje:", self.caballaje_var, 3, 0)
        self.crear_label_entry(marco_entrada, "Plazas:", self.plazas_var, 3, 2)
        
        marco_botones = ttk.Frame(contenedor, padding="10")
        marco_botones.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(marco_botones, text="Insertar Auto", command=self.insertar_auto).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Consultar Autos", command=self.consultar_autos).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Actualizar Auto", command=self.cambiar_auto).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Borrar Auto", command=self.borrar_auto).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Limpiar Campos", command=self.limpiar_campos).pack(side=tk.LEFT, padx=5, pady=5)

        columnas_autos = ("id", "marca", "color", "modelo", "velocidad", "caballaje", "plazas")
        self.tabla_autos = self.crear_tabla(contenedor, columnas_autos)
        self.tabla_autos.bind('<<TreeviewSelect>>', self.seleccionar_registro_auto)

    # INTERFAZ CAMIONETAS
    def crear_widgets_camionetas(self, contenedor):
        marco_entrada = ttk.Frame(contenedor, padding="10")
        marco_entrada.pack(side=tk.TOP, fill=tk.X)
        
        self.crear_label_entry(marco_entrada, "ID Camioneta:", self.id_var, 0, 0)
        self.crear_label_entry(marco_entrada, "Marca:", self.marca_var, 1, 0)
        self.crear_label_entry(marco_entrada, "Color:", self.color_var, 1, 2)
        self.crear_label_entry(marco_entrada, "Modelo (Año):", self.modelo_var, 2, 0)
        self.crear_label_entry(marco_entrada, "Velocidad:", self.velocidad_var, 2, 2)
        self.crear_label_entry(marco_entrada, "Caballaje:", self.caballaje_var, 3, 0)
        self.crear_label_entry(marco_entrada, "Plazas:", self.plazas_var, 3, 2)
        
        self.crear_label_entry(marco_entrada, "Tracción:", self.traccion_var, 4, 0)
        self.crear_label_entry(marco_entrada, "Cerrada (0/1):", self.cerrada_var, 4, 2)
        
        marco_botones = ttk.Frame(contenedor, padding="10")
        marco_botones.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(marco_botones, text="Insertar Camioneta", command=self.insertar_camioneta).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Consultar Camionetas", command=self.consultar_camionetas).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Actualizar Camioneta", command=self.cambiar_camioneta).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Borrar Camioneta", command=self.borrar_camioneta).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Limpiar Campos", command=self.limpiar_campos).pack(side=tk.LEFT, padx=5, pady=5)

        columnas_camionetas = ("id", "marca", "color", "modelo", "velocidad", "caballaje", "plazas", "traccion", "cerrada")
        self.tabla_camionetas = self.crear_tabla(contenedor, columnas_camionetas)
        self.tabla_camionetas.bind('<<TreeviewSelect>>', self.seleccionar_registro_camioneta)

    # INTERFAZ CAMIONES
    def crear_widgets_camiones(self, contenedor):
        marco_entrada = ttk.Frame(contenedor, padding="10")
        marco_entrada.pack(side=tk.TOP, fill=tk.X)
        
        self.crear_label_entry(marco_entrada, "ID Camión:", self.id_var, 0, 0)
        self.crear_label_entry(marco_entrada, "Marca:", self.marca_var, 1, 0)
        self.crear_label_entry(marco_entrada, "Color:", self.color_var, 1, 2)
        self.crear_label_entry(marco_entrada, "Modelo (Año):", self.modelo_var, 2, 0)
        self.crear_label_entry(marco_entrada, "Velocidad:", self.velocidad_var, 2, 2)
        self.crear_label_entry(marco_entrada, "Caballaje:", self.caballaje_var, 3, 0)
        self.crear_label_entry(marco_entrada, "Plazas:", self.plazas_var, 3, 2)
        
        self.crear_label_entry(marco_entrada, "Eje:", self.eje_var, 4, 0)
        self.crear_label_entry(marco_entrada, "Capacidad Carga:", self.capacidad_carga_var, 4, 2)
        
        marco_botones = ttk.Frame(contenedor, padding="10")
        marco_botones.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(marco_botones, text="Insertar Camión", command=self.insertar_camion).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Consultar Camiones", command=self.consultar_camiones).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Actualizar Camión", command=self.cambiar_camion).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Borrar Camión", command=self.borrar_camion).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(marco_botones, text="Limpiar Campos", command=self.limpiar_campos).pack(side=tk.LEFT, padx=5, pady=5)

        columnas_camiones = ("id", "marca", "color", "modelo", "velocidad", "caballaje", "plazas", "eje", "capacidadcarga")
        self.tabla_camiones = self.crear_tabla(contenedor, columnas_camiones)
        self.tabla_camiones.bind('<<TreeviewSelect>>', self.seleccionar_registro_camion)


    # MÉTODOS CRUD AUTOS
    def insertar_auto(self):
        resultado = self.controlador.insertar_auto(self.id_var.get(), self.marca_var.get(), self.color_var.get(), self.modelo_var.get(), self.velocidad_var.get(), self.caballaje_var.get(), self.plazas_var.get())
        messagebox.showinfo("Insertar", resultado)
        self.limpiar_campos()
        self.consultar_autos()

    def consultar_autos(self):
        self.tabla_activa = self.tabla_autos
        for item in self.tabla_activa.get_children(): self.tabla_activa.delete(item)
        registros = self.controlador.consultar_autos()
        for registro in registros: self.tabla_activa.insert('', tk.END, values=registro)
            
    def cambiar_auto(self):
        resultado = self.controlador.cambiar_auto(self.id_var.get(), self.marca_var.get(), self.color_var.get(), self.modelo_var.get(), self.velocidad_var.get(), self.caballaje_var.get(), self.plazas_var.get())
        messagebox.showinfo("Actualizar", resultado)
        self.limpiar_campos()
        self.consultar_autos()

    def borrar_auto(self):
        id_a_borrar = self.id_var.get()
        if not id_a_borrar: messagebox.showerror("Error", "Debe seleccionar o ingresar un ID para borrar."); return
        confirmar = messagebox.askyesno("Confirmar Borrado", f"¿Está seguro de borrar el Auto con ID {id_a_borrar}?")
        if confirmar:
            resultado = self.controlador.borrar_auto(id_a_borrar)
            messagebox.showinfo("Borrar", resultado)
            self.limpiar_campos()
            self.consultar_autos()

    def seleccionar_registro_auto(self, event):
        item_seleccionado = self.tabla_autos.focus()
        if item_seleccionado:
            valores = self.tabla_autos.item(item_seleccionado, 'values')
            self.id_var.set(valores[0])
            self.marca_var.set(valores[1])
            self.color_var.set(valores[2])
            self.modelo_var.set(valores[3])
            self.velocidad_var.set(valores[4])
            self.caballaje_var.set(valores[5])
            self.plazas_var.set(valores[6])
            self.traccion_var.set(""); self.cerrada_var.set(""); self.eje_var.set(""); self.capacidad_carga_var.set("") 


    # MÉTODOS CRUD CAMIONETAS
    def insertar_camioneta(self):
        resultado = self.controlador.insertar_camioneta(self.marca_var.get(), self.color_var.get(), self.modelo_var.get(), self.velocidad_var.get(), self.caballaje_var.get(), self.plazas_var.get(), self.traccion_var.get(), self.cerrada_var.get())
        messagebox.showinfo("Insertar Camioneta", resultado)
        self.limpiar_campos()
        self.consultar_camionetas()

    def consultar_camionetas(self):
        self.tabla_activa = self.tabla_camionetas
        for item in self.tabla_activa.get_children(): self.tabla_activa.delete(item)
        registros = self.controlador.consultar_camionetas()
        for registro in registros: self.tabla_activa.insert('', tk.END, values=registro)
            
    def cambiar_camioneta(self):
        resultado = self.controlador.cambiar_camioneta(self.id_var.get(), self.marca_var.get(), self.color_var.get(), self.modelo_var.get(), self.velocidad_var.get(), self.caballaje_var.get(), self.plazas_var.get(), self.traccion_var.get(), self.cerrada_var.get())
        messagebox.showinfo("Actualizar Camioneta", resultado)
        self.limpiar_campos()
        self.consultar_camionetas()

    def borrar_camioneta(self):
        id_a_borrar = self.id_var.get()
        if not id_a_borrar: messagebox.showerror("Error", "Debe seleccionar o ingresar un ID para borrar."); return
        confirmar = messagebox.askyesno("Confirmar Borrado", f"¿Está seguro de borrar la Camioneta con ID {id_a_borrar}?")
        if confirmar:
            resultado = self.controlador.borrar_camioneta(id_a_borrar)
            messagebox.showinfo("Borrar Camioneta", resultado)
            self.limpiar_campos()
            self.consultar_camionetas()

    def seleccionar_registro_camioneta(self, event):
        item_seleccionado = self.tabla_camionetas.focus()
        if item_seleccionado:
            valores = self.tabla_camionetas.item(item_seleccionado, 'values')
            self.id_var.set(valores[0])
            self.marca_var.set(valores[1])
            self.color_var.set(valores[2])
            self.modelo_var.set(valores[3])
            self.velocidad_var.set(valores[4])
            self.caballaje_var.set(valores[5])
            self.plazas_var.set(valores[6])
            self.traccion_var.set(valores[7])
            self.cerrada_var.set(valores[8])
            self.eje_var.set(""); self.capacidad_carga_var.set("") 

    
    # MÉTODOS CRUD CAMIONES
    def insertar_camion(self):
        resultado = self.controlador.insertar_camion(self.marca_var.get(), self.color_var.get(), self.modelo_var.get(), self.velocidad_var.get(), self.caballaje_var.get(), self.plazas_var.get(), self.eje_var.get(), self.capacidad_carga_var.get())
        messagebox.showinfo("Insertar Camión", resultado)
        self.limpiar_campos()
        self.consultar_camiones()

    def consultar_camiones(self):
        self.tabla_activa = self.tabla_camiones
        for item in self.tabla_activa.get_children(): self.tabla_activa.delete(item)
        registros = self.controlador.consultar_camiones()
        for registro in registros: self.tabla_activa.insert('', tk.END, values=registro)
            
    def cambiar_camion(self):
        resultado = self.controlador.cambiar_camion(self.id_var.get(), self.marca_var.get(), self.color_var.get(), self.modelo_var.get(), self.velocidad_var.get(), self.caballaje_var.get(), self.plazas_var.get(), self.eje_var.get(), self.capacidad_carga_var.get())
        messagebox.showinfo("Actualizar Camión", resultado)
        self.limpiar_campos()
        self.consultar_camiones()

    def borrar_camion(self):
        id_a_borrar = self.id_var.get()
        if not id_a_borrar: messagebox.showerror("Error", "Debe seleccionar o ingresar un ID para borrar."); return
        confirmar = messagebox.askyesno("Confirmar Borrado", f"¿Está seguro de borrar el Camión con ID {id_a_borrar}?")
        if confirmar:
            resultado = self.controlador.borrar_camion(id_a_borrar)
            messagebox.showinfo("Borrar Camión", resultado)
            self.limpiar_campos()
            self.consultar_camiones()

    def seleccionar_registro_camion(self, event):
        item_seleccionado = self.tabla_camiones.focus()
        if item_seleccionado:
            valores = self.tabla_camiones.item(item_seleccionado, 'values')
            self.id_var.set(valores[0])
            self.marca_var.set(valores[1])
            self.color_var.set(valores[2])
            self.modelo_var.set(valores[3])
            self.velocidad_var.set(valores[4])
            self.caballaje_var.set(valores[5])
            self.plazas_var.set(valores[6])
            self.eje_var.set(valores[7])
            self.capacidad_carga_var.set(valores[8])
            self.traccion_var.set(""); self.cerrada_var.set("")