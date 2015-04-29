# -*- coding: utf-8 -*-
import requests
import json
import re

url = 'http://weibo.com/u/3426531624'
headers = {
    'Host': 'weibo.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

resrfile = open('./resrfile.txt', 'w')

print('file opened')

rules = re.compile(r"<!--feed内容-->[\s\S]*<!--翻页-->")
r = requests.get(url, headers=headers)
content = rules.match(r.text)

print('data got,writing...')

# resrfile.write(str(content))
for line in r.text:
    resrfile.write(line)

print('data writing finished')

resrfile.close()