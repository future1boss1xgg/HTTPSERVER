from socketserver import *

# 创建服务器类
class Server(ThreadingMixin,TCPServer):
    pass

class Handler(DatagramRequestHandler):
    def handler(self):
        while True:
            data=self.rfile.readline()
            print(self.client_address)
            if not data:
                break
            print(data.decode())
            self.wfile.write(b'Receive',addr)

if __name__=='__main__':
    server_addr=('0.0.0.0',8888)

    # 创建服务器对象
    server=Server(server_addr,Handler)
    # 启动服务器
    server.seve_forever()