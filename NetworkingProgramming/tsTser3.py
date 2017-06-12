#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSocket = socket(AF_INET, SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSocket, addr = tcpSerSocket.accept()
    print("...connected from: ", addr)

    while True:
        data = tcpCliSocket.recv(BUFFERSIZE)
        if not data:
            break
        # tcpCliSocket.send("[%s] %s" % (bytes(ctime(), 'utf-8')), data)
        tcpCliSocket.send(("[%s] %s" % (ctime(), data)).encode('utf-8'))

    tcpCliSocket.close()

tcpSerSocket.close() # will not run