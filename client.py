import socket


HEADER = 128 #No. of Bits
PORT = 3030
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!QUIT!"
SERVER = socket.gethostbyname(socket.gethostname())

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)