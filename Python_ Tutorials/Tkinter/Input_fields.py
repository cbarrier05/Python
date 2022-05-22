from tkinter import *
root = Tk()

# How to create input field
entry1 = Entry(root)
entry1.pack()

entry1.insert(0, "Enter your name")     # Places default data into input field


def myClick():  # entry1.get() gets the contents opf entry1
    hello = "Hello" + entry1.get()
    myLabel1 = Label(root, text=hello)
    myLabel1.pack()


myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()