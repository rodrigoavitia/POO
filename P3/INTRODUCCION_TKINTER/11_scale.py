from tkinter import *
import os

os.system("cls")

window = Tk()

window.title("Scale Practice")
window.geometry("500x500")

def showstatus():
    result.config(text=f"Value selected is: {value.get()} ")

value=IntVar()
scalebar=Scale(window, from_ = 0, to=100, orient=HORIZONTAL, variable=value, length=400)
scalebar.pack()



button=Button(window, text="Confirm", command=showstatus)
button.pack()

result = Label(window, text="")
result.pack()

window.mainloop()