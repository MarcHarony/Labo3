import socket
class Chat() :
    def __init__(self, host=socket.gethostname(),port=5000):
        s = socket.scoket(type = socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.bind((host,port))
        self.__s=s
    
    def _send(self,param) :
        if self.__address is not None :
            message = param.encode()
            totalsent = 0
            while totalsent < len(message):
                sent = self.__s.sendto(message[totalsent:],self.__address)
                totalsent+=sent
