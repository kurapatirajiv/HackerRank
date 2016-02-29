# Program : Chat with a client using socket programming

import socket
serverPort = 8080serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)serverSocket.bind(('', serverPort))  # binds address (hostname, port number pair) to socket
serverSocket.listen(1) # The server has created a door to communicate and is ready to accept new connectionsprint "The server is ready to receive"
connectionSocket, addr = serverSocket.accept()  # Accepting new connectionswhile 1:        message = connectionSocket.recv(2048)
    if (message == "bye"):
		print "What? It's so early, but if you insist! bye."
		connectionSocket.close()
		break
    else:		print "Client : " + message      		connectionSocket.send(raw_input());