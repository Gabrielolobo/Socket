from http import server
import socket
import threading

PORT = 3030
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#Allows code to start listening for connections.
def start():
    socket.listen()
    while True:
        addr, conn = server.accept()

def client_manager(addr, conn):
    pass

print("[STARTING SERVER...]")
start()
