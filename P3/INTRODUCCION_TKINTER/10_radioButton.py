from tkinter import *
import os

os.system("cls")


window = Tk()

window.title("Radio Button Practice")
window.geometry("500x500")




def selectedoption():
    selectionText.config(text=f"Option selected: {option.get()}")

option=StringVar()
optionbuttons = Radiobutton(window, text="option 1", variable=option,value="option 1")
optionbuttons.pack()

optionbuttons2 = Radiobutton(window, text="option 2", variable=option,value="option 2")
optionbuttons2.pack()

optionbuttons3 = Radiobutton(window, text="option 3", variable=option,value="option 3")
optionbuttons3.pack()

showselectionbutton = Button(window,text="Show selection", command=selectedoption)
showselectionbutton.pack()




selectionText = Label(window, text="")
selectionText.pack()



window.mainloop()