import requests
import re
from BeautifulSoup import BeautifulSoup


def get_proxy():
    proxies = []
    url = 'http://www.xici.net.co/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    trs = soup.findAll(attrs={'class': ''})
    for tr in trs:
        tds = tr.findAll('td')
        ip = tds[1].text
        port = tds[2].text
        typ = tds[5].text
        proxy = {'ip': ip, 'port': port, 'type': typ}
        proxies.append(proxy)

    return proxies


def query_domain(proxies):
    url = 'http://pandavip.www.net.cn/check/check_ac1.cgi?domain='
    proxies = {'http': 'http://218.97.194.201',
               'http': 'http://218.97.194.202',
               'http': 'http://218.97.194.219'}
    header = {
        'Host': 'pandavip.www.net.cn',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        # 'Referer': 'http://www.net.cn/domain/searchresult/?keyword=wwwww&suffix=.com',
        'Connection': 'keep-alive'
    }
    c = [chr(x) for x in range(ord('a'), ord('z')+1)]
    domain = ['xi'+d+x+'.com' for d in c for x in c]
    for x in domain:
        rules = re.compile('available')
        r = requests.get(url+x, headers=header, proxies=proxies)
        result = rules.search(r.text)
        if result:
            print('**************{}'.format(x))
        else:
            print(r.text)


get_proxy()
# query_domain()