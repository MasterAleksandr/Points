import socket


sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)
conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()

data1 = conn1.recv(1024)
data2 = conn2.recv(1024)
conn2.send(data2)
conn1.send(data1)