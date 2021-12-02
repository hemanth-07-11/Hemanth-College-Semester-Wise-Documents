import socket
import threading
import time 

threadLock = threading.Lock()
shutdown = False

def receiving(name, sock):
    while not shutdown:
        try:
            threadLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print (str(data))
        except:
            pass
        finally:
            threadLock.release()

def sending(name, sock):
    while not shutdown:
        try:
            threadLock.acquire()
            while True:
                 data, addr = sock.sendmsg(1024)
        except:
            pass
        finally:
            threadLock.release()

host = '127.0.0.1'
port = 0
server = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rThread = threading.Thread(target=receiving, args=("RecvThread", s))
rThread.start()

sThread = threading.Thread(target=sending, args=("SendThread", s))
sThread.start()

alias = input("Please enter your name:")
s.sendto(bytes(alias + " has entered the chat.",'utf-8'), server)
time.sleep(0.3)

message = input('You: ')

while message != '!Quit':
    if message != '':

        s.sendto(bytes(alias + ": " + message, 'utf-8'), server)
        time.sleep(0.3)

    message = input('>> ')
   
s.sendto(bytes(alias + " has left the chatroom.", 'utf-8'), server)
shutdown = True

rThread.join()
sThread.join()
s.close()
