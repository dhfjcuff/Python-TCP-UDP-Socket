#coding=utf-8
from socket import *
from time import sleep
from multiprocessing import Process
serverSocket = socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)  #注意加上这句表示端口复用，即断开后可以立即使用不用等待3mls时间
serverSocket.bind(('', 6688))
serverSocket.listen(9)
# newserver, adder = serverSocket.accept()


def runing(newserver, adder):
    while True:
        data = newserver.recv(1024)
        if len(data) > 0:
            print('来自 %s 的消息：%s'%(str(adder), data))
        else:
            print('结束一连接')
            break
    newserver.close()


if __name__ == "__main__":    #多进程必须放置在__name__里，不然不会后执行
    while True:
        print(1)
        newserver, adder = serverSocket.accept()
        print(newserver, adder)
        tjz = Process(target=runing, args=(newserver, adder))
        tjz.start()
        # newserver.close()





