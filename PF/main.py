import customtkinter as ctk
from tkinter import messagebox

""""
En lugar de utilizar el patrón estricto Modelo-Vista-Controlador (MVC), 
donde cada vista tendría su propio archivo de controlador dedicado, se optó por el patrón
Modelo-Vista (MV). Esto significa que las Vistas (view/*.py) contienen su propia lógica de eventos
(por ejemplo, qué hace un botón), y main.py se encarga de la coordinación de alto nivel entre ellas,
 reduciendo la complejidad de la herencia y el paso de parámetros entre múltiples archivos
 de controlador pequeños.
 
"""
# IMPORTACIÓN DE TODAS LAS VISTAS
from view.login_view import LoginView
from view.sudote_view import SudoteView
from view.sudito_view import SuditoView
from view.registrar_vehiculo import RegistrarVehiculo
from view.reportes_view import ReportesView  
from view.monitoreo_view import MonitoreoView
from view.splash_view import SplashView
from view.exit_view import ExitView
from view.gestion_usuarios_view import GestionUsuariosView
from view.gestion_vehiculos_view import GestionVehiculosView

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema V.E.R.A. | Control de Acceso")
        
        # Maximizar ventana (Windows)
        self.after(0, lambda: self.state('zoomed'))
        
        # Protocolo para cierre seguro
        self.protocol("WM_DELETE_WINDOW", self.confirmar_cierre)
        
        # Variables de estado compartidas
        self.vista_retorno = "LoginView" 
        self.usuario_preseleccionado = None 
        self.rol_actual = None 

        # Contenedor Principal
        self.container = ctk.CTkFrame(self, fg_color="#F3F4F6")
        self.container.pack(side="top", fill="both", expand=True)
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Lista de todas las pantallas a cargar
        lista_vistas = (
            SplashView, ExitView, LoginView, SudoteView, SuditoView, 
            RegistrarVehiculo, ReportesView, MonitoreoView,
            GestionUsuariosView, GestionVehiculosView
        )
        for F in lista_vistas:
            page_name = F.__name__
            try:
                frame = F(master=self.container, controller=self)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
            except Exception as e:
                print(f"ERROR CRÍTICO al cargar la vista {page_name}: {e}")

        # Iniciar con la pantalla de carga
        self.show_frame("SplashView")

    def show_frame(self, page_name):
        """Trae al frente la vista solicitada y ejecuta lógica de inicio."""
        
        if page_name not in self.frames:
            print(f"Error: La vista '{page_name}' no fue cargada o no existe.")
            return

        frame = self.frames[page_name]
        
        # 1. Registrar Vehículo: Verificar si venimos de crear un usuario
        if page_name == "RegistrarVehiculo":
            if hasattr(frame, 'verificar_preseleccion'):
                frame.verificar_preseleccion()

        # 2. Monitoreo: Iniciar simulación o cámara
        if page_name == "MonitoreoView":
            # Si es versión simulada (Demo)
            if hasattr(frame, 'simulating'):
                frame.simulating = True
                if hasattr(frame, 'actualizar_dashboard'): frame.actualizar_dashboard()
                if hasattr(frame, 'simular_proceso'): frame.simular_proceso()
            # Si es versión real
            elif hasattr(frame, 'start_monitoring'):
                frame.start_monitoring()
                
        # 3. Reportes: Recargar búsqueda
        if page_name == "ReportesView":
             if hasattr(frame, 'realizar_busqueda'):
                 frame.realizar_busqueda(None)

        # 4. Listas de Gestión: Recargar datos de la BD para ver registrados
        if page_name == "GestionUsuariosView":
            if hasattr(frame, 'cargar_datos_tabla'): frame.cargar_datos_tabla()
            elif hasattr(frame, 'cargar_datos'): frame.cargar_datos()

        if page_name == "GestionVehiculosView":
            if hasattr(frame, 'cargar_datos'): frame.cargar_datos()

        frame.tkraise()

    def confirmar_cierre(self):
        """Maneja el cierre de la aplicación de forma segura."""
        respuesta = messagebox.askyesno("Salir del Sistema", "¿Estás seguro de que deseas salir?")
        
        if respuesta:
            # Detener procesos de Monitoreo de forma segura
            if "MonitoreoView" in self.frames:
                monitor = self.frames["MonitoreoView"]
                
                # Detener Simulación
                if hasattr(monitor, 'simulating'):
                    monitor.simulating = False
                
                # Detener Cámara Real (Camara eliminada para la presentacion)
                if hasattr(monitor, 'camera') and monitor.camera and hasattr(monitor.camera, 'isOpened') and monitor.camera.isOpened():
                    monitor.camera.release()
                if hasattr(monitor, 'stop_camera_safe'):
                    monitor.stop_camera_safe()
                
                # Variable de control
                if hasattr(monitor, 'running'):
                    monitor.running = False
            
            # Mostrar pantalla de salida
            if "ExitView" in self.frames:
                frame_salida = self.frames["ExitView"]
                frame_salida.tkraise()
                if hasattr(frame_salida, 'iniciar_salida'):
                    frame_salida.iniciar_salida()
            else:
                self.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

