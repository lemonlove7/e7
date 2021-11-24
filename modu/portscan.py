import threading
import socket
import queue
thread = []
openNum = 0
A_port = []
def PortScaner(ip,port):
    global openNum
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        s.connect((ip,port))
        print('[+]端口%s是打开的' % (port))
        openNum += 1
        A_port.append(port)
    except:
        pass
    s.close()
def PortScaner1(ip):
    for port in range(1, 65536):
        t = threading.Thread(target=PortScaner, args=(ip, port))
        thread.append(t)
    for t in range(len(thread)):
        thread[t].start()
    for t in range(len(thread)):
        thread[t].join()
    print('[*] 主机%s共打开了%s个端口'%(ip,openNum))
    print('[*]已打开的端口：%s'%A_port)
