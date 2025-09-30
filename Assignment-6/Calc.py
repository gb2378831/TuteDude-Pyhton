# step 1: importing
from tkinter import *

# step 2: GUI interacton
window = Tk()
window.geometry("360x332")

# step 3: Adding Inputs

# ENTRY BOX
e = Entry(window,width=56,border=5)
e.place(x=0,y=0)

# BUTTONS

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

b = Button(window,text='1', width=12, command= lambda:click(1))
b.place(x=10,y=60)

b = Button(window,text='2', width=12, command= lambda:click(2))
b.place(x=80,y=60)

b = Button(window,text='3', width=12, command= lambda:click(3))
b.place(x=170,y=60)


b = Button(window,text='4', width=12, command= lambda:click(4))
b.place(x=10,y=120)

b = Button(window,text='5', width=12, command= lambda:click(5))
b.place(x=80,y=120)

b = Button(window,text='6', width=12, command= lambda:click(6))
b.place(x=170,y=120)


b = Button(window,text='7', width=12, command= lambda:click(7))
b.place(x=10,y=180)

b = Button(window,text='8', width=12, command= lambda:click(8))
b.place(x=80,y=180)

b = Button(window,text='9', width=12, command= lambda:click(9))
b.place(x=170,y=180)


b = Button(window,text='0', width=12, command= lambda:click(0))
b.place(x=10,y=240)

b = Button(window,text='.', width=12, command= lambda:click('.'))
b.place(x=80,y=240)

#OPERATOR'S FUNCTION

def add():
    global math
    math = "addition"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window,text='+', width=12,command=add)
b.place(x=260,y=60)

def sub():
    global math
    math = "subtraction"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window,text='-', width=12, command= sub)
b.place(x=260,y=120)

def mult():
    global math
    math = "multiplication"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window,text='×', width=12, command= mult)
b.place(x=260,y=180)

def div():
    global math
    math = "division"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window,text='÷', width=12, command= div)
b.place(x=260,y=240)


def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))

b = Button(window,text='=', width=12,command=equal)
b.place(x=170,y=240)


def clear():
    e.delete(0,END)

b = Button(window,text='clear result', width=12,command=clear)
b.place(x=125,y=300)
# step 4: mainloops
mainloop()