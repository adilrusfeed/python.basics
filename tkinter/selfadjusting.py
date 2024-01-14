from tkinter import *
from tkinter import messagebox
root =Tk()

l1=Label(root,text="adil",bg="green")

l1.pack(fill=X)
def fun():
    print("click here")
button1=Button(root,text="loged in",command=fun)
button1.pack()

messagebox.showinfo("title","login succes")
messagebox.showwarning("title","login succes")
messagebox.showerror("title","login succes")
messagebox.askquestion("title","is it python")
messagebox.askokcancel("title","login succes")




root.mainloop()