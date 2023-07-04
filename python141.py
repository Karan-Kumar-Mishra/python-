import tkinter as tk
karan=tk.Tk()
karan.geometry("400x400")
btn= tk.Button(text="Exit",width=5,command=karan.destroy)
btn.place(x=160,y=160)
karan.mainloop()