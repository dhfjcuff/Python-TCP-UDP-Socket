import sys
import time
import gevent
from gevent import socket, monkey
monkey.patch_all()


def newsock(conn):
    while True:
        data = conn.recv(1024)
        if len(data) > 0:
            print('有消息：%s'%data)
        else:
            print('关闭一个连接')
            break
            conn.close()
        conn.send(data)


def sock():
    s = socket.socket()
    s.bind(('', 8899))
    s.listen(5)
    while True:
        cli, addr = s.accept()
        print('有新连接加入%s'%str(addr))
        gevent.spawn(newsock, cli)


if __name__ == '__main__':
    sock()

