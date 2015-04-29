import requests
import re
import threading
from BeautifulSoup import BeautifulSoup

lock = threading.Lock()


class Spider:
    """ spider for domain query. """

    def __init__(self):
        c = [chr(x) for x in range(ord('a'), ord('z')+1)]
        self.domains = ['oo'+d+x+'.com' for d in c for x in c]
        self.header = {
            'Host': 'pandavip.www.net.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:37.0) Gecko/20100101 Firefox/37.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            # 'Referer': 'http://www.net.cn/domain/searchresult/?keyword=www&suffix=.com',
            'Connection': 'keep-alive'
        }
        self.proxy = {'http': 'http://218.97.194.219'}
        self.url = 'http://pandavip.www.net.cn/check/check_ac1.cgi?domain='
        self.domain_count = len(self.domains)
        self.current = -1
        self.proxies = []

    def loop(self):
        while self.current < self.domain_count:
            domain = self.get_domain()
            print('{}'.format(threading.current_thread().name))
            try:
                self.query_domain(domain)
                print(domain)
            except requests.RequestException as e:
                eno = re.compile('\[\w+.\d+\]').search(str(e.message)).group(0)
                print('message:{}\nmore:{}'.format(e.message, str(eno)))
            finally:
                pass

    def run(self, count):
        for x in range(count):
            t = threading.Thread(target=self.loop(), name='thread'+chr(x))
            t.start()
            t.join()
            # print(x)
        pass

    def get_proxy(self):
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
            self.proxies.append(proxy)

    def query_domain(self, domain='google.com'):
        r = requests.get(self.url+domain, headers=self.header, proxies=self.proxy)
        if re.compile('available').search(r.text):
            print('available**************{}'.format(domain))
        else:
            print(r.text)

    def get_domain(self):
        lock.acquire()
        try:
            self.current += 1
            domain = self.domains[self.current]
        finally:
            lock.release()
        return domain

spider = Spider()
spider.run(5)

