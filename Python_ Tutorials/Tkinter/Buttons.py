from tkinter import *
root = Tk()

def myClick():
    myLabel1 = Label(root, text="Pressed")
    myLabel1.pack()
# How to create button       padx and pady change the size of the button
myButton1 = Button(root, text="click me", padx=50)
# How a state is used to disable a button
myButton2 = Button(root, text="click me", state=DISABLED)
# How to make function run when pressed  fg changes text colour  bg for background colour
myButton3 = Button(root, text="click me", command=myClick, fg="blue")
myButton3.pack()

# How to create an exit button
exit_button = Button(root, text="Quit", command=root.quit)


root.mainloop()
