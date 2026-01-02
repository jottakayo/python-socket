#!/usr/bin/env python3

import socket

socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM) 
HOST = str(input("What host do you want to test (leave empty for localhost): "))
PORT = input("What port do you want acess: ")

if HOST == "":
    HOST = "127.0.0.1"

if PORT == "":
    print("Port cannot be empty.")
    exit(1)

PORT = int(PORT)

socket.bind((HOST, PORT))
socket.listen()
print(f"Server is listening on {HOST}:{PORT}")

conn, addr = socket.accept()

while True:
    data = conn.recv(1024) 
    if not data: break 
    print ("New mensage from host %s: %s" % (addr, data.decode()))

conn.close()