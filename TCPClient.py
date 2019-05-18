import socket
import Game
import Click


class Client:
    conn = socket.socket()
    conn.connect("212.193.78.200", 14900)
    data = conn.recv(1024)
    def send(self, board):
        conn = socket.socket()
        conn.connect("212.193.78.200", 14900)
        board = Click.Click.cod_map_to_string(board)
        conn.send(board)
    def listen(self):
        conn = socket.socket()
        conn.connect("212.193.78.200", 14900)
        data = conn.recv(8000)
        return data.decode("utf-8")