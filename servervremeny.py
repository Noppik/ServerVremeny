import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 123))
lie_time = 0
with open("lietime.txt", "r") as f:
    lie_time = int(f.readline())
while True:
    data, address = server.recvfrom(1024)
    server.sendto(bytes(time.ctime(time.time() + lie_time), encoding="utf8"), address)
