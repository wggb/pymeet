# this code will be run on remote server

from socket import socket, AddressFamily, SocketKind

BUFFER_SIZE = 1028 * 64
ip = '51.178.215.202'
port = 12000

# create and bind socket
s = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
s.bind((ip, port))

try:
    while True:
        msg, addr = s.recvfrom(BUFFER_SIZE)
        print(len(msg))
        s.sendto(msg, addr)

except KeyboardInterrupt:
    s.close()
