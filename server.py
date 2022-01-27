import socket

localIP = "192.168.0.66"
localPort = 1234
bufferSize = 1024

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

server.bind((localIP, localPort))

print("Listening...")

while(True):
    bytes = server.recvfrom(bufferSize)
    message = bytes[0]
    addr = bytes[1]
    print(message)
    print(addr)
    server.sendto(str.encode("Received."), addr)
    server.sendto(message, addr)