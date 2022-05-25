from tkinter import *
root = Tk()

isClicked = IntVar()

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
# How to create a radio button

#Radiobutton(root, text= "Option1", variable=isClicked, value=1, command=lambda: clicked(isClicked.get())).pack()
#Radiobutton(root, text= "Option2", variable=isClicked, value=2, command=lambda: clicked(isClicked.get())).pack()
# When clicked it sets isClicked to the value of the clicked button

# Creating radio buttons with a loop, this creates 3 but can be modified for any amount
ButtonOptions = [
    ("Option1", 1), # First part is displayed text, second part is value
    ("Option2", 2),
    ("Option3", 3)
]
option = IntVar()
for text, ButtonOption in ButtonOptions:
    Radiobutton(root, text=text, variable=option, value=ButtonOption).pack()

myLabel = Label(root, text=isClicked.get())
myLabel.pack()
mainloop()