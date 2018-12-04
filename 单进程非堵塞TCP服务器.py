from socket import *

ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 注意加上这句表示端口复用，即断开后可以立即使用不用等待3mls时间
ServerSocket.bind(('', 7788))
ServerSocket.listen(9)
ServerSocket.setblocking(False) #设置非堵塞状态
list = []
while True:
    try:
        newsocket, adder = ServerSocket.accept()
    except:
        pass
    else:
        print('上线：%s'%str(adder))
        list.append((newsocket, adder))
        newsocket.setblocking(False)    #设置非堵塞状态

    for i in list:
        a, b = i
        try:
            data = a.recv(1024)
        except:
            pass
        else:
            if len(data) == 0:
                print('%s 下线'%str(b))
                list.remove((newsocket, adder))
                a.close()
            else:
                print('来自%s的消息：%s'%(b, data))




