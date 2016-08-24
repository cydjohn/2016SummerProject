# -*- coding: utf-8 -*-

# 用不成……

import scrapy

class QSBKSpider(scrapy.Spider):
    name = "QSBK"
    start_urls = ["http://www.qiushibaike.com/hot/"]
    def parse(self, response):
        print "hehehheheheh"
        print response.body
        for sel in response.xpath('/article block untagged mb15'):
            author = sel.xpath('author clearfix/text()').extract()
            content = sel.xpath('content/text()').extract()
            likes = sel.xpath('text()').extract()
            print author, link, desc 
