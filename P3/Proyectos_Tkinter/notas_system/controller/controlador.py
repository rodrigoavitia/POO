
from tkinter import messagebox
from model import usuario,nota
from view import menu_principal
class Controladores():
    @staticmethod
    def registrar(nombre,apellidos,email,password):
        resultado=usuario.Usuarios.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos}, se registro correctamente con el email {email}",title="Registro exitoso")
        else:
            messagebox.showerror(message="Hubo un error al registrarse")

    @staticmethod
    def login(ventana,email,password):
        registro=usuario.Usuarios.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info",message=f"{registro[1]} {registro[2]}, haz iniciado sesion correctamente",title="Registro exitoso")
            menu_principal.InterfacesMenu.menu_notas(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showerror(message="Hubo un error al iniciar sesion, vuelve a intentar")

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo,message="La accion se ha realizado con exito")
        else:
            messagebox.showinfo(title="Algo ha salido mal",message="La accion no se ha podido realizar",icon="warning")

    @staticmethod
    def crear_nota(titulo,descripcion,uid):
        resultado=nota.Notas.crear(uid,titulo,descripcion)
        Controladores.respuesta_sql("Crear notas",resultado)

    @staticmethod
    def mostrar_nota(uid):
        registro=nota.Notas.mostrar(uid)
        return registro
    
    @staticmethod
    def eliminar_nota(id):
        respuesta=nota.Notas.eliminar(id)
        Controladores.respuesta_sql("Eliminar nota",respuesta)

    def modificar_nota(id,titulo,desc):
        respuesta=nota.Notas.actualizar(id,titulo,desc)
        Controladores.respuesta_sql("Modificar nota",respuesta)
    