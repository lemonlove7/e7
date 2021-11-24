import sys
import re
import os
sys.dont_write_bytecode = True
print('[+]版本：v1.1')
import modu.cmsfi,modu.cdn,modu.ymip,modu.portscan,modu.zym,modu.clscan
url = input('[+]输入要进行信息收集的url：')
number=10  #多线程数量
print('------------------------------------------------------')

domain=url.replace('http://','')    #  检测ip使用
if 'https://' in url:
    domain=url.replace('https://', '')

res=re.findall( r'(.*?)\.',url)   #子域名扫描使用
one=(res[0])
do = url.replace(one+'.','')
#print(do)

#检测IP
ymip=modu.ymip.ym_ip(domain)  #IP
print(f'[+]IP:{ymip}')
#检测是否存在cdn
if modu.cdn.cdn_jc(domain) == True:
    print(f'[+]存在cdn：{domain}')
else:
    print(f'[+]不存在cdn：{domain}')

#cms指纹识别
cms = modu.cmsfi.whatweb(url)
print(f'[+]cms识别结果\n{cms.json()}')


#端口扫描
ip=ymip
modu.portscan.port_run(ip=ip,number=number)
#print(modu.portscan.open_port)


#子域名扫描
apikey='b8850a5bbbba753effd1f5a8bc2dc98987a3b9d950b5fcded6071f28912470fa'
zymscan=modu.zym.zym_scan(do, apikey)
if zymscan == False:
    print('没有输入apikey，扫描无法开始，跳过子域名扫描')

for zy in zymscan:
    print(f'[+]{zy}')
print(f'共发现{len(zymscan)}个子域名')


#目录扫描

modu.clscan.mu_scan(number=number,url=url)
