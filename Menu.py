from tkinter import *
from PIL import Image
import  os

from PIL import Image, ImageTk

def on_click(i, j, event):
    root.destroy()
    import Mode

root = Tk()
root.title("Battle of magic crystals")
root.resizable(width=False, height=False)
menuPng = ImageTk.PhotoImage(Image.open("Menu.png"))
cell = Label(root, image=menuPng , bg="black")
cell.grid(row=0, column=0)
cell.bind('<Button-1>', lambda e, i=0, j=0: on_click(i, j, e))

root.mainloop()