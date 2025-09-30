# step 1 : import tkinter
from tkinter import *

# step 2 : gui interaction
window = Tk()

# step 3 : adding inputs

window.geometry('500x500')

check_box1 = IntVar()
check_box2 = IntVar()
check_box3 = IntVar()

check_btn1 = Checkbutton(window,text="apple", onvalue=1, offvalue=0, height=2,width=10)
check_btn2 = Checkbutton(window,text="mango", onvalue=1, offvalue=0, height=2,width=10)
check_btn3 = Checkbutton(window,text="plumb", onvalue=1, offvalue=0, height=2,width=10)

check_btn1.pack()
check_btn2.pack()
check_btn3.pack()

# step 4 : main loop
window.mainloop()