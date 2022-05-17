# How to import tkinter
from tkinter import *

# root widget creates the screen, needs to go first
root = Tk()

# To create a widget you need to define it then pace it

# Creates a label, hasn't been placed yet
myLabel = Label(root, text="Hello World")

# Methods of placing
# Pack, places it at the first available stop, simplest
myLabel.pack()

# Event look is required to register inputs and changes, clicking button etc
# Required
root.mainloop()