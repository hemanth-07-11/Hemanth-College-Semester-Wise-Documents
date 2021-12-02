#!/usr/bin/env python3
import sys,os
from socket import *

if(len(sys.argv)!=4):
	print('You must give exactly three arguments: remote IP/server name, remote Port, and file to transfer.')
	sys.exit()
	
ipAdd = sys.argv[1] 
portNum = int(sys.argv[2]) 
fileName = str(sys.argv[3]) 

try:
	oldFile = open(fileName,'rb')
except:
	print('There was a problem opening the file to copy.')
	sys.exit()

try:
	clientSocket = socket(AF_INET,SOCK_STREAM)
	clientSocket.connect((ipAdd,portNum))
except:
	print('There was a problem establishing the connection, is the server ready to receive?')
	sys.exit()

fileSize = os.path.getsize(fileName).to_bytes(4,byteorder='big')
clientSocket.send(fileSize)

fileName = fileName.rjust(20)
clientSocket.send(fileName.encode('ASCII'))

try:
	readBytes = oldFile.read(500)
	while (readBytes):
		clientSocket.send(readBytes)
		readBytes = oldFile.read(500)
except:
	print('There was an error sending part of the file to '+ ipAdd)

print('File successfully transferred. Yayyy !!! ')

oldFile.close()
clientSocket.close()
