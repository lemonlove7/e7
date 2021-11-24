import os
def cdn_jc(domain):
    cdn =os.popen('nslookup %s' %domain).read()
    cdns = cdn.count('.')
    if cdns >10:
        return True
    else:
        return False
