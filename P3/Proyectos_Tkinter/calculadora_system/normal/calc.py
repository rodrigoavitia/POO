"""
1.- Dos campos de Texto
2.- 4 Botones para las operaciones básicas
3.- Un campo para mostrar el resultado
"""
import os
from tkinter import *
from tkinter import messagebox
from unittest import result

os.system("cls")

window = Tk()

def operation(title,number1,number2,result,operator):
    if operator == "+":
        result = number1 + number2  
    elif operator == "-":
        result = number1 - number2
    elif operator == "x":
        result = number1 * number2
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            messagebox.showerror(title="Error", message="Cannot divide by zero.")
            return
    messagebox.showinfo(title=f"{title} Result",
                        message=f"{number1} {operator} {number2} = {result}")
def exitoperation():
    window.quit()

window.title("Calculator")
window.geometry("600x400")
window.resizable(FALSE,FALSE)

n1=IntVar()
number1=Entry(window, textvariable=n1,width=5,justify="right")
number1.pack(side=TOP,anchor="center")

n2=IntVar()
number2=Entry(window, textvariable=n2,width=5,justify="right")
number2.pack(side=TOP,anchor="center", pady=10)

plusbutton=Button(window,text="+",
                   command=lambda:operation("Addition", n1.get(), n2.get(), 0, "+"))
plusbutton.pack()

substractionbutton=Button(window,text="-",
                           command=lambda:operation("Subtraction", n1.get(), n2.get(), 0, "-"))
substractionbutton.pack(pady=10)

multiplicationbutton=Button(window, text="x", 
                            command=lambda:operation("Multiplication", n1.get(), n2.get(), 0, "x"))
multiplicationbutton.pack(pady=10)


divisionbutton=Button(window,text="/",
                       command=lambda:operation("Division", n1.get(), n2.get(), 0, "/"))
divisionbutton.pack(pady=10)

exitbutton=Button(window, text="Exit", command=exitoperation())
exitbutton.pack(pady=10)



window.mainloop()










