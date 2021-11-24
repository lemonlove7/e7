# import threading
# import socket
# import queue
# import time
# open_port=[]
# openNum=0
# count=0 #声明全局变量
# def portscan_start(ip):
#     while not q.empty():
#         dict = q.get()
#         #print(dict)
#         try:
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.settimeout(0.1)#设置socket连接超时，避免socket重复操作
#             s.connect((ip, dict))
#             print(f'端口{dict}是打开的')
#             open_port.append(dict)
#         except:
#             pass
#             #print(f'端口{dict}是关闭的')
# def port_run(ip,number):
#     print('[-] 开始端口扫描...')
#     number=int(number)
#     for x in range(number):
#         t = threading.Thread(target=portscan_start, args=(ip,))
#         t.start()
#         t.join()
#
#     time.sleep(2)
#     print('[*] 主机%s共打开了%s个端口' % (ip,len(open_port)))
#     print('[*]已打开的端口：%s' % open_port)
#
# # ip='36.152.44.96'
# # number=6
# q=queue.Queue()
# for port in range(1,1000):
#     q.put(port)
# #port_run(ip,number)
# #portscan_start(ip=ip)
#


import threading
import socket
import queue
thread = []#线程列表
openNum = 0#处于开放状态的端口数，默认为0
A_port = []#主机存活的端口列表

def PortScaner(ip,port):
    global openNum
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
    s.settimeout(0.1)#设置socket连接超时，避免socket重复操作
    try:
        s.connect((ip,port))
        print('[+]端口%s是打开的' % (port))
        openNum += 1#如果socket连接成功，openNum加1
        A_port.append(port)#并把该端口号添加到主机存活的端口列表中
    except:
        pass   #如果连接失败，则pass
    s.close()


def PortScaner1(ip):
    for port in range(1, 65536):
        t = threading.Thread(target=PortScaner, args=(ip, port))  # 创建一个线程，target为线程需要执行的函数，args为函数的参数
        thread.append(t)  # 把线程保存到线程列表
    for t in range(len(thread)):  # 先获取thread线程列表的长度，遍历线程列表
        thread[t].start()  # 运行一个线程，即运行target指定的函数
    for t in range(len(thread)):
        thread[t].join()  # 表示当主进程中断时，所有的线程也会停止执行
    print('[*] 主机%s共打开了%s个端口'%(ip,openNum))
    print('[*]已打开的端口：%s'%A_port)