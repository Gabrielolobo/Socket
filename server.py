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
        #Stores client's information.
        addr, conn = server.accept()
        thread = threading.Thread(target=client_manager, args=(addr, conn))
        thread.start()
        #The ("number of threads" - 1) represents the number of connections to the server.
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

def client_manager(addr, conn):
    print(f"[NEW CONNECTION] {addr} is connected")

    connected = True
    while connected:
        msg = conn.recv()

print("[STARTING SERVER...]")
start()
