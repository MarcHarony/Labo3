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
pseudoList = []

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
                        j=0
                        for users in reguserlist :
                            list2str += str(users) + " : " + pseudoList[j] + "\n"
                            j+=1
                        user.send(list2str.encode())
                elif rcvData == "chat" :
                    if socket.gethostbyaddr(addr[0]) in reguserlist :
                        user.send("chat openned".encode())
                    else :
                        user.send("not connected".encode())
                elif "connection" in rcvData and "de" not in rcvData :
                    user.send("well connected".encode())
                    reguserlist.append(socket.gethostbyaddr(addr[0]))
                    tokens = rcvData.split(' ')
                    i=1
                    pseudo=""
                    while i<len(tokens) :
                        pseudo += tokens[i] + ' '
                        i+=1
                    print("pseudo : " + pseudo)
                    pseudoList.append(pseudo)
                    
                elif rcvData == "deconnection" :
                    user.send("well deconnected".encode())
                    k=0
                    pseudoIndex = 0
                    for users in reguserlist :
                        if socket.gethostbyaddr(addr[0]) == users :
                            pseudoIndex =k
                        else :
                            k+=1
                    reguserlist.remove(socket.gethostbyaddr(addr[0]))
                    pseudoList.remove(pseudoList[k])
                    print(pseudoList)
                    
                else :
                    user.send(b'unknown command')
            except OSError :
                pass
                

print("Fermeture des connexions")
for user in reguser:
    user.close()

s.close()
