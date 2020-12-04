# http://127.0.0.1:8765/index.html

# import socket module
from socket import *
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
SERVER_HOST = '127.0.0.1'
# Prepare a sever socket
TCP_PORT = 8765
BUFFER_SIZE = 1024

serverSocket.bind((SERVER_HOST, TCP_PORT))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connection address:', addr)
    try:
        message = connectionSocket.recv(BUFFER_SIZE)
        filename = message.split()[1]
        f = open('index.html')
        outputdata = f.read()
        print(outputdata)
        # Send one HTTP header line into socket
        connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n', 'UTF-8'))
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(bytes('HTTP/1.1 404 Not Found\r\n\r\n', 'UTF-8'))
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
