import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.sendto(b"", ('localhost', 123))
data, address = server.recvfrom(1024)
print(data)
server.close()
