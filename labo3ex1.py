import socket
s = socket.socket()
s.connect(('www.vinci.be',80))
print(s.getsockname())
data = "GET / HTTP/shit1.0\n\n".encode()
sent = s.send(data)
if sent == len(data) :
    print("ok")
recep = s.recv(4096).decode()
print('reçu', len(recep), 'octets :')
print(recep)
s.close()
