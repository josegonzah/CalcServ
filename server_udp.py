from SocketServer import UDPServer, BaseRequestHandler

class myHandler(BaseRequestHandler):
    def handle(self):
        print "Connection from ", str(self.client_address)
        data, conn = self.request
        data_oper = data.split(" ")
        if data_oper[1] == "+":
            res = int(data_oper[0]) + int(data_oper[2])
        elif data_oper[1] == "-":
            res = int(data_oper[0]) - int(data_oper[2])
        elif data_oper[1] == "*":
            res = int(data_oper[0]) * int(data_oper[2])
        if data_oper[1] == "/":
            res = int(data_oper[0]) / int(data_oper[2])
        conn.sendto(str(res)+"\n", self.client_address)

myServer = UDPServer(("127.0.0.1", 5555), myHandler)
myServer.serve_forever()