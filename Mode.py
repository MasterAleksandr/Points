from tkinter import *
from PIL import Image
import  os

from PIL import Image, ImageTk

def on_click(i, j, event):
    root.destroy()
    if(j == 0):
        import Game
    else:
        import Menu

root = Tk()
root.title("Battle of magic crystals")
'''root.resizable(width=False, height=False)'''
pve = ImageTk.PhotoImage(Image.open("Pve.png"))
cell = Label(root, image=pve, bg="black")
cell.grid(row=0, column=0)
cell.bind('<Button-1>', lambda e, i=0, j=0: on_click(i, j, e))
pvp = ImageTk.PhotoImage(Image.open("Pvp.png"))
cellp = Label(root, image=pvp, bg="black")
cellp.grid(row=0, column=1)
cellp.bind('<Button-1>', lambda e, i=0, j=1: on_click(i, j, e))

def newTk():
    return root

root.mainloop()