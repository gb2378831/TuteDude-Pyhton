# step 1 : import tkinter
from tkinter import *

# step 2 : gui interaction
window = Tk()

# step 3 : adding inputs
window.title("Simple")
window.geometry("500x500")

label1 = Label(window,text="Label1",bg="red",fg="white")
label2 = Label(window,text="Label2",bg="blue",fg="white")
label3 = Label(window,text="Label3",bg="green",fg="white")



label1.pack(side=TOP , fill=X, expand=False)
label2.pack(side=LEFT , fill=Y, expand=False)
label3.pack(side=RIGHT , fill=Y, expand=False)

# step 4 : main loop
window.mainloop()