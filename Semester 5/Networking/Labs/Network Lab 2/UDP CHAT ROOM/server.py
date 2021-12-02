import socket
import time
host = '127.0.0.1'
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False
print("Chat room server started...")

while not quitting:
    try:

        data, addr = s.recvfrom(1024)
        if "!Quit" in str(data):
            clients.remove(addr)

        if addr not in clients:
            s.sendto((bytes("Welcome to the chatroom !!! To leave type !Quit", 'utf-8')), addr)
            clients.append(addr)
                 
        print(time.ctime(time.time()) + str(addr) + ": :" + str(data))

        for client in clients:
            if client != addr:	
                s.sendto(data, client)
    except:
        pass
s.close()
