from tkinter import *

def changeText():
    label_name.config(text="Rodrigo Abdiel Avitia Benitez :)")
    label_password.config(text="derfarlolcrack")

def backText():
    label_name.config(text="Name: ")
    label_password.config(text="Password: ")

window = Tk()

window.title("Use of buttons")
window.geometry("600x600")

principal_frame=Frame(window)
principal_frame.config(width=600,
                       height=50,
                       border=2,
                       bg="#ADADAD",
                       relief=SOLID)

principal_frame.pack_propagate(FALSE)
principal_frame.pack(side=TOP)

label_title=Label(principal_frame, text="Login")
label_title.config(
    bg="#ADADAD",
    height=25,
    font="Arial"
)

label_title.pack()

label_name=Label(window,text="Name")
label_name.pack(pady=10)
label_password=Label(window,text="Password: ")
label_password.pack(pady=10)

accept_button = Button(window, bg="#969696", text="Accept", command=changeText)
accept_button.pack(pady=30)

back_button=Button(window, bg="#969696", text="Go Back", command=backText)
back_button.pack(pady=10)


window.mainloop()