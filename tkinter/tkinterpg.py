# from tkinter import *
# root=Tk()
#
#
# label=Label(root,text="Adil Rusfeed").pack()
# frame1=Frame(root)
# frame1.pack()
# but=Button(frame1,text="Ok",fg="white",bg="black").pack()
#
# root.mainloop()

# --------------------------------------------------------------------------------------------------------

from tkinter import *
root=Tk()

l1=Label(root,text="username")
l2=Label(root,text="password")
l3=Label(root,text="confirm password")
l4=Label(root,text="mobile")
l5=Label(root,text="age")
l6=Label(root,text="email")

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Entry(root)
entry5=Entry(root)
entry6=Entry(root)
l1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
l2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
l3.grid(row=2,column=0)
entry3.grid(row=2,column=1)
l4.grid(row=3,column=0)
entry4.grid(row=3,column=1)
l5.grid(row=4,column=0)
entry5.grid(row=4,column=1)
l6.grid(row=5,column=0)
entry6.grid(row=5,column=1)

root.mainloop()


