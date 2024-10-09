"""
查询单词服务端
"""
from socket import *

import pymysql


class Dict:
    def __init__(self):
        self.kwargs = {
                "user": "root",
                "password": "Sxxzgyb+3",
                "database": "dict",
                "charset": "utf8mb4"
                }
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭
        self.cur.close()
        self.db.close()

    # 查单词
    def query_word(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        result = self.cur.fetchone()  # (mean,)  None
        if result:
            return result[0]  # (mean,)
        else:
            return "Not Found!"


class DictServer:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.dict = Dict()
        self.sock = self._create_socket()

    def _create_socket(self):
        udp_socket = socket(AF_INET, SOCK_DGRAM)
        udp_socket.bind(self.address)
        return udp_socket

    def close(self):
        # 关闭套接字
        self.dict.close()
        self.sock.close()

    def start(self):
        # 循环先收后发
        while True:
            word, addr = self.sock.recvfrom(1024)
            # 查询单词解释
            mean = self.dict.query_word(word.decode())
            print(f"{addr}: {word.decode()}\t{mean}")
            # 发送解释
            self.sock.sendto(mean.encode(), addr)


if __name__ == '__main__':
    server = DictServer(host="0.0.0.0", port=8888)
    server.start()
    server.close()
