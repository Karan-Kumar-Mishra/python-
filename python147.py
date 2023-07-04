#Combobox
import tkinter as tk
from tkinter import ttk
from tkinter import *
karan=tk.Tk()
karan.title("Combobox")
karan.geometry("600x600")
var=tk.StringVar()
cb=ttk.Combobox(karan,width=30,textvariable=var)
cb['values']=('january',
              'February',
              'March',
              'April',
              'May',
              'june',
              'july',
              'August',
              'September',
              'October',
              'November',
              'December'
    
)
cb.place(x=60,y=60)
cb.current()
btn=Button(karan,text="Submit",width=15,command=karan.destroy)
btn.place(x=180,y=420)


karan.mainloop()