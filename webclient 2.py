from socket import *


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send("GET /HelloWorld.html HTTP/1.1\r\n".encode())
clientSocket.send("Host: 10.0.0.253:65012\r\n".encode())
clientSocket.send("Accept: text/html\r\n".encode())

modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()