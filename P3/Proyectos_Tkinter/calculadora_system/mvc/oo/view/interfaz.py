from tkinter import *
from tkinter import messagebox
from controller import funciones
from model import operaciones
from tkinter import messagebox
 
class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("1024x768")
        ventana.resizable(False,False)#para que la ventana ya no se pueda hacer mas grande o pequeña   
        self.interfaz(ventana)
      
    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)    
        #Interfaz o vista
        #ventana=Tk()
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana, textvariable=n1, width=5,justify="right")
        txt_numero1.focus()#cuando se ejecuta, pon el cursos encima algo así
        txt_numero1.pack(side="top",anchor="center")

        txt_numero2=Entry(ventana, textvariable=n2, width=5, justify="right")
        txt_numero2.pack(side="top", anchor="center")


        btn_suma=Button(ventana,text="+",
                    command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_suma.pack()

        btn_resta=Button(ventana,text="-",command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="x",command=lambda: funciones.Controladores.operaciones("Multiplicación",n1.get(),n2.get(),"x"))
        btn_multiplicacion.pack()

        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("División",n1.get(),n2.get(),"/"))
        btn_division.pack()


        boton_salir=Button(ventana, text=" Salir ", command=ventana.quit)
        boton_salir.pack()

        etiqueta=Label(ventana, text=" ")
        etiqueta.pack()
        
    def menuPrincipal(self, ventana):
        menuBar=Menu(ventana)
        ventana.config (menu=menuBar)

        operacionesMenu=Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciones",menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda:self.interfaz(ventana))#aca lo envío, por eso pone parámetro
        operacionesMenu.add_command(label="Consultar",command=lambda: self.mostrar(ventana))
        operacionesMenu.add_command(label="Cambiar",command=lambda:self.cambiar(ventana))
        operacionesMenu.add_command(label="Borrar",command=lambda:self.eliminar(ventana))
        #lamba es una palabra reservada que 
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir",command=ventana.quit)
        
        
    def eliminar(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        etiqueta2=Label(ventana,text=".:: Borrar una Operación ::.")
        etiqueta2.pack(pady=10)
        etiqueta1=Label(ventana, text="ID de la Operación: ")
        etiqueta1.pack(pady=5)
        id=IntVar
        texto=Entry(ventana, textvariable=id,justify="right",width=25)
        texto.focus()
        texto.pack(pady=5)
        boton_eliminar=Button(ventana, text="Eliminar",command=lambda: operaciones.Operaciones.eliminar(id.get()))
        boton_eliminar.pack(pady=5)
        boton_volver=Button(ventana, text="Volver",command=lambda: self.interfaz(ventana))
        boton_volver.pack(pady=5)
        
        
    def mostrar(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        etiqueta2=Label(ventana,text=".:: Listado de las operaciones ::.")
        etiqueta2.pack(pady=10)
        
        registros=operaciones.Operaciones.consultar()
        filas=""
        if len(registros)>0:
            num=1
            for fila in registros:
                filas=filas+f"\nOperacion: {num} ID:{fila[0]} FECHA:{fila[1]} Operación:{fila[2]}{fila[4]}{fila[3]}={fila[5]}"
                num+=1
        else:
            messagebox.showinfo(icon="info",message="..No existen operaciones en el Sistema")

        lbl=Label(ventana,text=f"{filas}")
        lbl.pack()
        boton_volver=Button(ventana, text="Volver",command=lambda: self.interfaz(ventana))
        boton_volver.pack(pady=5)
        
    def cambiar(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        etiqueta2=Label(ventana,text=".:: Cambiar una operación ::.")
        etiqueta2.pack(pady=10)
        etiqueta1=Label(ventana, text="ID de la Operación: ")
        etiqueta1.pack(pady=5)
        id=IntVar
        texto=Entry(ventana, textvariable=id,justify="right",width=25)
        texto.focus()
        texto.pack(pady=5)
        etiqueta3=Label(ventana, text="Nuevo número 1: ")
        etiqueta3.pack(pady=5)
        n1=IntVar
        texto=Entry(ventana, textvariable=n1,justify="right",width=25)
        texto.pack(pady=5)
        
        etiqueta4=Label(ventana, text="Nuevo número 2: ")
        etiqueta4.pack(pady=5)
        n2=IntVar
        texto2=Entry(ventana, textvariable=n2,justify="right",width=25)
        texto2.pack(pady=5)
        
        etiqueta5=Label(ventana, text="Nuevo signo: ")
        etiqueta5.pack(pady=5)
        signo=""
        texto3=Entry(ventana, textvariable=signo,justify="right",width=25)
        texto3.pack(pady=5)
        
        etiqueta6=Label(ventana, text="Nuevo resultado: ")
        etiqueta6.pack(pady=5)
        resul=IntVar
        texto4=Entry(ventana, textvariable=resul,justify="right",width=25)
        texto4.pack(pady=5)
    
        
        boton_guardar=Button(ventana, text="Guardar",command=lambda: "")
        boton_guardar.pack(pady=5)
    
        boton_volver=Button(ventana, text="Volver",command=lambda: self.interfaz(ventana))
        boton_volver.pack(pady=5)
         
        
    def borrarPantalla(self, ventana):
            for widget in ventana.winfo_children():
                widget.destroy()
           
     #cada interfaz puede ser un metodo      
     #cuando creas un metodo estatico, ya todo tiene que ser estatico
     