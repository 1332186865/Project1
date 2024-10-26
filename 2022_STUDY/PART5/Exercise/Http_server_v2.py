#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
from socket import *

import select


class HTTPServer:
    def __init__(self, server_address, static_dir):
        self.rlist = self.xlist = self.wlist = []
        self.server_address = server_address
        self.static_dir = static_dir
        self.create_socket()
        self.bind()

    def create_socket(self):
        """创建套接字"""
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.port = self.server_address[1]

    def server_forever(self):
        """启动服务"""
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select.select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from", addr)
                    self.rlist.append(c)
                else:
                    self.handle(r)

    def handle(self, connfd: socket):
        request = connfd.recv(4096)
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return

        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd)
        self.rlist.remove(connfd)
        connfd.close()

    def get_html(self, connfd, info):
        """处理网页"""
        if info == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + info
        try:
            fd = open(filename, 'r', encoding='utf-8')
        except Exception:
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += '\r\n'
            responseBody = "<h1>Sorry, Not Found The Page<h1>"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            responseBody = fd.read(1024)
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self, connfd):
        responseHeaders = "HTTP/1.1 200 OK\r\n"
        responseHeaders += '\r\n'
        responseBody = "<h1>Waiting httpserver 3.0<h1>"
        response = responseHeaders + responseBody
        connfd.send(response.encode())


if __name__ == '__main__':
    server_addr = ('127.0.0.1', 8000)
    static_dir = './static'

    httpd = HTTPServer(server_addr, static_dir)
    httpd.server_forever()
