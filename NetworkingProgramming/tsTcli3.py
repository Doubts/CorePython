#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFFERSIZE = 1024
ADDR = (HOST, PORT)


tcpCliSocket = socket(AF_INET, SOCK_STREAM)
tcpCliSocket.connect(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    tcpCliSocket.send(data.encode('utf-8'))
    data = tcpCliSocket.recv(BUFFERSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSocket.close()