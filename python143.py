import tkinter as tk
from tkinter import *
def function():
    textmsg="hii this is simple message"
    msgvar=Message(karan,text=textmsg,width=200)
    msgvar.place(x=490,y=180)
karan=tk.Tk()
karan.title("Message")
karan.geometry("800x500")
btn=tk.Button(karan,width=10,text="click me!",command=function)

btn.place(x=120,y=180)





karan.mainloop()