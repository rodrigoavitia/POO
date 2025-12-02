from tkinter import messagebox
import os

os.system("cls")

def operation(title,number1,operator,number2,result):
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
