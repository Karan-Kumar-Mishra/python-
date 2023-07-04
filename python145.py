#Entry
import tkinter as tk
from tkinter import *
karan=tk.Tk()
karan.title("Entry widget Example")
karan.geometry("500x500")
lb1=Label(karan,text="Username")
lb1.place(x=40,y=40)
etr1=Entry(karan)
etr1.place(x=180,y=40)
lb2=Label(karan,text="Password")
lb2.place(x=40,y=180)
etr2=Entry(karan)
etr2.place(x=180,y=180)
btn1=Button(karan,width=20,text="Login",command=karan.destroy)
btn1['bg']="blue"
btn1['fg']="white"
btn1.place(x=120,y=350)













karan.mainloop()