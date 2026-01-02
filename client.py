#!/usr/bin/env python3

import socket
socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM) 
HOST = str(input("What host do you want to connected for test (leave empty for localhost): "))
PORT = input("What port do you want acess to connect: ")

if HOST == "":
    HOST = "127.0.0.1"

if PORT == "":
    print("Port cannot be empty.")
    exit(1)

PORT = int(PORT)


socket.connect((HOST, PORT))

while True:
    msg = input("Type your mensage:\n")
    socket.send(msg.encode())