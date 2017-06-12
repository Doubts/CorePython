#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("> ")
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, addr = udpCliSock.recvfrom(BUFFERSIZE)
    if not data:
        break
    print(data)

udpCliSock.close()