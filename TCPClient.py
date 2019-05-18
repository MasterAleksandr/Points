import socket
import Game
import Click


class Client:
    conn = socket.socket()
    conn.connect("212.193.78.200", 14900)
    data = conn.recv(1024)
    board = Click.Click.cod_map_to_string(Game.board)
    conn.send(board)
