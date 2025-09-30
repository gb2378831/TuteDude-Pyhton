# step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : gui interaction
window = Tk()

# step 3 : adding inputs
tkinter.messagebox.showerror("Info", "Runnig out of time")
question = tkinter.messagebox.askokcancel("Weather", "will it rain")

if question == True:
    print("Take an Umbrela")

else:
    print("Okay")


# step 4 : main loop
window.mainloop()