#Canvas

import tkinter as tk
from tkinter import ttk
from tkinter import *
karan=tk.Tk()
karan.geometry("1400x800")
cav=Canvas(karan,width=550,height=550)
cav['bg']='black'
cav.create_rectangle(50, 80, 200, 200, fill="red")
cav.place(x=10,y=10)











karan.mainloop()