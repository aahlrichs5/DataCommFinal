# import socket module
from socket import *
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
TCP_PORT = 8000
BUFFER_SIZE = 1024

serverSocket.bind(('', TCP_PORT))
serverSocket.listen(1)

while True:
 	# Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept()
    print('Connection address:', addr)
    try:
        message =  connectionSocket.recv(BUFFER_SIZE)
        filename = message.split()[1]
 		f = open(filename[1:])
        outputdata =  f.read()
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n')

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
sys.exit()#Terminate the program after sending the corresponding data
