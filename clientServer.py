import socket
import os

host = "localhost"
port = 6000

t=socket.socket()
t.connect((host,port))

print("connecté au server sur le port {}".format(port))

sendata = b""

while sendata != b"fin":
    sendata = input("> ")
    sendata = sendata.encode()
    t.send(sendata)
    recvdata = t.recv(1024)
    print(recvdata.decode())
    if recvdata.decode() == "chat openned" :
        os.system("chat_V1.py")

t.close()
