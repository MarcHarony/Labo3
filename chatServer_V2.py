import socket
import select
import os

host = ''
port = 6000

s= socket.socket()
s.bind((host, port))
s.listen(5)
print("Ecoute sur {}".format(port))

reguser = []
reguserlist = []

while True:
    waitingConnections, wlist, xlist = select.select([s],[], [], 0.05)
    for connection in waitingConnections :
        client, addr = connection.accept()
        reguser.append(client)
    waitingClients = []
    try:
        waitingClients, wlist, xlist = select.select(reguser,[], [], 0.05)
    except select.error:
        pass
    else:
        for user in waitingClients:
            try :
                rcvData = user.recv(1024).decode()
                print(rcvData)
                if rcvData == "clients" :
                    if len(reguserlist) == 0 :
                        user.send("none".encode())
                    else :
                        list2str = ""
                        for users in reguserlist :
                            list2str += str(users) + "\n"
                        user.send(list2str.encode())
                elif rcvData == "chat" :
                    if socket.gethostbyaddr(addr[0]) in reguserlist :
                        user.send("chat openned".encode())
                        os.system("chat_V1.py")
                    else :
                        user.send("not connected".encode())
                elif rcvData == "connection" :
                    user.send("well connected".encode())
                    reguserlist.append(socket.gethostbyaddr(addr[0]))
                elif rcvData == "deconnection" :
                    user.send("well deconnected".encode())
                    reguserlist.remove(socket.gethostbyaddr(addr[0]))
                else :
                    user.send(b'unknown command')
            except OSError :
                pass
                

print("Fermeture des connexions")
for user in reguser:
    user.close()

s.close()
