from tkinter import *
root=Tk()

def printName(event):
    print("wa7wa7 hachimyen ")
button_1= Button(root,text="enzel ou bella3 ")
button_1.bind("<Button-1>",printName)
button_1.pack()

root.mainloop()

