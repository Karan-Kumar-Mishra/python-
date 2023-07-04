import tkinter as tk
from tkinter import *
karan=tk.Tk()
karan.title("GUI")
karan.geometry("800x400")
btn1=tk.Button(karan,width=15,text="Exit",command=karan.destroy)
btn1['bg']="blue"
btn1['fg']="White"

btn1.place(x=490,y=150)
var1=IntVar()
cb1=Checkbutton(karan,width=10,text="Travel",variable=var1,onvalue=1,offvalue=0,height=3).grid(row=0,sticky=W)

var2=IntVar()
cb2=Checkbutton(karan,width=10,text="Sports",variable=var2,onvalue=1,offvalue=0,height=3).grid(row=1,sticky=W)


var3=IntVar()

cb3=Checkbutton(karan,width=10,text="Music",variable=var3,onvalue=1,offvalue=0,height=3).grid(row=2,sticky=W)





karan.mainloop()