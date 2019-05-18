from Coordinates import Coordinate
from PIL import Image, ImageTk

countOfPoints = 0


class Bot:
    WIDTH = 12

    def on_click(i, j, event, board, cells):
        global countOfPoints
        if board[i][j] == None:
            point = ImageTk.PhotoImage(Image.open("bluePoint.png"))
            event.widget.config(image=point)
            board[i][j] = point
            countOfPoints += 1
            point = pingPoint = ImageTk.PhotoImage(Image.open("pingPoint.png"))
            coordinate = Bot.MarkPoint(i, j, board, 12, 12)
            board[coordinate.x][coordinate.y] = pingPoint
            cells[coordinate.x][coordinate.y].config(image=point)
            countOfPoints += 1
            '''check_end_game(countOfPoints)'''
            print(countOfPoints)

    def MarkPoint(lastX, lastY, board, WIDTH, HEIGHT):
        for dx in range(lastX - 1, lastX + 2):
            for dy in range(lastY - 1, lastY + 2):
                if dy >= 0 and dy < HEIGHT and dx >= 0 and dx < WIDTH:
                    if not (dx == lastX and dy == lastY):
                        if board[dx][dy] is None:
                            return Coordinate(dx, dy)

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if board[i][j] is None:
                    return Coordinate(i, j)
