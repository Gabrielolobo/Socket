from email import message
from http import client
import socket


HEADER = 64 #No. of Bits
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 3030
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!QUIT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) #connects to server

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Do or do not, there is no try.")
send("SAY HELLO TO MY LITTLE FRIEND!")
send("You broke my heart, Fredo... You broke my heart.")
send(DISCONNECT_MESSAGE)