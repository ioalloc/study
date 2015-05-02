import requests
import re
import threading
from BeautifulSoup import BeautifulSoup
import time

lock = threading.Lock()


class Spider:
    """ spider for domain query. """

    def __init__(self):
        self.domains = [chr(x) + chr(y) + chr(z) + '.me' for x in range(ord('a'), ord('z') + 1)
                        for y in range(ord('a'), ord('z') + 1)
                        for z in range(ord('a'), ord('z') + 1)]
        self.header = {
            'Host': 'pandavip.www.net.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:37.0) Gecko/20100101 Firefox/37.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            # 'Referer': 'http://www.net.cn/domain/searchresult/?keyword=www&suffix=.com',
            'Connection': 'keep-alive'
        }
        self.proxies = []
        self.url = 'http://pandavip.www.net.cn/check/check_ac1.cgi?domain='
        self.init_proxy()
        self.domain_count = len(self.domains)
        self.proxy_count = len(self.proxies)
        self.current_domain = -1
        self.proxy = self.proxies.pop()
        self.current_proxy = -1

    def __del__(self):
        pass

    def loop(self):
        while len(self.domains) > 0:
            domain = self.get_domain()
            print('{}'.format(threading.current_thread().name))
            try:
                self.query_domain(domain)
            except:
                lock.acquire()
                self.proxies.append(self.proxy)
                lock.release()
                self.proxy = self.get_proxy()
                lock.acquire()
                self.domains.append(domain)
                lock.release()
            finally:
                time.sleep(0.2)
                pass

    def run(self):
        t1 = threading.Thread(target=self.loop, name='thread1')
        t2 = threading.Thread(target=self.loop, name='thread2')
        t3 = threading.Thread(target=self.loop, name='thread3')
        t4 = threading.Thread(target=self.loop, name='thread4')

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

    def init_proxy(self):
        url = 'http://www.xici.net.co/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        trs = soup.findAll(attrs={'class': ''})
        for tr in trs:
            tds = tr.findAll('td')
            ip = tds[1].text
            port = tds[2].text
            typ = tds[5].text
            proxy = {typ: 'http://{}:{}'.format(ip,port)}

            self.proxies.append(proxy)

    def query_domain(self, domain='google.com'):
        r = requests.get(self.url + domain, headers=self.header, proxies=self.proxy)
        if re.compile('available').search(r.text):
            print('available**************{}'.format(domain))
        elif re.compile('frequency').search(r.text):
            self.proxy = self.get_proxy()
            self.domains.append(domain)
        else:
            print(r.text)
            pass

    def get_domain(self):
        lock.acquire()
        try:
            self.current_domain += 1
            domain = self.domains.pop()
        finally:
            lock.release()
        return domain

    def get_proxy(self):
        lock.acquire()
        try:
            proxy = self.proxies.pop()
            print('change proxy:{}'.format(proxy))
        finally:
            lock.release()
        return proxy


if __name__ == '__main__':
    spider = Spider()
    spider.run()

