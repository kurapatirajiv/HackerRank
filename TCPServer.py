# Program : To convert Lower case message typed from client to upper case using socket programming

# Note : "import socket" is different to "from socket import *" if we are 
# using the first one we have to mention the method name 

import socket
serverPort = 8080serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)serverSocket.bind(('', serverPort))  # binds address (hostname, port number pair) to socket
serverSocket.listen(1) # The server has created a door to communicate and is ready to accept new connectionsprint "The server is ready to receive"while 1:
    connectionSocket, addr = serverSocket.accept()  # Accepting new connections    message = connectionSocket.recv(2048)    modifiedMessage = message.upper()    connectionSocket.send(modifiedMessage)    connectionSocket.close()