from PIL import Image, ImageTk
import Bot

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
            point = pingPoint = ImageTk.PhotoImage(Image.open("pingPoint.png"))
            coordinate = Bot.Bot.MarkPoint(i, j, board, 12, 12)
            board[coordinate.x][coordinate.y] = pingPoint
            cells[coordinate.x][coordinate.y].config(image=point)
            countOfPoints += 1
            '''check_end_game(countOfPoints)'''
            print(countOfPoints)

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
