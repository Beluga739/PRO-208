import socket
from  threading import Thread
import time
import os

IP_ADDRESS = '127.0.0.1'
PORT=8050
SERVER = None
BUFFER_SIZE=4096
clients = {}

def setup():
    print("\n\t\t\t\t\tIP MESSENGER")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(100)

    print("\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")
    acceptConnections()
setup()
def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        print(client.addr)
