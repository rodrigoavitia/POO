import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os

class SudoteView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F3F4F6")

        # SIDEBAR
        self.sidebar = ctk.CTkFrame(self, width=260, fg_color="white", corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo y Título
        ctk.CTkLabel(self.sidebar, text="Búfalos UTD", font=("Arial", 22, "bold"), text_color="#111827").pack(pady=(30, 5), padx=20, anchor="w")
        ctk.CTkLabel(self.sidebar, text="Super Administrador", font=("Arial", 12), text_color="gray").pack(padx=20, anchor="w")
        ctk.CTkFrame(self.sidebar, height=2, fg_color="#E5E7EB").pack(fill="x", pady=20)

        # MENÚ DE NAVEGACIÓN
        self.crear_boton_menu("Panel de Control", "📊", activo=True)
        self.crear_boton_menu("Vehículos", "🚗", comando=lambda: self.controller.show_frame("GestionVehiculosView"))
        #SudoteView y SuditoView:
        self.crear_boton_menu("Usuarios", "👥", comando=lambda: self.controller.show_frame("GestionUsuariosView"))
        self.crear_boton_menu("Monitoreo en Vivo", "📹", comando=lambda: self.controller.show_frame("MonitoreoView"))
        self.crear_boton_menu("Reportes", "📄", comando=lambda: self.controller.show_frame("ReportesView"))

        # Logout
        self.btn_logout = ctk.CTkButton(self.sidebar, text="Cerrar Sesión", fg_color="#FEF2F2", text_color="#DC2626", hover_color="#FEE2E2", command=self.logout)
        self.btn_logout.pack(side="bottom", fill="x", padx=20, pady=30)

        # ÁREA PRINCIPAL 
        self.main_area = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_area.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(self.main_area, text="Dashboard - Sistema V.E.R.A.", font=("Arial", 24, "bold"), text_color="#111827").pack(anchor="w")
        ctk.CTkLabel(self.main_area, text="Vista general del estacionamiento institucional", font=("Arial", 14), text_color="gray").pack(anchor="w", pady=(0, 20))

        # 1. TARJETAS KPI
        self.kpi_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.kpi_frame.pack(fill="x", pady=(0, 20))
        
        # Vehículos Hoy 
        self.crear_kpi(self.kpi_frame, "Vehículos Hoy", "820", "+12% vs ayer", "#2B7FFF", "#EFF6FF")
        # Usuarios Activos)
        self.crear_kpi(self.kpi_frame, "Usuarios Activos", "1,200", "Total registrados", "#AD46FF", "#FAF5FF")
        # Ocupación
        self.crear_kpi(self.kpi_frame, "Ocupación", "78%", "Cerca del límite", "#F97316", "#FFF7ED")

        # 2. GRÁFICAS DE BARRAS (Fila Central)
        self.charts_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.charts_frame.pack(fill="x", pady=10)
        self.charts_frame.columnconfigure(0, weight=1)
        self.charts_frame.columnconfigure(1, weight=1)

        # Gráfica 1: Registro Mensual
        self.crear_grafica_barras(self.charts_frame, 0, "Registro Mensual", 
                                  ["Estudiantes", "Profesores", "Admin", "Trabajadores"], 
                                  [0.8, 0.5, 0.3, 0.2])
        
        # Gráfica 2: Ocupación por Zona
        self.crear_grafica_barras(self.charts_frame, 1, "Ocupación por Zona", 
                                  ["Zona A", "Zona B", "Zona C", "Zona D"], 
                                  [0.85, 0.70, 0.92, 0.65], 
                                  colores=["#3B82F6", "#8B5CF6", "#EC4899", "#F59E0B"])

        # 3. ACTIVIDAD RECIENTE (Fila Inferior)
        self.crear_actividad_reciente(self.main_area)

    # HELPERS VISUALES 
    def crear_boton_menu(self, texto, icono, comando=None, activo=False):
        color = "#1F2937" if activo else "transparent"
        text_c = "white" if activo else "#4B5563"
        hover = "#374151" if activo else "#F3F4F6"
        btn = ctk.CTkButton(self.sidebar, text=f"  {icono}  {texto}", anchor="w", fg_color=color, text_color=text_c, hover_color=hover, height=45, corner_radius=8, command=comando)
        btn.pack(fill="x", padx=15, pady=5)

    def crear_kpi(self, parent, titulo, valor, sub, color_borde, color_bg):
        card = ctk.CTkFrame(parent, fg_color="white", corner_radius=12, border_color=color_borde, border_width=2)
        card.pack(side="left", fill="x", expand=True, padx=10)
        
        ctk.CTkLabel(card, text=titulo, font=("Arial", 13, "bold"), text_color="gray").pack(anchor="w", padx=20, pady=(15, 0))
        ctk.CTkLabel(card, text=valor, font=("Arial", 32, "bold"), text_color="#111827").pack(anchor="w", padx=20, pady=(5, 0))
        
        badge = ctk.CTkFrame(card, fg_color=color_bg, corner_radius=6, height=25)
        badge.pack(anchor="w", padx=20, pady=(5, 15))
        ctk.CTkLabel(badge, text=sub, font=("Arial", 11, "bold"), text_color=color_borde).pack(padx=8, pady=2)

    def crear_grafica_barras(self, parent, col, titulo, labels, valores, colores=None):
        frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=12)
        frame.grid(row=0, column=col, sticky="nsew", padx=10)
        
        ctk.CTkLabel(frame, text=titulo, font=("Arial", 16, "bold"), text_color="#111827").pack(anchor="w", padx=20, pady=20)
        
        for i, (lbl, val) in enumerate(zip(labels, valores)):
            row = ctk.CTkFrame(frame, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=8)
            
            info = ctk.CTkFrame(row, fg_color="transparent")
            info.pack(fill="x")
            ctk.CTkLabel(info, text=lbl, font=("Arial", 12), text_color="#4B5563").pack(side="left")
            ctk.CTkLabel(info, text=f"{int(val*100)}%", font=("Arial", 12, "bold"), text_color="#111827").pack(side="right")
            
            color = colores[i] if colores else "#3B82F6"
            progress = ctk.CTkProgressBar(row, height=10, corner_radius=5, progress_color=color)
            progress.set(val)
            progress.pack(fill="x", pady=(5, 0))

    def crear_actividad_reciente(self, parent):
        frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=12)
        frame.pack(fill="x", pady=20, padx=10)
        
        ctk.CTkLabel(frame, text="Actividad Reciente", font=("Arial", 16, "bold"), text_color="#111827").pack(anchor="w", padx=20, pady=20)
        
        datos = [
            ("09:45", "Juan Pérez", "ABC-123 - Zona A", "Entrada", "#DCFCE7", "#166534"),
            ("09:42", "María Gzz", "XYZ-789 - Zona B", "Salida", "#DBEAFE", "#1E40AF"),
            ("09:38", "Roberto T.", "MNO-456 - Zona C", "Entrada", "#DCFCE7", "#166534"),
        ]
        
        for hora, nombre, detalle, tipo, bg, fg in datos:
            row = ctk.CTkFrame(frame, fg_color="#F9FAFB", corner_radius=8, height=50)
            row.pack(fill="x", padx=20, pady=5)
            
            ctk.CTkLabel(row, text=hora, font=("Arial", 12, "bold"), text_color="gray", width=60).pack(side="left", padx=10)
            
            info = ctk.CTkFrame(row, fg_color="transparent")
            info.pack(side="left", fill="x", expand=True)
            ctk.CTkLabel(info, text=nombre, font=("Arial", 13, "bold"), text_color="#111827").pack(anchor="w")
            ctk.CTkLabel(info, text=detalle, font=("Arial", 11), text_color="gray").pack(anchor="w")
            
            badge = ctk.CTkFrame(row, fg_color=bg, corner_radius=6, width=80, height=25)
            badge.pack(side="right", padx=15)
            badge.pack_propagate(False)
            ctk.CTkLabel(badge, text=tipo, font=("Arial", 11, "bold"), text_color=fg).place(relx=0.5, rely=0.5, anchor="center")

    def logout(self):
        if messagebox.askyesno("Salir", "¿Cerrar Sesión?"):
            self.controller.show_frame("LoginView")