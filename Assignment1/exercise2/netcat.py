#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#buf = "\n**********\nHello :^]\n**********\n".encode("utf-8")

stringbuf = ""
for i in range(0, 1000):
    stringbuf = stringbuf + "spam " + str(i) + "\n"

buf = stringbuf.encode("utf-8")

sentlength = s.sendto(buf, ("localhost", 42424)) 

if (sentlength < len(buf)):
    print("Error: Data sent is incomplete")
else:
    print("Data succesfully sent")
