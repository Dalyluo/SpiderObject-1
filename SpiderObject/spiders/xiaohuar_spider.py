#ecoding=utf-8

import scrapy,os
from SpiderObject.items import XiaoHuarNewsItem
from scrapy.loader import ItemLoader

class XiaoHuarSpider(scrapy.Spider):
    name = 'xiaohuarSpider'

    #设置初始请求，与start_urls属性设置有相同功效
    def start_requests(self):
        yield scrapy.FormRequest('http://www.xiaohuar.com/news/')

    def parse(self, response):
        filename = 'xiaohuar_news.html'
        with open(filename, 'wb') as f:
            f.write(response.body)


        #打印所有的新闻列表
        # list = response.xpath("/html/body/div[2]/div[1]/div[1]/div[4]/ul").getall()
        # for item in list:
        #     print item


        # l = ItemLoader(item=XiaoHuarNewsItem(), response=response)
        # l.add_xpath('title','a[@class="title"]')
        # l.add_xpath('url','a[@class="href"]')
        # l.add_xpath('publishDate','/html/body/div[2]/div[1]/div[1]/div[4]/ul/li[1]/span')
        #
        # print "Spider,Helloworld! "
        # print l['title']

    def __init__(self, category=None, *args, **kwargs):
        super(XiaoHuarSpider, self).__init__(*args, **kwargs)
        print "--init---"
