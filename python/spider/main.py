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
		'Cookie': 'UOR=imcn.me,widget.weibo.com,roclinux.cn; SINAGLOBAL=5321411160343.511.1426472087009; ULV=1427268903882:7:7:2:5893705920086.48.1427268903874:1427100913766; SUB=_2AkMiTuoTf8NhqwJRmPoVzW3qa4l-zwrEiebDAHzsJxJjHkE37FYys8vCQlbMOLsePO6XHQyYCg3e; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5H.oOAfR5Lv1HCWosCJGTv; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; _s_tentry=passport.weibo.com; Apache=5893705920086.48.1427268903874; YF-Page-G0=fc0a6021b784ae1aaff2d0aa4c9d1f17; YF-V5-G0=447063a9cae10ef9825e823f864999b0; WBtopGlobal_register_version=56b492c83030fda6',
		'Connection': 'keep-alive'
	}

resrfile = open('./resrfile.txt','w')

print('file opened')

rules = re.compile(r"<!--feed内容-->[\s\S]*<!--翻页-->")
r = requests.get(url,headers = headers)
content = rules.match(r.text)

print('data got,writing...')

# resrfile.write(str(content))
for line in r.text:
	resrfile.write(line)

print('data writing finished')

resrfile.close()