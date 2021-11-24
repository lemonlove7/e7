import requests
import zlib
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning  #消除警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # 消除警告

def whatweb(url):
    response = requests.get(url,verify=False)
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go",files=data)

# if __name__ == '__main__':
#     url=input('请输入要检查的url：')
#     request = whatweb(url=url)
#     print(u"今日识别剩余次数")
#     print(request.headers["X-RateLimit-Remaining"])
#     print(f'cms识别结果：{request.json()}')