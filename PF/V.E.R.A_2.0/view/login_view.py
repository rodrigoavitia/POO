import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
from model.usuarios import Consulta_usuarios 

class LoginView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.contrasena_es_visible = False
        self.configure(fg_color="#F3F4F6") 

        # Card Central
        self.card = ctk.CTkFrame(self, fg_color="white", width=450, height=620, corner_radius=20)
        self.card.place(relx=0.5, rely=0.5, anchor="center")
        self.card.grid_propagate(False); self.card.pack_propagate(False)

        # Logo
        try:
            ruta = os.path.join("view", "logo_integradora.png")
            img = ctk.CTkImage(Image.open(ruta), size=(140, 140))
            ctk.CTkLabel(self.card, text="", image=img).pack(pady=(40, 10))
        except:
            ctk.CTkLabel(self.card, text="[LOGO V.E.R.A.]", font=("Arial", 20, "bold"), text_color="#0092B8").pack(pady=(40, 10))

        ctk.CTkLabel(self.card, text="Bienvenido", font=("Arial", 28, "bold"), text_color="#0F172B").pack(pady=5)
        ctk.CTkLabel(self.card, text="Sistema de Vigilancia Élite\nde Reconocimiento de Acceso", font=("Arial", 15), text_color="#64748B", justify="center").pack(pady=(0, 30))

        # Inputs
        ctk.CTkLabel(self.card, text="Correo electrónico", font=("Arial", 14, "bold"), text_color="#334155", anchor="w").pack(fill="x", padx=45, pady=(0, 5))
        self.entry_user = ctk.CTkEntry(self.card, placeholder_text="usuario@vera.security", height=45, font=("Arial", 14), border_color="#94A3B8", border_width=2, corner_radius=8, fg_color="white", text_color="black")
        self.entry_user.pack(fill="x", padx=45, pady=(0, 20))

        ctk.CTkLabel(self.card, text="Contraseña", font=("Arial", 14, "bold"), text_color="#334155", anchor="w").pack(fill="x", padx=45, pady=(0, 5))
        self.pass_frame = ctk.CTkFrame(self.card, height=45, fg_color="white", border_color="#94A3B8", border_width=2, corner_radius=8)
        self.pass_frame.pack(fill="x", padx=45, pady=(0, 5))
        
        self.entry_pass = ctk.CTkEntry(self.pass_frame, show="•", height=40, border_width=0, fg_color="transparent", text_color="black", font=("Arial", 14), placeholder_text="••••••••")
        self.entry_pass.pack(side="left", fill="both", expand=True, padx=(10, 5), pady=2)
        
        self.btn_eye = ctk.CTkButton(self.pass_frame, text="👁", width=35, fg_color="transparent", text_color="#64748B", hover_color="#F1F5F9", font=("Arial", 18), command=self.toggle_pass)
        self.btn_eye.pack(side="right", padx=(0, 5), pady=2)

        ctk.CTkButton(self.card, text="Iniciar Sesión", height=50, fg_color="black", text_color="white", hover_color="#333333", font=("Arial", 16, "bold"), corner_radius=10, command=self.validar).pack(fill="x", padx=45, pady=(30, 20))

    def toggle_pass(self):
        if self.contrasena_es_visible:
            self.entry_pass.configure(show="•")
            self.btn_eye.configure(text="👁")
            self.contrasena_es_visible = False
        else:
            self.entry_pass.configure(show="")
            self.btn_eye.configure(text="Ø")
            self.contrasena_es_visible = True

    def validar(self):
        u = self.entry_user.get()
        p = self.entry_pass.get() # Obtenemos la contraseña plana
        
        # VALIDACIÓN ÚNICA CONTRA LA BD (El modelo se encarga de hashear y comparar)
        datos = Consulta_usuarios.login(u, p) 
        
        if datos:
            nombre, rol = datos
            print(f"Acceso Concedido: {nombre} ({rol})")
            
            # Guardar sesión en el controlador
            self.controller.rol_actual = rol 
            
            # Redirección según rol
            if "Sudote" in rol:
                self.controller.vista_retorno = "SudoteView"
                self.controller.show_frame("SudoteView")
            elif "Sudito" in rol or "Administrador" in rol:
                self.controller.vista_retorno = "SuditoView"
                self.controller.show_frame("SuditoView")
            else:
                messagebox.showerror("Acceso Restringido", "Este usuario no tiene permisos para acceder al sistema.")
                return

            self.limpiar()
        else:
            messagebox.showerror("Error de Autenticación", "Usuario o contraseña incorrectos.")

    def limpiar(self):
        self.entry_user.delete(0, 'end')
        self.entry_pass.delete(0, 'end')
        if self.contrasena_es_visible: self.toggle_pass()