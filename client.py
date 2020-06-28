import socket
import tkinter as tk
from tkinter import *

PORT = 5050
SERVER = "192.168.1.214"
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

class app:
	def __init__(self,master):
		self.master = master
		self.master.attributes('-fullscreen',True)
		self.makeButton = Button(master, text = "Make", height = 30, width = 30, command = lambda: sendData(1))
		self.missButton = Button(master, text = "Miss", height = 30, width = 30, command = lambda: sendData(0))
		self.quitButton = Button(master, text = "Quit", command = lambda: sendData(-1))
		self.makeButton.pack(side = LEFT)
		self.missButton.pack(side = RIGHT)
		self.quitButton.pack()

def sendData(info):
    if info != -1:
        b = info.encode(FORMAT)
        client.send(b)
    else:
        sys.exit()

root = Tk()
gui = app(root)
root.mainloop()