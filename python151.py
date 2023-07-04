#Scrollbar
import tkinter as tk
from tkinter import ttk
from tkinter import *
karan=tk.Tk()
karan.title("Scrollbar")
karan.geometry("800x800")
scrb=Scrollbar(karan,width=32)

scrb.place(x=10,y=10)
karan.mainloop()