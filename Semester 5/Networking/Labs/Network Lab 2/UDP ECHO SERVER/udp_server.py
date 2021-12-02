import socketserver

class UDPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        data = self.request[0]
        socket= self.request[1]
        print("{} wrote: ".format(self.client_address[0]))
        print(data)
        data = str(data.decode('utf8'))
        data = data.upper()
        data = bytes(data,'utf8')
        socket.sendto(data,self.client_address)

if __name__=="__main__":
    HOST,PORT = "localhost",5120
    server = socketserver.UDPServer((HOST,PORT),UDPHandler)
    server.serve_forever()
