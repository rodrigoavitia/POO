from tkinter import *

"""
def changeData():
    name= txt_name.get()
    helloLabel.config(text=f".:: Welcome {name} to your first functional interface :D ")

window=Tk()

window.title("Entry")
window.geometry("600x600")

writeName=Label(window, text="Write your name: ")
writeName.pack(pady=25)

txt_name=Entry(window,width=50)
txt_name.pack()

button1=Button(window,text="Salute",command=changeData)
button1.pack(pady=25)


helloLabel=Label(window,text="")
helloLabel.pack()

window.mainloop()

"""

def delete():
    usernametxt.delete(0,END)
    password_txt.delete(0, END)


window=Tk()

window.title("System")
window.geometry("700x700")

label_title=Label(window, text="System Access Caution!")
label_title.config(
     bg="#CC4E00",
     fg="#E1FF00",
     width=50,
     height=4,
     font=("Arial",20,"bold"),
     relief=SOLID,
     border=1
)
label_title.pack(pady=25)

nameLabel=Label(window, text="UserName",)
nameLabel.pack(pady=5)

usernametxt=Entry(window,width=50)
usernametxt.pack(pady=5)

passwordLabel=Label(window, text="Password")
passwordLabel.pack(pady=5)

password_txt=Entry(window,width=50,show="*")
password_txt.pack(pady=5)

loginbutton=Button(window,text="Login")
loginbutton.pack(pady=5)

deletebutton=Button(window,text="Delete")
deletebutton.pack(pady=5)







window.mainloop()







