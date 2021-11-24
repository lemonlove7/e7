import socket
#域名反查IP
def ym_ip(domain):
    ip = socket.gethostbyname(domain)
    #print('IP为：',ip)
    return ip
