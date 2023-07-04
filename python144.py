#Radio button
import tkinter as tk
from tkinter import *
karan=tk.Tk()
karan.title("Radio button ")
karan.geometry("800x800")
var=StringVar(value='1')
def rbsel():
    textmsg="You select the "+var.get()
    msgVar=Message(karan,text=textmsg,width=200)
    msgVar.place(x=480,y=350)
    
rb1=Radiobutton(karan,text="Green",height=4,variable=var,value='Green',command=rbsel)
rb1.place(x=10,y=10)
rb1.pack(anchor=W)

rb2=Radiobutton(karan,text="Blue",height=4,variable=var,value='Blue',command=rbsel)
rb2.place(x=10,y=40)
rb2.pack(anchor=W)

rb3=Radiobutton(karan,text="Red",height=4,variable=var,value='Red',command=rbsel)
rb3.place(x=10,y=60)
rb3.pack(anchor=W)


karan.mainloop()