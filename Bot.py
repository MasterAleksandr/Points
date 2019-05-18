from Coordinates import Coordinate


class Bot:
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
