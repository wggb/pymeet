from enum import Flag
from socket import socket, AddressFamily, SocketKind

class connection:
    def __init__(
        self, 
        ip = '51.178.215.202', 
        port = 12000, 
        buffer_size =  1024 * 64):
        
        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.server = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM, 0)

    def send(self, data, encode = True):
        if (encode):
            data = data.encode('utf-8')
        self.server.sendto(data, (self.ip, self.port))
        print(f"Client Sent data of length : {len(data)}")

    def recv(self, decode = True):
        data, address = self.server.recvfrom(self.buffer_size)
        if decode:
            data = data.decode('utf-8')
        print(f"Client received data of length : {len(data)}")
        return data
        
    def close(self):
        self.server.close()
