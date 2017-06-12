#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFFERSIZE)
    udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode('utf-8'), addr)
    print('...received form and returned to : ', addr)

udpSerSock.close()
