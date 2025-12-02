from tkinter import *

window = Tk()

window.title("CheckButton Practice")
window.geometry("500x500")

def showstatus():
    if option.get() == 1:
        result.config(text="Notifications activated :)")
    else:
        result.config(text="Notifications desactivated :(")

option=IntVar()
confirmation = Checkbutton(window, text="Do you want receive notifications?",
                           variable=option,onvalue=1, offvalue=0)
confirmation.pack()

confirmationButton = Button(window, text="Confirm", command=showstatus)
confirmationButton.pack()

text_label = Label(window, text = "")
text_label.pack()

result = Label(window, text="")
result.pack()




window.mainloop()

