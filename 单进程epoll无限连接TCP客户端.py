from select import select
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 7788))
s.listen(5)

epoll=select.epoll()  # 创建epoll
epoll.registre(s.fileno(), select.EPOOLIN|epoll.EPOLLET)  # 将s套接字的文件描述符加入epool，监听事件是收到消息类型，处理事件是一次信息只通知一次

sockdict={}  # 用于储存相应套接字的文件描述符
adderdict={}

while True:
    epool_list = epoll.poll()  # 开始监听，有消息则返回文件描述符及事件类型给列表，然后进行下一轮监听,

    for fd, everts in epool_list:
        if s.fileno() == fd:
            newsock, adder = s.accept()
            print('出现了新的线程：%s'%str(adder))
            sockdict[newsock.fileno] = newsock
            adderdict[newsock.fileno] = adder
            epoll.registre(newsock.fileno(), select.EPOOLIN|epoll.EPOLLET)
        elif everts == select.EPOOLIN:  # 确认事件类型是消息
            data = sockdict[fd].recv(1024)
            if len(data) > 0:
                print('来自%s的消息：%s'%(str(adderdict[fd]), data))

            else:
                epoll.unregister(fd)
                del sockdict[fd]
                del adderdict[fd]
                sockdict[fd].close()
