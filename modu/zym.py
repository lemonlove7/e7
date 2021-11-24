import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
zym_b=[]
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
