#ecoding=utf-8
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
    ]

    #当用户的请求没有指定回调时，这是Scrapy用来处理下载响应的默认回调。
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        # http://www.runoob.com/python/file-methods.html
        # open(filename, 'wb')  以二进制格式打开一个文件只用于写入。
        # 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，
        # 创建新文件。一般用于非文本文件如图片等。
        with open(filename, 'wb') as f:
            f.write(response.body)

