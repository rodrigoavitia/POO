from tkinter import *
import os

os.system("cls")

window = Tk()

def message1(type):
    result.config(text=f"{type}")

window.title("Pillow Images Practice")
window.geometry("500x500")

# Primer forma de agregar imagenes con la libreria de Tkinter :D

image1=PhotoImage(file="C:\\Users\\Abdie\\OneDrive\\Documentos\\POO\\P2\\INTRODUCCION_TKINTER\\K9wD.gif")

label=Label(window,image=image1)
label.pack()

buttonimage=Button(window, image=image1, command=lambda:message1("Hello Python"))
buttonimage.pack()

result=Label(window, text="")
result.pack() 

window.mainloop()