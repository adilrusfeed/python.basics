from  tkinter import *
root =Tk()

canves=Canvas(root,width=100,height=200)
canves.pack()
newline=canves.create_line(0,0,50,80)
root.mainloop()