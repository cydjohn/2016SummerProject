# -*- coding:utf-8 -*-

#没有使用框架，通过python自带的urllib库以及正则表达式抓取糗事百科的段子
# 参考网址：http://cuiqingcai.com/990.html

import urllib
import urllib2
import re


url = 'http://www.qiushibaike.com/hot/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
    # pattern = re.compile('<div class="content".*?</div>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        # if len(item) > 4:
        #     print len(item)
        #     haveImg = re.search("img",item[3])
        #     if not haveImg:
        #         print item[0],item[1],item[2],item[4]
        print item[0],item[1],item[2]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason