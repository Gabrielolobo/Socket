from http import client
import socket


HEADER = 128 #No. of Bits
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 3030
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!QUIT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) #connects to server