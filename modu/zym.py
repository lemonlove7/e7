import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning  #消除警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # 消除警告

zym_b=[] #扫描出来的子域名
def zym_scan(do, apikey):
    # f=open(bc,'a+')
    # f.write('子域名扫描结果如下'+'\n')
    # f.close()
    if apikey=='':
        return False
    print('开始扫描%s存在的子域名'%do)
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey': apikey, 'domain': do}
    try:
        response = requests.get(url, params=params)
        j_data = response.json()
        domains = sorted(j_data['subdomains'])
        return domains
        #print(domains)
    except(KeyError):
        print("找不到子域： %s" % do)
        return
    except(requests.ConnectionError):
        print("无法连接到www.vitustotal.com", file=sys.stderr)
        return

    # print('[+] 共找到 %d 个域名' % len(domains))
    # i = 1
    # for domain in domains:
    #     print("[%d] %s" % (i, domain))
    #     i = i + 1
    #     f=open(bc,'a+')
    #     f.write(domain+'\n')
    #     f.close()


#do='baidu.com'
#apikey=input('请输入api:')
#apikey='b8850a5bbbba753effd1f5a8bc2dc98987a3b9d950b5fcded6071f28912470fa' #导入API' virustotal的API
#zym_scan(do, apikey)