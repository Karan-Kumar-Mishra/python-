#Listbox
import tkinter as tk
from tkinter import *
karan=tk.Tk()
karan.title("List box ")
karan.geometry("500x500")
lb1=Listbox(karan,width=20)
lb1.insert(1,"c")
lb1.insert(2,"c++")
lb1.insert(3,"java")
lb1.insert(4,"python")
lb1.insert(5,"sql")
lb1.insert(6,"git")
lb1.insert(7,"github")
lb1.insert(8,"html")
lb1.insert(9,"css")
lb1.insert(10,"javascript")
lb1.insert(11,"mongodb")
lb1.place(x=120,y=50)
karan.mainloop()