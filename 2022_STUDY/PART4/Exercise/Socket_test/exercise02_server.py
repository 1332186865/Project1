"""
练习02：tcp完成

从客户端上传一张照片到服务端，上传完成后
两边都结束即可

图片自选，服务端保存为 "20211209.jpeg"
"""
from socket import *

def recv_image(conn):
    fw = open("20211209.jpeg",'wb')
    # 边接收边写入
    while True:
        data = conn.recv(1024)
        if data == b"##":
            break # 客户端发送完断开连接
        fw.write(data)
    fw.close()
    conn.send("上传成功".encode())

def main():
    # 创建套接字
    sock = socket()
    sock.bind(("0.0.0.0",8888))
    sock.listen(5)
    # 接收连接
    conn,addr = sock.accept()
    print("Connect from",addr)
    # 做事情函数 : 接收图片
    recv_image(conn)
    conn.close()
    sock.close()



if __name__ == '__main__':
    main()




