from socket import *
import sys

# webclient.py <server_host> <server_port> <filename>

print(sys.argv)
serverName = sys.argv[1]
serverPort = sys.argv[2]
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, int(serverPort)))
output = "GET /" + sys.argv[3] + " HTTP/1.1\r\n" + "Host: " + serverName + ":" + sys.argv[2] + "\r\n" + "Accept: text/html\r\n"
print(output)
clientSocket.send(output.encode())

modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()