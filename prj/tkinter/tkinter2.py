#!/usr/bin/env python3
#          21 : tkinter 2
#  https://www.youtube.com/watch?v=Mim5tTSf05E&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=21
#   http://www.newthinktank.com/2016/08/learn-program-21/
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# ---------- VARIABLES & UNBIND ----------
def get_data(event):
    # Output the values for the Widgets with get()
    print("String :", strVar.get())
    print("Integer :", intVar.get())
    print("Double :", dblVar.get())
    print("Boolean :", boolVar.get())


# You can unbind and rebind an event to a function
def bind_button(event):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)


root = Tk()

# As I showed previously there are TkInter variables
# you can use with Widgets to set and get values
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

# Set the default values with set()
strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

# Assign the variable to either textvariable or variable
strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

# Depending on if this check button is selected or not
# will determine if we can get data on our Widgets
theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)#left button
theCheckBut.pack(side=LEFT)

# Call the function get_data on click
getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()
