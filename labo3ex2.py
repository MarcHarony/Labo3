import socket
socks = socket.socket(type = socket.SOCK_DGRAM)
data = "azerty".encode()
sended = socks.sendto(data,('localhost',5000))
if sended == len(data) :
    print('its ok bro')
socks.close()
