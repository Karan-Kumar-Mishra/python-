#Menubutton
import tkinter as tk
from tkinter import ttk
from tkinter import *
karan=tk.Tk()
karan.geometry("800x800")
karan.title("Menubutton")
mebtn=Menubutton(karan,width=20,height=20)
mebtn.place(x=10,y=10)
mebtn['bg']="black"
karan.mainloop()