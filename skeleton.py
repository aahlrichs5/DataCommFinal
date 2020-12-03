# import socket module
from socket import *
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
SERVER_HOST = '192.168.56.1'
# Prepare a sever socket
TCP_PORT = 8000
BUFFER_SIZE = 1024

serverSocket.bind((SERVER_HOST, TCP_PORT))
serverSocket.listen(5)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connection address:', addr)
    try:
        message = connectionSocket.recv(BUFFER_SIZE)
        filename = message.split()[1]
        f = open(filename[1:'index.html'])
        outputdata = f.read()
        print(outputdata)
        # Send one HTTP header line into socket
        connectionSocket.send(bytes('HTTP/1.0 200 OK\r\n'))
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        fail = '''<html> <head> <title> 404 </title> </head> <body><h1>404 Bruh</h1> <h3> hushies! </h3> </body></html>'''
        connectionSocket.send('HTTP/1.0 200 OK\r\n')
        for q in fail:
            connectionSocket.send(q)
            # Close client socket
     # Fill in start
            # Fill in end
    serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
