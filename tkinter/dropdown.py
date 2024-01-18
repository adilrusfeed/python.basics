from tkinter import *

root = Tk()
def file():
    print("saved")
def edit():
    print("edited")
def view():
    print("view")
def navigate():
    print("navigate")
def run():
    print("Run")


mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project", command=file)
submenu.add_command(label="New", command=file)
submenu.add_command(label="New Scratch File", command=file)
submenu.add_command(label="Ope", command=file)
submenu.add_command(label="Save As", command=file)

newmenu1 = Menu(mymenu)

mymenu.add_cascade(label="Edit", menu=newmenu1)
newmenu1.add_command(label="Undo", command=edit)
newmenu1.add_command(label="Redo", command=edit)
newmenu1.add_command(label="Cut", command=edit)
newmenu1.add_command(label="Copy", command=edit)

newmenu2 = Menu(mymenu)

mymenu.add_cascade(label="View", menu=newmenu2)
newmenu2.add_command(label="Appearance", command=view)
newmenu2.add_command(label="Recent", command=view)
newmenu2.add_command(label="Editor", command=view)

newmenu3 = Menu(mymenu)

mymenu.add_cascade(label="Navigate", menu=newmenu3)
newmenu3.add_command(label="Search", command=navigate)
newmenu3.add_command(label="Class", command=navigate)
newmenu3.add_command(label="File", command=navigate)
newmenu3.add_command(label="Text", command=navigate)

newmenu4 = Menu(mymenu)

mymenu.add_cascade(label="Run", menu=newmenu4)
newmenu4.add_command(label="Run", command=run)
newmenu4.add_command(label="Debug", command=run)
newmenu4.add_command(label="Stop", command=run)
newmenu4 .add_command(label="Breakpoint", command=run)
root.mainloop()
