import tkinter as tk
from tkinter import *
from tkinter import filedialog



notepad=tk.Tk()
def openfile():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_box.delete('1.0', END)
            text_box.insert('1.0', text)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            text = text_box.get('1.0', END)
            file.write(text)          

 

notepad.title("Notepad")
notepad.geometry("1400x700")
menu=Menu(notepad)
notepad.config(menu=menu)
filemenu=Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_cascade(label='New tab')
filemenu.add_cascade(label='New')
filemenu.add_cascade(label='Open',command=openfile)
filemenu.add_cascade(label='Save')
filemenu.add_cascade(label='Save as',command=save_file)
filemenu.add_cascade(label='Save all',command=save_file)
filemenu.add_separator()
filemenu.add_cascade(label='Page setup')
filemenu.add_cascade(label='Print')
filemenu.add_separator()
filemenu.add_cascade(label='Close tab')
filemenu.add_cascade(label='Close windows')
filemenu.add_cascade(label='Exit',command=notepad.destroy)

Edit=Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=Edit)
Edit.add_cascade(label='Undo')
Edit.add_cascade(label='Copy')
Edit.add_cascade(label='Paste')
Edit.add_cascade(label='Delete')
Edit.add_cascade(label='Find')
Edit.add_cascade(label='Find next')
Edit.add_cascade(label='Find previus')
Edit.add_cascade(label='Replace')
Edit.add_cascade(label='Go to')
Edit.add_cascade(label='Select all')
Edit.add_cascade(label='Time/Date')
Edit.add_cascade(label='Font')

View=Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=View)
View.add_cascade(label='Zoom')
View.add_cascade(label='Status bar')
View.add_cascade(label='Word warp')


















text_box = tk.Text(notepad, width=150, height=90)
text_box.pack()
text_box.configure(font=3)




notepad.mainloop()