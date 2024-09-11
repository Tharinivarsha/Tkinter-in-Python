#Activity1
from tkinter import *
window= Tk()
window.geometry("500x500")
window.title("Tkinter sample window")
Greeting=Label(text="Hello",fg="red",bg="yellow")
button=Button(text="Click Me",fg="green",bg="orange")
entry=Entry(fg="blue",bg="pink",width=50)


Greeting.pack()
button.pack()
entry.pack()
frame=Frame(master=window,relief=RAISED,borderwidth=5)
framelabel=Label(master=frame,text="Sample frame")
frame.pack()
framelabel.pack()
textbox=Text(fg="red",bg="yellow")
textbox.pack()
window.mainloop()