from tkinter import * 

window=Tk()

window.title("Uso del mainloop")
window.geometry("600x600")

frame1=Frame(window,width=600,height=100, bg="#FF0000",border=2,relief="raised").pack()
frame2=Frame(window,width=600,height=100, bg="#FF8800",border=2,relief="raised").pack()
frame=Frame(window,width=600,height=100, bg="#F6FF00",border=2,relief="raised").pack()
frame4=Frame(window,width=600,height=100, bg="#1AFF00",border=2,relief="raised").pack()
frame5=Frame(window,width=600,height=100, bg="#002AFF",border=2,relief="raised").pack()
frame6=Frame(window,width=600,height=100, bg="#A812F3",border=2,relief="raised").pack()
window.mainloop()

