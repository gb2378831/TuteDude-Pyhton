# step 1 : import tkinter
from tkinter import *

# step 2 : gui interaction
window = Tk()

# step 3 : adding inputs
window.title("Simple")
window.geometry("500x700")
window.config(bg="yellow")
frame1 = Frame(window, width=300,height=300, cursor="dot")
frame2 = Frame(window,width=300,height=300, cursor="dotbox")

button1 = Button(frame1,text="Button",bg="Blue")
button2 = Button(frame2,text="Button",bg="green")
button3 = Button(frame1,text="Logged",fg="red")


frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button2.pack()
button1.pack()
button3.pack()
# step 4 : main loop
window.mainloop()