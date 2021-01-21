from SocketServer import TCPServer, BaseRequestHandler
class myHandler(BaseRequestHandler):
    def handle(self):
        print "Connection from ", str(self.client_address)
        while True:
            data = self.request.recv(1024)
            if data == "bye\r\n": break
            data_oper = data.split(" ")
            if data_oper[1] == "+":
                res = int(data_oper[0]) + int(data_oper[2])
            elif data_oper[1] == "-":
                res = int(data_oper[0]) - int(data_oper[2])
            elif data_oper[1] == "*":
                res = int(data_oper[0]) * int(data_oper[2])
            if data_oper[1] == "/":
                res = int(data_oper[0]) / int(data_oper[2])
            self.request.send(str(res)+"\n")
        self.request.close()

myServer = TCPServer(("127.0.0.1", 3455), myHandler)
myServer.serve_forever()
