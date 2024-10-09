"""
练习01 客户端
"""
from socket import *

# 访问服务器使用的地址
ADDR = ("127.0.0.1", 8888)

# udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 循环输入内容发送
while True:
    word = input("\n要查询的单词:")
    if not word or word == "##":
        break  # 退出标志
    udp_socket.sendto(word.encode(), ADDR)
    data, addr = udp_socket.recvfrom(1024)
    print(word, ":", data.decode())

udp_socket.close()
