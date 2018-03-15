import socket

host = "localhost"
port = 6000

t=socket.socket()
t.connect((host,port))

print("connecté au serveur sur le port {}".format(port))

sendata = b""

while True:
    sendata = input("> ")
    sendata = sendata.encode()
    t.send(sendata)
    recvdata = t.recv(1024)
    print(recvdata.decode())

t.close()
