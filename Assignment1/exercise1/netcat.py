#!/usr/bin/env python3

import socket

s = socket.create_connection(("localhost", 42424))

#buf = "\n**********\nHello :^]\n**********\n".encode("utf-8")

stringbuf = ""
for i in range(0, 1000):
    stringbuf = stringbuf + "spam " + str(i) + "\n"

buf = stringbuf.encode("utf-8")

s.sendall(buf)
s.close()
