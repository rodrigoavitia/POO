import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
from tkcalendar import Calendar
from model.imagenes import Consultas_reportes 

class ReportesView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F9FAFB")

        # CONTENEDOR PRINCIPAL
        self.main_card = ctk.CTkFrame(self, fg_color="white", corner_radius=14, border_color="#E5E7EB", border_width=1)
        self.main_card.pack(fill="both", expand=True, padx=32, pady=32)

        # Header
        self.header = ctk.CTkFrame(self.main_card, fg_color="transparent", height=80)
        self.header.pack(fill="x", padx=24, pady=(20, 0))
        ctk.CTkLabel(self.header, text="📄 Sistema de Reportes", font=("Arial", 24, "bold"), text_color="#0A0A0A").pack(side="left")
        ctk.CTkButton(self.header, text="Volver", fg_color="white", text_color="#0A0A0A", border_color="#E5E7EB", border_width=1, width=80, command=self.volver).pack(side="right")
        ctk.CTkFrame(self.main_card, height=2, fg_color="#F3F4F6").pack(fill="x", pady=20)

        # BARRA DE FILTROS
        self.filters_frame = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.filters_frame.pack(fill="x", padx=24)

        # Fila 1: Búsqueda General
        row1 = ctk.CTkFrame(self.filters_frame, fg_color="transparent")
        row1.pack(fill="x", pady=(0, 10))
        
        self.entry_search = ctk.CTkEntry(row1, placeholder_text="🔍 Buscar por Nombre, Placa...", width=300, fg_color="#F9FAFB", text_color="black")
        self.entry_search.pack(side="left", padx=(0, 10))
        self.entry_search.bind("<Return>", self.realizar_busqueda)
        self.entry_search.bind("<KeyRelease>", self.realizar_busqueda) 
        
        self.cb_filtro_rol = ctk.CTkComboBox(row1, values=["Todos", "Estudiante", "Docente", "Administrativo", "Trabajador"], width=150, fg_color="white", text_color="black", command=self.realizar_busqueda)
        self.cb_filtro_rol.set("Todos")
        self.cb_filtro_rol.pack(side="left", padx=10)

        # Fila 2: Filtros de Fecha
        row2 = ctk.CTkFrame(self.filters_frame, fg_color="transparent")
        row2.pack(fill="x", pady=(0, 10))

        # Fecha Desde
        ctk.CTkLabel(row2, text="Desde:", text_color="gray").pack(side="left", padx=(0, 5))
        self.entry_fecha_ini = ctk.CTkEntry(row2, placeholder_text="AAAA-MM-DD", width=100, fg_color="#F9FAFB", text_color="black")
        self.entry_fecha_ini.pack(side="left")
        ctk.CTkButton(row2, text="📅", width=30, fg_color="#E5E7EB", text_color="black", hover_color="#D1D5DB", command=lambda: self.abrir_calendario(self.entry_fecha_ini)).pack(side="left", padx=(2, 15))

        # Fecha Hasta
        ctk.CTkLabel(row2, text="Hasta:", text_color="gray").pack(side="left", padx=(0, 5))
        self.entry_fecha_fin = ctk.CTkEntry(row2, placeholder_text="AAAA-MM-DD", width=100, fg_color="#F9FAFB", text_color="black")
        self.entry_fecha_fin.pack(side="left")
        ctk.CTkButton(row2, text="📅", width=30, fg_color="#E5E7EB", text_color="black", hover_color="#D1D5DB", command=lambda: self.abrir_calendario(self.entry_fecha_fin)).pack(side="left", padx=(2, 20))

        # Botón Limpiar
        ctk.CTkButton(row2, text="Limpiar Filtros", width=100, fg_color="#F3F4F6", text_color="black", hover_color="#E5E7EB", command=self.limpiar_filtros).pack(side="left", padx=10)

        # TABLA DE DATOS
        self.lbl_resultados = ctk.CTkLabel(self.main_card, text="Resultados: 0", font=("Arial", 12, "bold"), text_color="gray")
        self.lbl_resultados.pack(anchor="w", padx=24, pady=(10, 5))

        header_cols = ["Fecha", "Nombre", "Rol", "ID", "Placa", "Espacio", "Entrada", "Salida", "Tipo", ""]
        self.widths = [90, 180, 100, 60, 90, 70, 70, 70, 90, 60]
        
        self.table_header = ctk.CTkFrame(self.main_card, fg_color="#F9FAFB", height=35, corner_radius=0)
        self.table_header.pack(fill="x", padx=24)
        for i, col in enumerate(header_cols):
            ctk.CTkLabel(self.table_header, text=col, font=("Arial", 12, "bold"), text_color="#334155", anchor="w", width=self.widths[i]).pack(side="left", padx=5)

        self.table_body = ctk.CTkScrollableFrame(self.main_card, fg_color="transparent", height=350)
        self.table_body.pack(fill="both", expand=True, padx=24, pady=(0, 24))

        self.realizar_busqueda(None)

    # FUNCIONES
    def abrir_calendario(self, entry_target):
        top = ctk.CTkToplevel(self)
        top.title("Seleccionar Fecha")
        top.geometry("300x250")
        top.grab_set()
        
        cal = Calendar(top, selectmode='day', locale='es_ES', date_pattern='y-mm-dd')
        cal.pack(pady=20, padx=20, fill="both", expand=True)

        def seleccionar():
            fecha = cal.get_date()
            entry_target.delete(0, 'end')
            entry_target.insert(0, fecha)
            self.realizar_busqueda(None)
            top.destroy()

        ctk.CTkButton(top, text="Seleccionar", command=seleccionar).pack(pady=10)

    def realizar_busqueda(self, event):
        termino = self.entry_search.get()
        rol = self.cb_filtro_rol.get()
        f_ini = self.entry_fecha_ini.get()
        f_fin = self.entry_fecha_fin.get()
        
        for widget in self.table_body.winfo_children(): widget.destroy()
            
        resultados = Consultas_reportes.buscar_reportes(termino, rol, f_ini, f_fin)
        self.lbl_resultados.configure(text=f"Resultados: {len(resultados)}")
        
        for fila_datos in resultados:
            self.crear_fila(fila_datos)

    def crear_fila(self, datos):
        id_reporte = datos[-1]
        datos_visuales = datos[:-1]

        row = ctk.CTkFrame(self.table_body, fg_color="transparent", height=45)
        row.pack(fill="x", pady=2)
        ctk.CTkFrame(row, height=1, fg_color="#E5E7EB").pack(side="bottom", fill="x")

        for i, dato in enumerate(datos_visuales):
            if i == 2: # Rol con color para mas sabor
                bg = "#E0E7FF" if "Estudiante" in str(dato) else "#DCFCE7" if "Docente" in str(dato) else "#F3F4F6"
                fg = "#3730A3" if "Estudiante" in str(dato) else "#166534"
                lbl = ctk.CTkLabel(row, text=str(dato), font=("Arial", 11, "bold"), text_color=fg, fg_color=bg, corner_radius=5, width=self.widths[i])
                lbl.pack(side="left", padx=5)
            else:
                ctk.CTkLabel(row, text=str(dato), font=("Arial", 12), text_color="#0A0A0A", anchor="w", width=self.widths[i]).pack(side="left", padx=5)
        
        ctk.CTkButton(row, text="Ver", width=50, height=25, fg_color="#3B82F6", hover_color="#2563EB", 
                      command=lambda id=id_reporte: self.ver_detalle(id)).pack(side="left", padx=5)

    def ver_detalle(self, id_reporte):
        datos = Consultas_reportes.obtener_detalle(id_reporte)
        if not datos: return

        img_blob, fecha, hora, tipo, placa, modelo, color, nombre, rol = datos
        
        top = ctk.CTkToplevel(self)
        top.geometry("600x400")
        top.title(f"Detalle #{id_reporte}")
        top.configure(fg_color="white")
        top.grab_set()

        img_frame = ctk.CTkFrame(top, width=300, fg_color="#F3F4F6")
        img_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        img_frame.pack_propagate(False)
        
        try:
            if img_blob:
                pil_img = Image.open(io.BytesIO(img_blob))
                ctk_img = ctk.CTkImage(light_image=pil_img, size=(280, 200))
                ctk.CTkLabel(img_frame, text="", image=ctk_img).pack(expand=True)
            else:
                ctk.CTkLabel(img_frame, text="Sin Imagen", text_color="gray").pack(expand=True)
        except:
            ctk.CTkLabel(img_frame, text="Error Imagen", text_color="red").pack(expand=True)

        info = ctk.CTkFrame(top, fg_color="transparent")
        info.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        color_tipo = "#16A34A" if tipo == "Entrada" else "#DC2626"
        ctk.CTkLabel(info, text=f"● {tipo}", font=("Arial", 16, "bold"), text_color=color_tipo).pack(anchor="w", pady=(0, 10))
        
        for k, v in [("Fecha:", f"{fecha} {hora}"), ("Conductor:", nombre), ("Rol:", rol), ("Vehículo:", f"{modelo} {color}")] :
            f = ctk.CTkFrame(info, fg_color="transparent")
            f.pack(fill="x", pady=2)
            ctk.CTkLabel(f, text=k, font=("Arial", 12, "bold"), text_color="#64748B", width=80, anchor="w").pack(side="left")
            ctk.CTkLabel(f, text=str(v), font=("Arial", 12), text_color="black", anchor="w").pack(side="left")

        ctk.CTkFrame(info, height=2, fg_color="#E5E7EB").pack(fill="x", pady=15)
        ctk.CTkLabel(info, text=placa, font=("Courier", 24, "bold"), text_color="black").pack()
        ctk.CTkLabel(info, text="Placa Detectada", font=("Arial", 10), text_color="gray").pack()

    def limpiar_filtros(self):
        self.entry_search.delete(0, 'end')
        self.entry_fecha_ini.delete(0, 'end')
        self.entry_fecha_fin.delete(0, 'end')
        self.cb_filtro_rol.set("Todos")
        self.realizar_busqueda(None)

    def volver(self):
        self.controller.show_frame(self.controller.vista_retorno)