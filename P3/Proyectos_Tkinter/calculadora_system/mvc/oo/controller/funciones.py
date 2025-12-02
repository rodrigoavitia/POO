from tkinter import messagebox
from model import operaciones   #vinculo

class Controladores:
    @staticmethod
    def operaciones(titulo,numero1,numero2,signo):
        if signo=="+":
            resultado=numero1+numero2
        elif signo=="-":
            resultado=numero1-numero2
        elif signo=="x":
            resultado=numero1*numero2
        elif signo=="/":
            resultado=numero1/numero2
            
        #messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}{signo}{numero2}={resultado}")
        
        resul=messagebox.askquestion(title=titulo,message=f"{numero1}{signo}{numero2}={resultado}\n¿Quieres guardar la operación en la BD?",icon="question")
        if resul=="yes":
            respuesta=operaciones.Operaciones.insertar(numero1,numero2,signo,resultado)
            Controladores.respuesta_sql("Agregar registro", respuesta)
            
    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="... ¡ Accion realizada con Éxito !...")
        else:
            messagebox.showinfo(icon="info",title=titulo,message="... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...")