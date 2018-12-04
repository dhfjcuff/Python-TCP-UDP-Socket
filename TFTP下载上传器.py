# -* encoding:utf-8 -*-
from socket import *
import struct
import time
"""实现从ftp服务器下载文件，主要联系协议的通信过程
协议的格式转化
文件传输与下载的实质
以及发送请求的格式要求极转化
疑问：ftp服务器发送文件给客户端时候，客户端没有绑定端口是怎么实现通信的
"""


def download():
    UdpSocket = socket(AF_INET, SOCK_DGRAM)
    name = input('请输入你要下载的文件名（全称）：')
    filename = bytes(name, encoding="utf8")
    # print(filename)
    cmd_buf = struct.pack("!H%ssb5sb"%len(filename), 1, filename, 0, b"octet", 0)
    sendAdd = ('192.168.1.4', 69)
    UdpSocket.sendto(cmd_buf, sendAdd)   # 发送请求

    while True:
        data, IP = UdpSocket.recvfrom(1024)
        cmd_ack = struct.unpack("!HH", data[:4])    # 数据包解包
        kuaibianhao = cmd_ack[1]  # 块编号
        print(len(data[4:]))
        if len(data[4:]) <= 512:
            if kuaibianhao == 1:
                file = open(name, 'wb')
            file.write(data[4:])
            print('写入%s'%kuaibianhao)

        if len(data[4:])<512:
            file.close()
            print('完成')
            break
        ack = struct.pack("!HH", 4, kuaibianhao)
        UdpSocket.sendto(ack, IP)    # 确认数据包)
    UdpSocket.close()


if __name__ == "__main__":
    download()

