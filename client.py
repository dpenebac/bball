import socket

PORT = 5050
SERVER = "192.168.1.214"
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def sendInfo(info):
    b = info.encode(FORMAT)
    client.send(b)

while 1:
    info = input()
    sendInfo(info)