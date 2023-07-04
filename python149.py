#Frame
import tkinter as tk
from tkinter import ttk
from tkinter import *
karan=tk.Tk()
karan.geometry("800x800")
karan.title("Frame")
frm=Frame(karan,width=330,height=340,)
frm['bg']="black"

frm.place(x=40,y=50)
karan.mainloop()