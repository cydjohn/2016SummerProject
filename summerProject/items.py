# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class SummerprojectItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class QSBKItem(scrapy.Item):
        author = scrapy.Field()
        content = scrapy.Field()
        likes = scrapy.Field()