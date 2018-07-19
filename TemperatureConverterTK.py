from tkinter import *
from tkinter import ttk
import re
import time
import threading
root = Tk()
mainframe = ttk.Frame(root)
mainframe.grid()
tempF = StringVar()
tempF.set(68)
tempC = StringVar()
tempC.set(20)
box = ttk.Entry(mainframe, width=4, textvariable=tempF)
box.grid()
ttk.Label(mainframe, textvariable=tempC).grid()
def Calc():
    if tempF.get() == "":
        tempC.set("")
    else:
        if tempF.get()[0] != '-':
            tempF.set(re.sub("[^0-9]", "", tempF.get()))
        else:
            tempF.set("-"+re.sub("[^0-9]", "", tempF.get()[1:]))
        if tempF.get() == "" or tempF.get() == "-":
            tempC.set("")
        else:
            tempC.set((5/9) * (int(tempF.get()) - 32))
    root.after(1, Calc)
Calc()
root.mainloop()