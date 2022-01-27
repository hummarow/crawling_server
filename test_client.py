import socket

server_addr = "192.168.0.66"
server_port = 1234
bufferSize = 1024

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

client_socket.sendto(str.encode("Hi, I am client."), (server_addr, server_port))

msg = client_socket.recvfrom(bufferSize)

print(msg[0])