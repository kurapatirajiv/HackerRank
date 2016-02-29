# Program : To convert Lower case message typed from client to upper case using socket programming

# Note : "import socket" is different to "from socket import *" if we are 
# using the first one we have to mention the method name 

import socket
serverPort = 8080serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)serverSocket.bind(('', serverPort))  # binds address (hostname, port number pair) to socketprint "The server is ready to receive"while 1:    message, clientAddress = serverSocket.recvfrom(2048)    modifiedMessage = message.upper()    serverSocket.sendto(modifiedMessage, clientAddress)