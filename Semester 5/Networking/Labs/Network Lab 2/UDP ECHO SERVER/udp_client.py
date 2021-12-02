import socket
import sys

PORT = 5120
data = bytes( ' ','utf8')
try:
    sys.argv[1]
except IndexError:
    HOST = 'localhost'
else:
    HOST = sys.argv[1]
while data.decode('utf8') != 'Bye.':
    data = bytes(input(">> "),'utf8')
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.sendto(data, (HOST,PORT))
    received = my_socket.recv(1024)


    print("Client said: {}".format(data.decode('utf8')))
    print("Server said: {}".format(received.decode('utf8')))
else:
    print("\nokay yayy!\n")
    SystemExit
