from socket import *
from select import select

ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 注意加上这句表示端口复用，即断开后可以立即使用不用等待2mls时间
ServerSocket.bind(('', 7788))
ServerSocket.listen(9)
list = [ServerSocket]
running = True

while True:
    nweserver, a, b = select(list, [], [])
    for i in nweserver:
        if i == ServerSocket:
            server, adder = ServerSocket.accept()
            list.append(server)
            print('新连接：%s'%str(adder))
        else:
            data = i.recv(1024)
            if len(data) > 0:
                print('收到来自：%s的消息:%s'%(str(adder), data))
            else:
                print('断开连接')
                list.remove(i)
                i.close()