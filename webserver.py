# Import socket module
from socket import * 
import sys # In order to terminate the program
serverPort = 65012
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Prepare a sever socket
#Fill in start

#Fill in end

while True:
	print('The server is ready to receive')

	connectionSocket, addr = serverSocket.accept()

	try:

		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]
		f = open(filename[1:])

		# send one http header line in to the socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
		outputdata = f.read()
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		
		connectionSocket.close()

	except IOError:
			# Send HTTP response code and message for file not found
			#Fill in start

            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><h1>The page was not found</h1></html>".encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()


			#Fill in end

			# Close the client connection socket
			#Fill in start

			#Fill in end

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data