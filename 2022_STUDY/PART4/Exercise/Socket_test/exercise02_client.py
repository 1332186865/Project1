"""
练习2 客户端
"""
from socket import *
from time import sleep

ADDR = ("127.0.0.1",8888) # 服务器地址

def send_image(sock,img):
    fr = open(img,'rb')
    # 边读取边发送
    while True:
        data = fr.read(1024)
        if not data:
            break
        sock.send(data)
    fr.close()
    # 接收通知  -- 上传完成
    sleep(0.1)
    sock.send(b"##")
    print(sock.recv(1024).decode())

def main():
    sock = socket()
    sock.connect(ADDR)
    # 发送图片
    send_image(sock,"/home/tarena/下载/dili.jpeg")
    sock.close()

if __name__ == '__main__':
    main()
