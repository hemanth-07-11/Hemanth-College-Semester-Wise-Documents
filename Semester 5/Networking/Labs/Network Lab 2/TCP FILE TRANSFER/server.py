#!/usr/bin/env python3
import sys,os
from socket import *

if(len(sys.argv)!=2):
	print('You must supply exactly one argument: local port number')
	sys.exit()

try:	
	if not (int(sys.argv[1]) in range(1,65535)):
		print('Your port number must an integer within 1 and 65535.')
		sys.exit()
except:
	print('Your port number must an integer within 1 and 65535.')
	sys.exit()
	
serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET,SOCK_STREAM)

try: 
	serverSocket.bind(('',serverPort))
except:
	print('There was a problem binding a socket to your port.')
	sys.exit()

serverSocket.listen(1)
print('Server successfully initialized and ready to receive.')
connectionSocket, addr = serverSocket.accept()

numBytes = connectionSocket.recv(4)
numBytes = int.from_bytes(numBytes,byteorder='big')
fileName = connectionSocket.recv(20)
fileName = fileName.decode('ASCII').strip()

subDir = os.path.join(os.getcwd(),'recv') #
pathToNewFile = os.path.join(subDir,str(fileName)) 

if not (os.path.exists(subDir)):
	try:
		os.makedirs(subDir) 
	except:
		print('There was a problem creating the directory for the new file. Terminating program.')

try:
	newCopy = open(pathToNewFile,'wb')
except:
	print('There was a problem writing a new file to '+ pathToNewFile)
while numBytes > 500:
	partialFile = connectionSocket.recv(500)
	newCopy.write(partialFile)
	numBytes-=500;

if numBytes > 0:
	partialFile = connectionSocket.recv(numBytes)
	newCopy.write(partialFile)

print('File transfer complete. File is located at: '+ pathToNewFile)
newCopy.close()
connectionSocket.close()
serverSocket.close()
