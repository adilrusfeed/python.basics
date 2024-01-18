from tkinter import *
class fun:
    def __int__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.pbutton=Button(frame,text="clikced",command="ok")
        self.pbutton.pack()

        self.qbutton=Button(frame,text="exit",command="ok")
        self.qbutton.pack(side=LEFT)

    def pmgs(self):
        print("clicked")



