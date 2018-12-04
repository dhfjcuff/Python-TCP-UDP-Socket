from multiprocessing import Pool,Process,Queue,Manager
from threading import Thread,Lock
from socket import *
import time

"""
主要作用是实现多线程套接字通信，即可以发送消息也可以接受消息，最套接字最简单的应用，基于udp通信协议
"""


def reade():
    while True:
        text = eco.recvfrom(1024)
        text, IP = text
        print('\n收到您的消息：', text.decode('gb2312'), end='\n>>')


def write():
    while True:
        text = input('>>')
        eco.sendto(text.encode('gb2312'), (addr, porx))


if __name__ == '__main__':
    addr = input('请输入对方IP地址：')
    porx = int(input('请输入对方端口号：'))
    eco = socket(AF_INET, SOCK_DGRAM)
    eco.bind(('', 6677))
    lock = Lock()
    a = Thread(target=reade,)
    b = Thread(target=write,)
    a.start()
    b.start()

