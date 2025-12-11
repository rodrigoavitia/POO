import customtkinter as ctk
from tkinter import filedialog, messagebox
from model.vehiculos import Consultas_vehiculos

class RegistrarVehiculo(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F9FAFB")
        self.usuario_id_seleccionado = None

        # DICCIONARIO AMPLIADO DE MARCAS Y MODELOS (SE PUEDEN AGREGAR MAS, PERO LO HARE A FUTURO)
        self.datos_vehiculos = {
            "Toyota": ["Corolla", "Yaris", "Camry", "RAV4", "Hilux", "Tacoma", "Prius", "Avanza"],
            "Ford": ["Fiesta", "Focus", "Mustang", "F-150", "Escape", "Explorer", "Ranger", "Edge"],
            "Chevrolet": ["Spark", "Aveo", "Cruze", "Camaro", "Silverado", "Trax", "Suburban", "Tahoe"],
            "Nissan": ["Versa", "Sentra", "Altima", "March", "Frontier", "Kicks", "X-Trail", "Urvan"],
            "Volkswagen": ["Jetta", "Golf", "Vento", "Polo", "Tiguan", "Saveiro", "Virtus", "Taos"],
            "Honda": ["Civic", "Accord", "CR-V", "HR-V", "City", "Fit", "Pilot", "BR-V"],
            "Kia": ["Rio", "Forte", "Soul", "Sportage", "Seltos", "Sorento", "Niro"],
            "Hyundai": ["Grand i10", "Accent", "Elantra", "Tucson", "Creta", "Santa Fe"],
            "Mazda": ["Mazda 2", "Mazda 3", "Mazda 6", "CX-3", "CX-5", "CX-30", "CX-9"],
            "BMW": ["Serie 1", "Serie 3", "X1", "X3", "X5"],
            "Mercedes-Benz": ["Clase A", "Clase C", "GLA", "GLC"],
            "Audi": ["A1", "A3", "A4", "Q3", "Q5"],
            "Jeep": ["Wrangler", "Cherokee", "Renegade", "Compass"],
            "Ram": ["700", "1500", "2500"],
            "Renault": ["Kwid", "Duster", "Stepway", "Oroch"],
            "Otro": ["Otro"]
        }
        self.lista_marcas = sorted(list(self.datos_vehiculos.keys())) # Orden alfabético

        # Header
        self.header = ctk.CTkFrame(self, fg_color="white", height=80)
        self.header.pack(fill="x", padx=30, pady=30)
        ctk.CTkLabel(self.header, text="Registro de Vehículo", font=("Arial", 24, "bold"), text_color="black").pack(side="left", padx=20)
        ctk.CTkButton(self.header, text="Volver", fg_color="white", text_color="black", border_color="gray", border_width=1, command=self.volver_menu).pack(side="right", padx=20)

        # Body
        self.body = ctk.CTkFrame(self, fg_color="transparent")
        self.body.pack(fill="both", expand=True, padx=30)
        self.body.columnconfigure(0, weight=1); self.body.columnconfigure(1, weight=1)

        # IZQ
        f1 = ctk.CTkFrame(self.body, fg_color="transparent")
        f1.grid(row=0, column=0, sticky="nsew", padx=10)
        ctk.CTkLabel(f1, text="Propietario", font=("Arial", 14, "bold"), text_color="black").pack(anchor="w", pady=10)
        
        self.search_container = ctk.CTkFrame(f1, fg_color="transparent")
        self.search_container.pack(fill="x")
        self.en_buscar = ctk.CTkEntry(self.search_container, placeholder_text="Buscar nombre...", height=40)
        self.en_buscar.pack(fill="x")
        self.en_buscar.bind("<KeyRelease>", self.on_search_type)
        
        self.suggestions_frame = ctk.CTkScrollableFrame(f1, height=0, fg_color="white", border_color="gray", border_width=1)
        # Se empaqueta dinámicamente

        self.info = ctk.CTkFrame(f1, fg_color="#F3F4F6")
        self.info.pack(fill="x", pady=20)
        self.lbl_nom = ctk.CTkLabel(self.info, text="Sin selección", text_color="gray")
        self.lbl_nom.pack(pady=5)
        self.lbl_rol = ctk.CTkLabel(self.info, text="---", text_color="gray")
        self.lbl_rol.pack(pady=5)

        # DER
        f2 = ctk.CTkFrame(self.body, fg_color="transparent")
        f2.grid(row=0, column=1, sticky="nsew", padx=10)
        ctk.CTkLabel(f2, text="Vehículo", font=("Arial", 14, "bold"), text_color="black").pack(anchor="w", pady=10)
        
        # Validacion de Placa (Max 7 caracteres (SE BLOQUEA AL LLENAR LOS 7)
        vcmd = (self.register(self.validar_longitud), '%P')
        self.en_placa = ctk.CTkEntry(f2, placeholder_text="Placa (7 chars)", height=40, validate="key", validatecommand=vcmd)
        self.en_placa.pack(fill="x", pady=5)

        self.cb_marca = ctk.CTkComboBox(f2, values=self.lista_marcas, command=self.update_models)
        self.cb_marca.pack(fill="x", pady=5)
        self.cb_marca.set("Seleccionar Marca")
        
        self.cb_mod = ctk.CTkComboBox(f2, values=["-"])
        self.cb_mod.pack(fill="x", pady=5)
        
        self.en_col = self.mk_input(f2, "Color")
        self.en_anio = self.mk_input(f2, "Año")

        ctk.CTkButton(self.body, text="Registrar Vehículo", fg_color="black", height=40, command=self.guardar).grid(row=1, columnspan=2, pady=30)

        # Navegación Enter
        self.en_placa.bind("<Return>", lambda e: self.en_col.focus())
        self.en_col.bind("<Return>", lambda e: self.en_anio.focus())
        self.en_anio.bind("<Return>", lambda e: self.guardar())

    def mk_input(self, p, ph):
        e = ctk.CTkEntry(p, placeholder_text=ph, height=40)
        e.pack(fill="x", pady=5)
        return e

    # VALIDACIÓN DE LONGITUD
    def validar_longitud(self, new_text):
        if len(new_text) <= 7:
            return True
        return False

    def update_models(self, marca):
        if marca in self.datos_vehiculos:
            self.cb_mod.configure(values=self.datos_vehiculos[marca])
            self.cb_mod.set("Seleccionar Modelo")

    def on_search_type(self, event):
        t = self.en_buscar.get()
        for w in self.suggestions_frame.winfo_children(): w.destroy()
        if len(t)<2: self.suggestions_frame.pack_forget(); return
        
        res = Consultas_vehiculos.buscar_usuarios_like(t)
        if res:
            self.suggestions_frame.pack(fill="x", after=self.search_container)
            self.suggestions_frame.configure(height=min(len(res)*40, 150))
            for u in res:
                # u = (id, nombre, paterno, materno, rol)
                nombre_c = f"{u[1]} {u[2]} {u[3]}"
                btn = ctk.CTkButton(
                    self.suggestions_frame, 
                    text=f"{nombre_c} ({u[4]})", 
                    fg_color="white", text_color="black", hover_color="#EEE", anchor="w", 
                    command=lambda x=u: self.sel(x)
                )
                btn.pack(fill="x")
        else:
            self.suggestions_frame.pack_forget()

    def sel(self, u):
        # Filtro de Seguridad
        if "sud" in str(u[4]).lower() or "admin" in str(u[4]).lower() and "adminis" not in str(u[4]).lower():
            return messagebox.showerror("Restricción", "No se pueden registrar vehículos a Administradores.")
        
        self.usuario_id_seleccionado = u[0]
        self.en_buscar.delete(0, 'end'); self.en_buscar.insert(0, f"{u[1]} {u[2]}")
        self.lbl_nom.configure(text=f"{u[1]} {u[2]}", text_color="black")
        self.lbl_rol.configure(text=u[4])
        self.info.configure(fg_color="#DCFCE7")
        self.suggestions_frame.pack_forget()
        self.en_placa.focus()

    def guardar(self):
        if not self.usuario_id_seleccionado: return messagebox.showerror("Error", "Seleccione un propietario.")
        
        # Limpieza de datos
        p = self.en_placa.get().strip().upper()
        marca = self.cb_marca.get()
        mod = self.cb_mod.get()
        col = self.en_col.get()
        anio = self.en_anio.get()

        if len(p) != 7: return messagebox.showerror("Error", "La placa debe tener exactamente 7 caracteres.")
        if not col or not anio or marca=="Seleccionar Marca": return messagebox.showerror("Error", "Complete todos los campos.")
        
        if Consultas_vehiculos.registrar_vehiculo(marca, mod, col, p, anio, self.usuario_id_seleccionado):
            messagebox.showinfo("Éxito", "Vehículo registrado correctamente.")
            self.limpiar_form()

    def limpiar_form(self):
        self.usuario_id_seleccionado = None
        self.en_buscar.delete(0, 'end')
        self.lbl_nom.configure(text="Sin selección", text_color="gray")
        self.lbl_rol.configure(text="---", text_color="gray")
        self.info.configure(fg_color="#F3F4F6")
        
        self.en_placa.delete(0, 'end')
        self.en_col.delete(0, 'end')
        self.en_anio.delete(0, 'end')
        self.cb_marca.set("Seleccionar Marca")
        self.cb_mod.set("-")

    def verificar_preseleccion(self):
        d = self.controller.usuario_preseleccionado
        if d:
            self.controller.usuario_preseleccionado = None
            self.usuario_id_seleccionado = d['id']
            self.lbl_nom.configure(text=d['nombre'], text_color="black")
            self.lbl_rol.configure(text=f"Rol: {d['rol']} | ID: {d['id']}")
            self.info.configure(fg_color="#DCFCE7")
            self.en_buscar.insert(0, d['nombre'])
            self.en_placa.focus()

    def volver_menu(self): self.controller.show_frame(self.controller.vista_retorno)