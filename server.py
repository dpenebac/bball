import socket
import threading
import bball
from bball import *

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
f = open("basket.txt","w")

def connect():
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target = sendInfo,args = (conn,addr))
        clients.append(conn)
        thread.start()
        print("Connection Enabled")

def sendInfo(conn,addr):
    while True:
        data = conn.recv(1024).decode(FORMAT)
        f.write(data,"\n")

connect()