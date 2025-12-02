from tkinter import *
from tkinter import messagebox


window = Tk()

window.title("Warnings Practice")
window.geometry("500x500")

boton_warning = Button(window, text="Escaner", command="show_warning")
boton_warning.pack(pady=20)




window.mainloop()