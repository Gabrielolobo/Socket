from http import server
import socket
import threading

PORT = 3030
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 128 #No. of Bits
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!QUIT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def start():#Allows code to start listening for connections.
    server.listen()
    print(f"[RUNNING] Server is Running on {SERVER}")
    while True:
        #Stores client's information.
        addr, conn = server.accept()
        thread = threading.Thread(target=client_manager, args=(addr, conn))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}") #The ("number of threads" - 1) represents the number of connections to the server.

def client_manager(addr, conn):
    print(f"[NEW CONNECTION] {addr} is connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #Tells how long the message is.
        if msg_length:
            msg_length = int(msg_length) #Converts to an integer
            msg = conn.recv(msg_length).decode(FORMAT) #How many bytes per message.
            if msg == DISCONNECT_MESSAGE:
                connected = False
        
            print(f"[{addr}] {msg}")
        
    conn.close()


print("[STARTING SERVER...]")
start()
