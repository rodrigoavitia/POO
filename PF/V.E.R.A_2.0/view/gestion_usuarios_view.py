import customtkinter as ctk
from tkinter import messagebox
import re
from model.usuarios import Consulta_usuarios

# CLASE DE CONFIRMACION
class PasswordDialog(ctk.CTkToplevel):
    def __init__(self, title="Seguridad", text="Ingrese contraseña:"):
        super().__init__()
        self.title(title)
        self.geometry("320x180")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.password = None
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 320) // 2
        y = (self.winfo_screenheight() - 180) // 2
        self.geometry(f"+{x}+{y}")
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)
        ctk.CTkLabel(self.frame, text=text, font=("Arial", 13, "bold")).pack(pady=(0, 10))
        self.entry = ctk.CTkEntry(self.frame, show="*", width=200) 
        self.entry.pack(pady=5); self.entry.focus(); self.entry.bind("<Return>", self.on_ok)
        btn_frame = ctk.CTkFrame(self.frame, fg_color="transparent"); btn_frame.pack(pady=15)
        ctk.CTkButton(btn_frame, text="Cancelar", fg_color="gray", width=80, command=self.destroy).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Confirmar", width=80, command=self.on_ok).pack(side="left", padx=5)
        self.grab_set(); self.wait_window()
    def on_ok(self, event=None): self.password = self.entry.get(); self.destroy()
    def get_input(self): return self.password

class GestionUsuariosView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F9FAFB")
        
        self.id_edicion = None
        self.edit_data = {}
        self.filtro_txt_var = "" 

        # HEADER
        self.header = ctk.CTkFrame(self, fg_color="white", height=80)
        self.header.pack(fill="x", padx=30, pady=30)
        ctk.CTkLabel(self.header, text="Gestión de Usuarios", font=("Arial", 24, "bold"), text_color="#111827").pack(side="left", padx=20)
        ctk.CTkButton(self.header, text="Volver al Menú", fg_color="white", text_color="black", border_color="#E5E7EB", border_width=1, command=self.volver).pack(side="right", padx=20)

        # CONTENIDO
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="both", expand=True, padx=30, pady=(0, 20))

        # TABS
        self.tabs_container = ctk.CTkFrame(self.content, fg_color="transparent")
        self.tabs_container.pack(fill="x", pady=(0, 15))
        
        self.btn_tab_lista = ctk.CTkButton(self.tabs_container, text="📋 Lista de Usuarios", fg_color="#101828", text_color="white", width=150, height=40, command=self.mostrar_lista)
        self.btn_tab_lista.pack(side="left", padx=(0, 10))
        
        # Botón Agregar
        self.btn_tab_agregar = ctk.CTkButton(self.tabs_container, text="+ Agregar Usuario", fg_color="white", text_color="#0A0A0A", border_color="#E5E7EB", border_width=1, width=150, height=40, command=self.mostrar_formulario)
        self.btn_tab_agregar.pack(side="left")

        # DINÁMICO
        self.dynamic_frame = ctk.CTkFrame(self.content, fg_color="white", corner_radius=10)
        self.dynamic_frame.pack(fill="both", expand=True)

        self.mostrar_lista()

    # PESTAÑAS
    def mostrar_lista(self):
        self.btn_tab_lista.configure(fg_color="#101828", text_color="white", border_width=0)
        self.btn_tab_agregar.configure(fg_color="white", text_color="#0A0A0A", border_width=1)
        for w in self.dynamic_frame.winfo_children(): w.destroy()
        
        self.render_filtros()
        self.render_tabla()
        self.cargar_datos_tabla()

    
    def mostrar_formulario(self, limpiar=True):
        if limpiar:
            self.id_edicion = None
            self.edit_data = {}
        
        self.lbl_total = None; self.rows_frame = None
        
        self.btn_tab_lista.configure(fg_color="white", text_color="#0A0A0A", border_width=1)
        self.btn_tab_agregar.configure(fg_color="#10B981", text_color="white", border_width=0)
        for w in self.dynamic_frame.winfo_children(): w.destroy()
        self.cargar_formulario_ui()

    def cargar_datos(self):
        if hasattr(self, 'rows_frame') and self.rows_frame.winfo_exists():
            self.cargar_datos_tabla()
        else:
            self.mostrar_lista()

    # LISTA
    def render_filtros(self):
        f = ctk.CTkFrame(self.dynamic_frame, fg_color="transparent"); f.pack(fill="x", padx=20, pady=20)
        ctk.CTkLabel(f, text="Buscar:", text_color="gray").pack(side="left")
        self.entry_search = ctk.CTkEntry(f, width=200); self.entry_search.pack(side="left", padx=5)
        self.entry_search.insert(0, self.filtro_txt_var)
        self.entry_search.bind("<KeyRelease>", self.filtrar_tabla)
        self.cb_filtro_rol = ctk.CTkComboBox(f, values=["Todos", "Estudiante", "Docente", "Administrativo", "Sudito (Admin)"], command=self.recargar_tabla_evento); self.cb_filtro_rol.pack(side="left", padx=5)
        self.cb_filtro_estado = ctk.CTkComboBox(f, values=["Todos", "Activo", "Inactivo"], command=self.recargar_tabla_evento); self.cb_filtro_estado.pack(side="left", padx=5)

    def render_tabla(self):
        h_box = ctk.CTkFrame(self.dynamic_frame, fg_color="transparent"); h_box.pack(fill="x", padx=20, pady=10)
        self.lbl_total = ctk.CTkLabel(h_box, text="Usuarios Registrados", font=("Arial", 16, "bold")); self.lbl_total.pack(side="left")
        h = ctk.CTkFrame(self.dynamic_frame, fg_color="#F9FAFB", height=40); h.pack(fill="x", padx=20)
        cols = [("ID", 60), ("Nombre Completo", 200), ("Rol", 120), ("Estado", 80), ("Acciones", 200)]
        for t, w in cols: ctk.CTkLabel(h, text=t, width=w, anchor="w", text_color="gray", font=("Arial",12,"bold")).pack(side="left", padx=10)
        self.rows_frame = ctk.CTkScrollableFrame(self.dynamic_frame, fg_color="transparent", height=300); self.rows_frame.pack(fill="both", expand=True, padx=1, pady=1)

    def cargar_datos_tabla(self, event=None):
        if self.rows_frame is None or not self.rows_frame.winfo_exists(): return
        for w in self.rows_frame.winfo_children(): w.destroy()
        
        datos = Consulta_usuarios.obtener_todos() 
        rol_sesion = getattr(self.controller, 'rol_actual', 'Sudito')
        txt = self.entry_search.get().lower() if hasattr(self, 'entry_search') else ""
        rol_f = self.cb_filtro_rol.get() if hasattr(self, 'cb_filtro_rol') else "Todos"
        est_f = self.cb_filtro_estado.get() if hasattr(self, 'cb_filtro_estado') else "Todos"

        count = 0
        for uid, nom, ape_p, ape_m, rol, estado in datos:
            if "Sudote" in str(rol): continue
            es_admin = "sudito" in str(rol).lower() or "admin" in str(rol).lower()
            soy_sudito = "sudito" in str(rol_sesion).lower()
            if soy_sudito and es_admin and "administrativo" not in str(rol).lower(): continue 
            
            n_comp = f"{nom} {ape_p} {ape_m}"
            if txt and (txt not in n_comp.lower() and txt not in str(uid)): continue
            if rol_f != "Todos" and rol_f not in rol: continue
            st_txt = "Activo" if estado else "Inactivo"
            if est_f != "Todos" and est_f != st_txt: continue
            
            count += 1
            self.crear_fila(uid, nom, ape_p, ape_m, rol, estado)
        
        if self.lbl_total: self.lbl_total.configure(text=f"Usuarios Registrados ({count})")

    def crear_fila(self, uid, nom, ape_p, ape_m, rol, estado):
        row = ctk.CTkFrame(self.rows_frame, fg_color="white", height=50); row.pack(fill="x", pady=1)
        st_t = "Activo" if estado else "Inactivo"
        st_c = "#10B981" if estado else "#DC2626"
        ctk.CTkLabel(row, text=str(uid), width=60, anchor="w").pack(side="left", padx=10)
        ctk.CTkLabel(row, text=f"{nom} {ape_p} {ape_m}", width=200, anchor="w", font=("Arial", 13, "bold")).pack(side="left", padx=10)
        ctk.CTkLabel(row, text=rol, width=120, anchor="w").pack(side="left", padx=10)
        ctk.CTkLabel(row, text=st_t, width=80, text_color=st_c).pack(side="left", padx=10)
        acts = ctk.CTkFrame(row, fg_color="transparent", width=200); acts.pack(side="left", padx=10)
        
        # Pasa los datos completos automaticamente para editar 
        ctk.CTkButton(acts, text="Editar", width=60, height=25, fg_color="#3B82F6", 
                      command=lambda: self.preparar_edicion(uid, nom, ape_p, ape_m, rol, estado)).pack(side="left", padx=2)
        ctk.CTkButton(acts, text="B/A", width=60, fg_color="gray", 
                      command=lambda: self.toggle_estado(uid, estado, rol)).pack(side="left", padx=2)
        ctk.CTkButton(acts, text="Del", width=60, fg_color="#DC2626", 
                      command=lambda: self.eliminar(uid, rol)).pack(side="left", padx=2)

    # FORMULARIO
    def cargar_formulario_ui(self):
        f = ctk.CTkFrame(self.dynamic_frame, fg_color="transparent"); f.pack(fill="both", expand=True, padx=40, pady=20)
        f.columnconfigure(0, weight=1); f.columnconfigure(1, weight=1)

        t = f"Editando ID: {self.id_edicion}" if self.id_edicion else "Nuevo Usuario"
        ctk.CTkLabel(f, text=t, font=("Arial", 18, "bold"), text_color="black").grid(row=0, columnspan=2, sticky="w", pady=20)

        self.en_nom = self.input(f, "Nombre *", 1, 0)
        self.en_pat = self.input(f, "Apellido P *", 1, 1)
        self.en_mat = self.input(f, "Apellido M", 2, 0)
        
        ctk.CTkLabel(f, text="Rol *", text_color="gray").grid(row=4, column=1, sticky="w", padx=10)
        ops = ["Estudiante", "Docente", "Administrativo", "Trabajador"]
        if "Sudote" in getattr(self.controller, 'rol_actual', 'Sudito'): ops.append("Sudito (Admin)")
        self.cb_rol = ctk.CTkComboBox(f, values=ops, command=self.check_rol); self.cb_rol.grid(row=5, column=1, sticky="ew", padx=10)
        
        ctk.CTkLabel(f, text="Estado Inicial", font=("Arial", 12, "bold"), text_color="gray").grid(row=6, column=0, padx=10, pady=(20,0), sticky="w")
        self.sw_st = ctk.CTkSwitch(f, text="Activo", onvalue=True, offvalue=False); self.sw_st.select(); self.sw_st.grid(row=7, column=0, sticky="w", padx=10)
        
        # CREDENCIALES
        self.fr_cred = ctk.CTkFrame(f, fg_color="#F3F4F6", corner_radius=10)
        self.fr_cred.grid(row=8, columnspan=2, sticky="ew", pady=20, padx=10)
        self.fr_cred.columnconfigure(0, weight=1); self.fr_cred.columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.fr_cred, text="Correo (Login)*", text_color="gray").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.en_mail = ctk.CTkEntry(self.fr_cred, height=35); self.en_mail.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        
        ctk.CTkLabel(self.fr_cred, text="Contraseña *", text_color="gray").grid(row=0, column=1, sticky="w", padx=10, pady=5)
        self.en_pass = ctk.CTkEntry(self.fr_cred, height=35, show="*"); self.en_pass.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.en_pass.bind("<KeyRelease>", self.actualizar_fuerza)

        self.progress_fuerza = ctk.CTkProgressBar(self.fr_cred, height=6, width=200); self.progress_fuerza.set(0)
        self.progress_fuerza.grid(row=2, column=1, sticky="w", padx=10, pady=(0,5))
        self.lbl_fuerza = ctk.CTkLabel(self.fr_cred, text="Seguridad: ---", font=("Arial", 10), text_color="gray")
        self.lbl_fuerza.grid(row=3, column=1, sticky="w", padx=10)

        ctk.CTkLabel(self.fr_cred, text="Confirmar *", text_color="gray").grid(row=4, column=1, sticky="w", padx=10, pady=5)
        self.en_confirm = ctk.CTkEntry(self.fr_cred, height=35, show="*"); self.en_confirm.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

        self.fr_cred.grid_remove() 

        btn_t = "Actualizar" if self.id_edicion else "Guardar"
        ctk.CTkButton(f, text=btn_t, fg_color="#10B981", height=40, command=self.guardar_bd).grid(row=9, column=1, sticky="e", pady=30, padx=10)

        # Llenar datos
        if self.id_edicion:
            self.en_nom.insert(0, self.edit_data['n'])
            self.en_pat.insert(0, self.edit_data['p'])
            self.en_mat.insert(0, self.edit_data['m'])
            self.cb_rol.set(self.edit_data['r'])
            if self.edit_data['s'] == 1: self.sw_st.select()
            else: self.sw_st.deselect()
            self.check_rol(self.edit_data['r'])

    def input(self, p, l, r, c, show=None):
        ctk.CTkLabel(p, text=l, text_color="gray").grid(row=r*2, column=c, sticky="w", padx=10)
        e = ctk.CTkEntry(p, height=35, fg_color="white", text_color="black", border_color="#E5E7EB", show=show)
        e.grid(row=r*2+1, column=c, sticky="ew", padx=10, pady=(0,10))
        return e

    def check_rol(self, v):
        if v == "Sudito (Admin)": self.fr_cred.grid()
        else: self.fr_cred.grid_remove()

    def actualizar_fuerza(self, event):
        pwd = self.en_pass.get()
        score = 0
        if len(pwd) >= 8: score += 1
        if re.search(r"[A-Z]", pwd): score += 1
        if re.search(r"[a-z]", pwd): score += 1
        if re.search(r"[0-9]", pwd): score += 1
        if re.search(r"[!@#$%^&*]", pwd): score += 1
        
        self.progress_fuerza.set(score / 5)
        if score <= 2: 
            self.progress_fuerza.configure(progress_color="#EF4444")
            self.lbl_fuerza.configure(text="Débil", text_color="#EF4444")
        elif score <= 4:
            self.progress_fuerza.configure(progress_color="#F59E0B")
            self.lbl_fuerza.configure(text="Media", text_color="#F59E0B")
        else:
            self.progress_fuerza.configure(progress_color="#10B981")
            self.lbl_fuerza.configure(text="Fuerte", text_color="#10B981")

    def guardar_bd(self):
        n, p, m, r, s = self.en_nom.get(), self.en_pat.get(), self.en_mat.get(), self.cb_rol.get(), self.sw_st.get()
        em = self.en_mail.get() if r == "Sudito (Admin)" else ""
        pw = self.en_pass.get() if r == "Sudito (Admin)" else ""
        cf = self.en_confirm.get() if r == "Sudito (Admin)" else ""

        if not n or not p: return messagebox.showerror("Error", "Faltan datos")
        
        if r == "Sudito (Admin)":
            if not em or not pw: return messagebox.showerror("Error", "Credenciales requeridas")
            if pw != cf: return messagebox.showerror("Error", "Las contraseñas no coinciden")

        if self.id_edicion:
            if Consulta_usuarios.actualizar_usuario(self.id_edicion, n, p, m, r, s, em, pw):
                messagebox.showinfo("OK", "Actualizado"); self.mostrar_lista()
        else:
            nid = Consulta_usuarios.registrar_persona(n, p, m, r, s, em, pw)
            if nid:
                messagebox.showinfo("OK", "Registrado")
                if r != "Sudito (Admin)" and messagebox.askyesno("Vehículo", "¿Registrar vehículo?"):
                    self.controller.usuario_preseleccionado = {'id': nid, 'nombre': f"{n} {p}", 'rol': r}
                    self.controller.show_frame("RegistrarVehiculo")
                else: self.mostrar_lista()

    # PASAR TODOS LOS DATOS PARA EDITAR 
    def preparar_edicion(self, uid, n, p, m, r, s):
        self.id_edicion = uid
        self.edit_data = {'n': n, 'p': p, 'm': m, 'r': r, 's': s}
        self.mostrar_formulario(limpiar=False)

    def toggle_estado(self, uid, st, rol):
        if not self.validar(rol, "DESACTIVAR"): return
        Consulta_usuarios.cambiar_estado(uid, 0 if st else 1); self.cargar_datos_tabla()

    def eliminar(self, uid, rol):
        if not messagebox.askyesno("Eliminar", "¿Seguro?"): return
        if not self.validar(rol, "ELIMINAR"): return
        Consulta_usuarios.eliminar_usuario(uid); self.cargar_datos_tabla()

    def validar(self, rol, accion):
        me = getattr(self.controller, 'rol_actual', '')
        es_admin = "sudito" in str(rol).lower() or "admin" in str(rol).lower()
        if "Sudote" in me and es_admin and "administrativo" not in str(rol).lower():
             if PasswordDialog(text=f"{accion} ADMIN\n CONTRASEÑA maestra:").get_input() != "admin123":
                 messagebox.showerror("Error", "Incorrecto"); return False
        return True

    def filtrar_tabla(self, e): self.filtro_txt_var = self.entry_search.get(); self.cargar_datos_tabla()
    def recargar_tabla_evento(self, v): self.cargar_datos_tabla()
    def volver(self): self.controller.show_frame(self.controller.vista_retorno)