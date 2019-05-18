from PIL import Image, ImageTk
import Bot
from TCPClient import Client


countOfPoints = 0
WIDTH = 12
HEIGHT = 12


class Click:
    WIDTH = 12

    def on_click(i, j, event, board, cells):
        global countOfPoints
        if board[i][j] == None:
            point = ImageTk.PhotoImage(Image.open("bluePoint.png"))
            event.widget.config(image=point)
            board[i][j] = point
            countOfPoints += 1
            Client.send(board)
            board = Click.decode_string_to_map(Client.listen())
            Click.draw_board(board, cells)
            countOfPoints += 1
            '''check_end_game(countOfPoints)'''
            print(countOfPoints)

    def draw_board(self, board, cells):
        ping = ImageTk.PhotoImage(Image.open("pingPoint.png"))
        empty = ImageTk.PhotoImage(Image.open("mainEmpty.png"))
        blue = ImageTk.PhotoImage(Image.open("bluePoint.png"))
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if board[i][j] == None:
                    cells[i][j].config(image = empty)
                if board[i][j] == ping:
                    cells[i][j].config(image = ping)
                if board[i][j] == blue:
                    cells[i][j].config(image = blue)

    def cod_map_to_string(self, board):
        map_string = ""
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if board[i][j] == None:
                    map_string += " "
                if board[i][j] == ImageTk.PhotoImage(Image.open("pingPoint.png")):
                    map_string += "p"
                else:
                    map_string += "b"
        return map_string

    def decode_string_to_map(self, string):
        board = [[None] * HEIGHT for _ in range(WIDTH)]
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if string[i + j] == " ":
                    board[i][j] = None
                if string[i + j] == "p":
                    board[i][j] = ImageTk.PhotoImage(Image.open("pingPoint.png"))
                if string[i + j] == "b":
                    board[i][j] = ImageTk.PhotoImage(Image.open("bluePoint.png"))
        return board


'''def check_end_game(count):
    if count == WIDTH * HEIGHT:
        quit()
        endMess = Tk()
        endMess.resizable(width=False, height=False)
        mess = Label(endMess, image=endGame1, bg="black")
        mess.pack()
        endMess.mainloop()'''
