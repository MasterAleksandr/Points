from tkinter import *
from PIL import Image, ImageTk
from Bot import Bot
import socket
from Click import Click
import time

root = Tk()
root.title("Battle of magic crystals")
root.resizable(width=False, height=False)
cellPng = ImageTk.PhotoImage(Image.open("mainEmpty.png"))
pingPoint = ImageTk.PhotoImage(Image.open("pingPoint.png"))
bluePoint = ImageTk.PhotoImage(Image.open("bluePoint.png"))
hp = ImageTk.PhotoImage(Image.open("field.png"))
empty = ImageTk.PhotoImage(Image.open("empty.png"))
hearts = ImageTk.PhotoImage(Image.open("hearts.png"))
WIDTH = 12
HEIGHT = 12
sock = socket.socket()
board = [[None] * HEIGHT for _ in range(WIDTH)]
countOfPoints = 0


def quit():
    root.destroy()


cells = [[None] * HEIGHT for _ in range(WIDTH)]
for i in range(HEIGHT):
    for j in range(WIDTH):
        cell = Label(root, image=cellPng, bg="black")
        cell.grid(row=i, column=j)
        cell.bind('<Button-1>', lambda e, i=i, j=j: Bot.on_click(i, j, e, board, cells))
        cells[i][j] = cell

i = 1
for i in range(HEIGHT):
    cell = Label(root, image=empty, bg="black")
    cell.grid(row=i, column=j + 1)
cell = Label(root, text='hui', image=hp, fg="white", bg="black")
cell.grid(row=0, column=j + 1)

# def find_circle_color(color, newColor):

root.mainloop()
