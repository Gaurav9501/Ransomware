#!/usr/bin/env python3

import socket

def some(i):
	HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
	PORT = 65435        # Port to listen on (non-privileged ports are > 1023)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.bind((HOST, PORT))
	    s.listen()
	    conn, addr = s.accept()
	    with conn:
	    	print('Connected by', addr)
	    	data = conn.recv(1024)
	    	print(data)
	s.close()

some(8989)
