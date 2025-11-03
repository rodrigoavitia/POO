from tkinter import * 

window=Tk()

window.title("Uso del Mainloop")
window.geometry("600x600")

frame1=Frame(window,width=600,height=100, bg="#FF0000",border=2,relief="raised")
frame1.pack_propagate(FALSE)
frame1.pack()

frame2=Frame(window,width=600,height=100, bg="#FF8800",border=2,relief="raised")
frame2.pack_propagate(FALSE)
frame2.pack()

frame3=Frame(window,width=600,height=100, bg="#F6FF00",border=2,relief="raised")
frame3.pack_propagate(FALSE)
frame3.pack()

frame4=Frame(window,width=600,height=100, bg="#1AFF00",border=2,relief="raised")
frame4.pack_propagate(FALSE)
frame4.pack()



labe1=Label(frame1,text="I'm Abdiel Avitia :) ", bg="#FF0000").pack(pady=10)
label2=Label(frame2, text="UTD",bg="#FF8800").pack(pady=10)
label3=Label(frame3, text="Information Technology",bg="#F6FF00").pack(pady=10)
label4=Label(frame4, text="Multiplataform development",bg="#1AFF00").pack(pady=10)


window.mainloop()