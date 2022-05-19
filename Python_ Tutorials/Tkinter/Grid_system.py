from tkinter import *
root = Tk()

myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="I am Christian")

# How to place these labels with the grid system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# or can define and place in same command
myLabel3 = Label(root, text="I am a student").grid(row=0, column=3)


root.mainloop()
