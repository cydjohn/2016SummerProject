import scrapy

class QSBKSpider(scrapy.Spider):
        name = "dmoz"
        allowed_domains = ["dmoz.org"]
        start_urls = [
                                "http://www.qiushibaike.com/hot/page"
                                            ]
        def parse(self, response):
                    for sel in response.xpath('/article block untagged mb15'):
                        author = sel.xpath('author clearfix/text()').extract()
                        content = sel.xpath('content/text()').extract()
                        likes = sel.xpath('text()').extract()
                        print author, link, desc