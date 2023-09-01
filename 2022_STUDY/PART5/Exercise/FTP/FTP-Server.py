#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import os
import time
from socket import *
from threading import Thread

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)
FTP = "/Project1/2022_STUDY/PART5/Exercise/FTP/"


class FTPServer:
    """客户端请求功能"""

    def __init__(self, connfd: socket, FTP_PATH):
        self.connfd = connfd
        self.path = FTP_PATH

    def do_list(self):
        """获取文件列表"""
        files = os.listdir(self.path)
        if not files:
            self.connfd.send("该文件列表为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(.1)

        fs = ''
        for file in files:
            if file[0] != '.' and os.path.isfile(self.path + file):
                fs += file + '\n'
        self.connfd.send(fs.encode())

    def do_get(self, filename):
        try:
            fd = open(self.path + filename, 'rb')
        except Exception:
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(.1)
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self, filename):
        if os.path.exists(self.path + filename):
            self.connfd.send("该文件已存在".encode())
            return
        self.connfd.send(b'OK')
        with open(self.path + filename, 'wb') as fd:
            while True:
                data = self.connfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)


def handle(connfd):
    """客户端处理函数"""
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + '/'
    ftp = FTPServer(connfd, FTP_PATH)
    while True:
        # 接受客户端请求
        data = connfd.recv(1024).decode()
        if not data or data[0] == "Q":
            return
        elif data[0] == "L":
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[0] == 'P':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)


def main():
    """网络搭建"""
    s = socket()  # TCP套接字
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    print("Listen to the port 8888...")

    # 循环等待客户端连接
    while True:
        try:
            connfd, addr = s.accept()
        except KeyboardInterrupt:
            print("Server Exit...")
            return
        except Exception as e:
            print(e)
            continue
        print("连接的客户端：", connfd)

        # 创建线程处理请求
        client = Thread(target=handle, args=(connfd,))
        client.daemon = True  # 分支线程随主进程退出
        client.start()


if __name__ == '__main__':
    main()
