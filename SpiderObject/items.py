# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderobjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiaoHuarNewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    publishDate = scrapy.Field()
    pass

#定义文章Model
class Article51CTOSpiderItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    pass
