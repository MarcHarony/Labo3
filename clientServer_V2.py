import socket
import os

host = "localhost" #changer localhost par l'ipv4 de la machine sur laquelle se trouve le serveur
port = 6000

t=socket.socket()
t.connect((host,port))

print("connecté au server sur le port {}".format(port))

sendata = b""

while True:
    sendata = input("> ")
    sendata = sendata.encode()
    t.send(sendata)
    recvdata = t.recv(1024)
    print(recvdata.decode())
    if recvdata.decode() == "chat openned" :
        os.system("chat_V2.py")

t.close()
