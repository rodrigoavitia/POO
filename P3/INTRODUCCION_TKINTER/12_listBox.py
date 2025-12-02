from tkinter import *
import os
os.system("cls")

def showselection():
    selection=list1.get(list1.curselection())
    selectionlabel.config(text=f"You selected: {selection} ")


window = Tk()

window.title("Listbox Practice")
window.geometry("500x500")
window.config(bg="LightGray")

list1=Listbox(window, width=15,height=6,selectmode=SINGLE, bg="LightBlue")
list1.pack()

options=["Yellow", "Blue", "Red", "Green", "Black", "White"]
for i in options:
    list1.insert(END,i)

showselectionbutton = Button(window, text="Show selection", command = showselection, bg="LightGray")
showselectionbutton.pack()

selectionlabel=Label(window, text="", bg="LightGray")
selectionlabel.pack()

window.mainloop()