# Program : To convert Lower case message typed from client to upper case using socket programming
# Note : "import socket" is different to "from socket import *" if we are 
# using the first one we have to mention the method name 

import socket
serverName = 'localhost'
serverPort = 8080
clientSocket = socket.socket(socket.AF_INET, # Internet
                   socket.SOCK_STREAM) # TCP
clientSocket.connect((serverName,serverPort))
message = raw_input('Input lowercase sentence:')
clientSocket.send(message)
modifiedMessage = clientSocket.recv(2048)  # 2048 is the message buffersize
print modifiedMessage
clientSocket.close()


