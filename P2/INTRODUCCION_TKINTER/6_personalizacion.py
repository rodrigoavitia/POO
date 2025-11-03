from tkinter import *

def click():
    label_principal.config(text="OOP WITH PYTHON!");
def goback():
    label_principal.config(text="WELCOME TO Tkinter! ");
   

window=Tk();

window.title("Custom Widgets");
window.geometry("600x600");


label_principal=Label(window, text="WELCOME TO Tkinter!");
label_principal.config(
     bg="#004985",
     fg="#E1FF00",
     width=50,
     height=4,
     font=("Helvetica",30,"italic"),
     relief=SOLID,
     border=2
);
label_principal.pack(pady=25);


button1=Button(window,text="Click Here!",command=click);
button1.config(bg="#A9A9A9",
     fg="#00206F",
     width=15,
     font=("Arial",20,"italic"),
     relief=GROOVE,
     border=2,
     activeforeground="yellow",
     activebackground="black",
     # state= this desactivate the button

);
button1.pack(pady=25);


button2=Button(window,text="Go Back",command=goback)
button2.config(bg="#A9A9A9",
     fg="#00206F",
     width=15,
     font=("Arial",20,"italic"),
     relief=GROOVE,
     border=2,
     activeforeground="yellow",
     activebackground="black",

);
button2.pack(pady=20);





window.mainloop();



