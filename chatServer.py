import socket
import os

host, port = '',6000
s = socket.socket()
s.bind((host,port))
s.listen(5)
print("Ecoute sur {}".format(port))

client, addr = s.accept()
print(str(client) + str(addr))
rcvData = b""
reguserlist =[]
connected = False

while True:
    
    
    rcvData = client.recv(1024)
    print(rcvData.decode())
    if rcvData.decode() == "clients" :
        if len(reguserlist) == 0 :
            client.send("none".encode())
        else :
            list2str = ""
            for users in reguserlist :
                list2str += str(users) + "\n"
            client.send(list2str.encode())
    elif rcvData.decode() == "chat" :
        if connected :
            client.send("chat openned".encode())
            os.system("chat_V1.py")
        else :
            client.send("not connected".encode())
    elif rcvData.decode() == "connection" :
        client.send("well connected".encode())
        connected = True
        reguserlist.append(socket.gethostbyaddr(addr[0]))
    elif rcvData.decode() == "deconnection" :
        client.send("well deconnected".encode())
        reguserlist.remove(socket.gethostbyaddr(addr[0]))
        connected = False
    else :
        client.send(b'unknown command')
    
client.close()
s.close()
