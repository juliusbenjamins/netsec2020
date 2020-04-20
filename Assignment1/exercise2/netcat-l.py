#!/usr/bin/env python3

import socket

def handle(sock, i):
    for i in range(0,i):
        data = b""
        newdata = sock.recv(size)
        data += newdata
        if data:
           datastring = data.decode("utf-8")
           print(handlestring(datastring, len("spam "), "\n"))
    sock.close()

def handlestring(datastring, length, delimiter):
    stringlist = datastring.split(sep=delimiter)
    filteredlist = []
    for string in stringlist:
        filteredlist.append(string[length:])
    filteredstring = delimiter.join(filteredlist)
    return filteredstring

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    handle(s, iterations)
    s.close()

if __name__ == "__main__":
    host = "localhost"
    port = 42424
    backlog = 5
    size = 65507 #Max UDP data packet size for IPv4
    iterations = 3 #Amount of messages that want to be received
    main()
