from tkinter import *

def showstatus(type):
    status.config(text=f"{type}", bg="#C2C2C2")

window = Tk()

window.title("Menu Practice")
window.geometry("500x500")
window.config(bg="#C2C2C2")
menuBar=Menu(window)
window.config(menu=menuBar,bg="#C2C2C2")

archiveMenu=Menu(menuBar, tearoff=FALSE, bg="#C2C2C2")
menuBar.add_cascade(label="File",menu=archiveMenu)
archiveMenu.add_command(label="New file",command=lambda:showstatus("New File"))
archiveMenu.add_separator()
archiveMenu.add_command(label="Save File",command=lambda:showstatus("Save Done"))
archiveMenu.add_separator()
archiveMenu.add_command(label="Exit",command=window.quit)

editMenu=Menu(menuBar, tearoff=FALSE,bg="#C2C2C2")
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy",command=lambda:showstatus("Copy Done"))
editMenu.add_separator()
editMenu.add_command(label="Cut",command=lambda:showstatus("Cut Done"))

status= Label(window, text="")
status.pack()

window.mainloop()