from http import server
import socket
import threading

PORT = 3030
SERVER = socket.gethostbyname(socket.gethostname())

print(SERVER)