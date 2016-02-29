# Program : To convert Lower case message typed from client to upper case using socket programming
# Note : "import socket" is different to "from socket import *" if we are 
# using the first one we have to mention the method name 

import socket
serverName = 'localhost'
serverPort = 8080
clientSocket = socket.socket(socket.AF_INET, # Internet
                   socket.SOCK_STREAM) # TCP
clientSocket.connect((serverName,serverPort))
while 1:
	message = raw_input();
	if(message == "bye"):
		clientSocket.send(message)
		print clientSocket.recv(2048);
		clientSocket.close()
		break
	else:
		clientSocket.send(message)
		serverMessage = clientSocket.recv(2048)  # 2048 is the message buffersize
		print serverMessage



