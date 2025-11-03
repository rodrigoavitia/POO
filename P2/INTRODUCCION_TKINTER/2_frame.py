from tkinter import * 

ventana = Tk()
ventana.title("Marcos o Frame en Tkinter")
ventana.geometry("800x600")
ventana.resizable(FALSE,FALSE)

marco1=Frame(ventana,width=600,height=400,bg="green",relief=SOLID,border=2)
marco1.pack_propagate(FALSE) #ESTO EVITA QUE SE MODIFIQUE EL ESTILO DEL MARCO ORIGINAL
marco1.pack(pady=100)
marco1.pack() #ES IMPORTANTE PARA QUE SE DIBUJE O MUESTRE EL OBJETO DENTRO DE LA VENTANA  

marco2=Frame(marco1,width=300, height=150, bg="silver",relief=GROOVE,border=10)
marco2.pack()
marco2.pack(pady=25)
ventana.mainloop()

