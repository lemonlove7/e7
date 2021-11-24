import socket
def ym_ip(domain):
    ip = socket.gethostbyname(domain)
    return ip
