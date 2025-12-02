import os
from tkinter import *
from tkinter import messagebox
from controller import functions

os.system("cls")

class Views():
    def __init__(self,window):
        window.title("Calculator")
        window.geometry("600x400")
        window.resizable(FALSE,FALSE)


     
    def interface(self):
        n1=IntVar()
        number1=Entry(window, textvariable=n1,width=5,justify="right")
        number1.pack(side=TOP,anchor="center")

        n2=IntVar()
        number2=Entry(window, textvariable=n2,width=5,justify="right", )
        number2.pack(side=TOP,anchor="center", pady=10)

        plusbutton=Button(window,text="+",
                        command=lambda:functions.operation("Addition",n1.get(),n2.get(),"+",result=0))
        plusbutton.pack()

        substractionbutton=Button(window,text="-",
                                command=
                                lambda:functions.operation("Substraction",n1.get(),n2.get(),"-", result=0))
        substractionbutton.pack(pady=10)

        multiplicationbutton=Button(window, text="x", 
                                    command=lambda:functions.operation("Multiplication",n1.get(),n2.get(),"x", result=0))
        multiplicationbutton.pack(pady=10)


        divisionbutton=Button(window,text="/",
                            command=lambda:functions.operation("Division",n1.get(),n2.get(),"/", result=0))
        divisionbutton.pack(pady=10)

        exitbutton=Button(window, text="Exit", command="exitoperation()")
        exitbutton.pack(pady=10)

