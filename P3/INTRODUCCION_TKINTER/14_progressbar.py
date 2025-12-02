from tkinter import *
from tkinter import ttk
import os


os.system("cls")

window = Tk()

def progress():
    progressbar1["value"]=0
    window.update()
    for i in range(101):
        progressbar1["value"]=i
        window.update()
        window.after(50) 


window.title("ProgressBar Practice")
window.geometry("500x500")

progressbar1=ttk.Progressbar(window, orient=HORIZONTAL, length=300, mode="determinate",)
progressbar1.pack()

startbutton=Button(text="Start")
startbutton.pack()
startbutton.config(bg="#9F9F9F", width=5, command=progress)




window.mainloop()