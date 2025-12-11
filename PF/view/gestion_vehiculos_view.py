import customtkinter as ctk
from tkinter import messagebox
from model.vehiculos import Consultas_vehiculos

class GestionVehiculosView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F9FAFB")

        # HEADER
        self.header = ctk.CTkFrame(self, fg_color="white", height=80)
        self.header.pack(fill="x", padx=30, pady=30)
        ctk.CTkLabel(self.header, text="Gestión de Vehículos", font=("Arial", 24, "bold"), text_color="#111827").pack(side="left", padx=20)
        
        ctk.CTkButton(self.header, text="Volver al Menú", fg_color="white", text_color="black", border_color="#E5E7EB", border_width=1, command=self.volver).pack(side="right", padx=20)
        
        # Botón Nuevo Vehículo
        ctk.CTkButton(self.header, text="+ Nuevo Vehículo", fg_color="#2B7FFF", font=("Arial", 14, "bold"), command=self.ir_registro).pack(side="right", padx=10)

        # CONTENIDO
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="both", expand=True, padx=30, pady=10)

        # BUSCADOR
        search_bar = ctk.CTkFrame(self.content, fg_color="white", corner_radius=10)
        search_bar.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(search_bar, text="🔍 Buscar:", text_color="gray").pack(side="left", padx=15, pady=10)
        self.entry_search = ctk.CTkEntry(search_bar, placeholder_text="Placa, Marca, Propietario...", width=300, border_width=0, fg_color="#F3F4F6", text_color="black")
        self.entry_search.pack(side="left", fill="x", expand=True, padx=(0, 15), pady=10)
        
        self.entry_search.bind("<KeyRelease>", self.filtrar_tabla)

        # TABLA SCROLLABLE
        self.table_frame = ctk.CTkScrollableFrame(self.content, fg_color="transparent")
        self.table_frame.pack(fill="both", expand=True)
        
        self.cargar_datos()

    def filtrar_tabla(self, event):
        texto = self.entry_search.get()
        self.cargar_datos(filtro=texto)

    def cargar_datos(self, filtro=""):
        for widget in self.table_frame.winfo_children(): widget.destroy()
        
        # Headers
        h_frame = ctk.CTkFrame(self.table_frame, fg_color="#F3F4F6", height=40)
        h_frame.pack(fill="x")
        headers = ["Placa", "Marca", "Modelo", "Propietario", "Acciones"]
        for h in headers:
            w = 150 if h=="Propietario" else 100
            ctk.CTkLabel(h_frame, text=h, font=("Arial", 12, "bold"), text_color="gray", width=w, anchor="w").pack(side="left", padx=10, pady=10)

        datos = Consultas_vehiculos.obtener_todos_detallado()
        
        for vid, placa, marca, modelo, dueno in datos:
            # LÓGICA DE FILTRADO EN MEMORIA
            if filtro:
                b = filtro.lower()
                # Si no coincide con nada, saltar
                if (b not in placa.lower() and 
                    b not in marca.lower() and 
                    b not in modelo.lower() and 
                    b not in dueno.lower()):
                    continue

            # Render Fila
            row = ctk.CTkFrame(self.table_frame, fg_color="white", height=50)
            row.pack(fill="x", pady=1)
            
            ctk.CTkLabel(row, text=placa, width=100, anchor="w", text_color="black", font=("Courier", 14, "bold")).pack(side="left", padx=10)
            ctk.CTkLabel(row, text=marca, width=100, anchor="w", text_color="black").pack(side="left", padx=10)
            ctk.CTkLabel(row, text=modelo, width=100, anchor="w", text_color="black").pack(side="left", padx=10)
            ctk.CTkLabel(row, text=dueno, width=200, anchor="w", text_color="black").pack(side="left", padx=10)
            
            ctk.CTkButton(row, text="Eliminar", fg_color="#FEE2E2", text_color="#DC2626", width=80, height=28, hover_color="#FECACA",
                          command=lambda id=vid: self.eliminar(id)).pack(side="left", padx=10)

    def eliminar(self, vid):
        if messagebox.askyesno("Confirmar", "¿Eliminar este vehículo permanentemente?"):
            if Consultas_vehiculos.eliminar_vehiculo(vid):
                self.cargar_datos(self.entry_search.get())

    def ir_registro(self):
        self.controller.show_frame("RegistrarVehiculo")

    def volver(self):
        self.controller.show_frame(self.controller.vista_retorno)