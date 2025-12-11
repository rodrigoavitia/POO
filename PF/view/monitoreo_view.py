import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time
import random
from datetime import datetime

class MonitoreoView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F9FAFB")
        
        self.simulating = True
        self.paso_simulacion = 0
        
        self.after(0, self.cargar_ui)

    def cargar_ui(self):
        # 1. HEADER
        self.header = ctk.CTkFrame(self, fg_color="white", height=80)
        self.header.pack(fill="x")
        
        title_box = ctk.CTkFrame(self.header, fg_color="transparent")
        title_box.pack(side="left", padx=30, pady=15)
        ctk.CTkLabel(title_box, text="Sistema V.E.R.A. - Centro de Comando", font=("Arial", 20, "bold"), text_color="#101828").pack(anchor="w")
        ctk.CTkLabel(title_box, text="Monitoreo en Tiempo Real con IA (Simulación)", font=("Arial", 14), text_color="gray").pack(anchor="w")

        self.btn_volver = ctk.CTkButton(self.header, text="Salir", fg_color="#F3F4F6", text_color="black", border_width=1, border_color="#E5E7EB", command=self.volver)
        self.btn_volver.pack(side="right", padx=30)

        # 2. LAYOUT PRINCIPAL
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="both", expand=True, padx=20, pady=20)
        self.content.columnconfigure(0, weight=3); self.content.columnconfigure(1, weight=1)

        # IZQUIERDA: VIDEO + DASHBOARD
        self.left_panel = ctk.CTkFrame(self.content, fg_color="transparent")
        self.left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        # Video Frame
        self.video_frame = ctk.CTkFrame(self.left_panel, fg_color="black", corner_radius=12, height=400)
        self.video_frame.pack(fill="x", pady=(0, 15))
        self.video_frame.pack_propagate(False)

        # Label para la imagen
        self.lbl_video = ctk.CTkLabel(self.video_frame, text="Cargando feed...", text_color="white")
        self.lbl_video.place(relx=0.5, rely=0.5, anchor="center")
    
        self.cargar_imagen_estatica()

        # Overlays
        self.badge_live = ctk.CTkFrame(self.video_frame, fg_color="#B91C1C", corner_radius=4, height=25, width=80)
        self.badge_live.place(x=20, y=20)
        ctk.CTkLabel(self.badge_live, text="● EN VIVO", text_color="white", font=("Arial", 11, "bold")).place(relx=0.5, rely=0.5, anchor="center")

        self.scan_frame = ctk.CTkFrame(self.video_frame, fg_color="transparent", border_color="#00FF00", border_width=3, width=250, height=100)
        self.scan_frame.place(relx=0.5, rely=0.7, anchor="center")
        self.lbl_scan_text = ctk.CTkLabel(self.scan_frame, text="ESCANEANDO...", text_color="#00FF00", bg_color="black", font=("Arial", 10, "bold"))
        self.lbl_scan_text.place(relx=0.5, y=-10, anchor="s")

        # Dashboard Inferior
        self.dashboard_frame = ctk.CTkFrame(self.left_panel, fg_color="white", corner_radius=12, border_color="#E5E7EB", border_width=1)
        self.dashboard_frame.pack(fill="both", expand=True)
        
        self.metrics_box = ctk.CTkFrame(self.dashboard_frame, fg_color="transparent", width=200)
        self.metrics_box.pack(side="left", fill="y", padx=20, pady=20)
        
        ctk.CTkLabel(self.metrics_box, text="Métricas del Sistema", font=("Arial", 14, "bold"), text_color="black").pack(anchor="w", pady=(0,10))
        self.lbl_fps = self.crear_metrica(self.metrics_box, "FPS Camara:", "30.0")
        self.lbl_cpu = self.crear_metrica(self.metrics_box, "Uso CPU (IA):", "12%")
        self.lbl_conf = self.crear_metrica(self.metrics_box, "Confianza ANPR:", "---")

        self.console_box = ctk.CTkTextbox(self.dashboard_frame, fg_color="#FFFFFF", text_color="#000000", font=("Courier", 12), corner_radius=8)
        self.console_box.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        self.console_box.insert("0.0", "> Iniciando V.E.R.A...\n> Conectando BD... OK\n")

        # DERECHA: SIDEBAR
        self.sidebar = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12, border_color="#E5E7EB", border_width=1)
        self.sidebar.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(self.sidebar, text="Última Detección", font=("Arial", 16, "bold"), text_color="#101828").pack(pady=(20, 10), padx=20, anchor="w")
        self.card_resultado = ctk.CTkFrame(self.sidebar, fg_color="#F9FAFB", border_color="gray", border_width=2, corner_radius=8)
        self.card_resultado.pack(fill="x", padx=20, pady=10)
        
        self.lbl_placa_res = ctk.CTkLabel(self.card_resultado, text="---", font=("Courier", 24, "bold"), text_color="#101828")
        self.lbl_placa_res.pack(pady=(15, 5))
        self.lbl_estado_res = ctk.CTkLabel(self.card_resultado, text="ESPERANDO...", font=("Arial", 14, "bold"), text_color="gray")
        self.lbl_estado_res.pack(pady=(0, 15))
        
        self.info_box = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.info_box.pack(fill="x", padx=20, pady=20)
        self.lbl_prop_val = self.crear_dato(self.info_box, "Propietario:", "---")
        self.lbl_rol_val = self.crear_dato(self.info_box, "Rol:", "---")
        self.lbl_veh_val = self.crear_dato(self.info_box, "Vehículo:", "---")

        self.actualizar_dashboard()
        self.simular_proceso()

    def crear_metrica(self, parent, label, valor):
        f = ctk.CTkFrame(parent, fg_color="transparent")
        f.pack(fill="x", pady=2)
        ctk.CTkLabel(f, text=label, font=("Arial", 12), text_color="gray").pack(side="left")
        lbl = ctk.CTkLabel(f, text=valor, font=("Arial", 12, "bold"), text_color="#101828")
        lbl.pack(side="right")
        return lbl

    def crear_dato(self, parent, label, valor):
        f = ctk.CTkFrame(parent, fg_color="transparent")
        f.pack(fill="x", pady=5)
        ctk.CTkLabel(f, text=label, font=("Arial", 12, "bold"), text_color="gray").pack(side="left")
        lbl = ctk.CTkLabel(f, text=valor, font=("Arial", 12), text_color="black")
        lbl.pack(side="right")
        return lbl

    def log(self, mensaje):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console_box.insert("end", f"[{timestamp}] {mensaje}\n")
        self.console_box.see("end")

    def cargar_imagen_estatica(self):
        try:
            ruta = os.path.join("view", "camara_demo.jpg") 
            pil_img = Image.open(ruta)
            ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(800, 400))
            self.lbl_video.configure(image=ctk_img, text="")
        except:
            self.lbl_video.configure(text="[FALTA IMAGEN view/camara_demo.jpg]", text_color="red")

    # SIMULACIÓN 
    def actualizar_dashboard(self):
        if not self.simulating: return
        fps = random.randint(28, 32)
        self.lbl_fps.configure(text=f"{fps} FPS")
        cpu = random.randint(10, 25)
        self.lbl_cpu.configure(text=f"{cpu}%")
        self.after(800, self.actualizar_dashboard)

    def simular_proceso(self):
        """Ciclo infinito de simulación"""
        if not self.simulating: return

        if self.paso_simulacion == 0:
            self.scan_frame.configure(border_color="#FDC700") 
            self.lbl_scan_text.configure(text="ESCANEANDO...", text_color="#FDC700")
            
            self.lbl_placa_res.configure(text="...")
            self.lbl_estado_res.configure(text="PROCESANDO...", text_color="gray")
            self.card_resultado.configure(fg_color="#F9FAFB", border_color="gray")
            
            self.lbl_prop_val.configure(text="---")
            self.lbl_rol_val.configure(text="---")
            self.lbl_veh_val.configure(text="---")
            self.lbl_conf.configure(text="---")

            self.paso_simulacion = 1
            self.after(2500, self.simular_proceso)

        elif self.paso_simulacion == 1: # DETECTADO
            self.scan_frame.configure(border_color="#10B981")
            self.lbl_scan_text.configure(text="DETECTADO", text_color="#10B981")
            
            self.lbl_placa_res.configure(text="GFY-509-C")
            self.lbl_estado_res.configure(text="ACCESO AUTORIZADO", text_color="#15803D")
            self.card_resultado.configure(fg_color="#F0FDF4", border_color="#10B981")
            
            self.lbl_prop_val.configure(text="Juan Pérez")
            self.lbl_rol_val.configure(text="Docente")
            self.lbl_veh_val.configure(text="Toyota Corolla")
            
            conf = random.randint(95, 99)
            self.lbl_conf.configure(text=f"{conf}.{random.randint(0,9)}%")
            
            self.log("Objeto detectado: Vehículo")
            self.log(f"OCR Resultado: GFY-509-C (Conf: 0.{conf})")
            self.log(">> ACCESO CONCEDIDO <<")

            self.paso_simulacion = 0
            self.after(4000, self.simular_proceso)

    def volver(self):
        self.simulating = False
        self.controller.show_frame("SudoteView")

""""
Por el momento solo haremos la simulación debido a la falta de recolección 
de datos y de inversión economica
"""
