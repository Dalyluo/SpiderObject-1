#ecoding=utf-8

# Create Time 2019-04
# Author： 罗武
import scrapy
from SpiderObject.items import XiaoHuarNewsItem, Article51CTOSpiderItem
from scrapy.loader import ItemLoader

class Article51CTOSpider(scrapy.Spider):
    name = 'article51ctoSpider'

    #设置初始请求，与start_urls属性设置有相同功效,该属性定义的URL列表将被顺序执行
    start_urls = [
        "https://blog.51cto.com/slaytanic",
        "https://blog.51cto.com/xjsunjie"
    ]

    def parse(self, response):
        # filename = 'xiaohuar_news.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        #xpath的写法：
        #1、//表示路径
        #2、ul[@class="artical-list"] 表示截取class属性值为"artical-list"的ul元素
        #3、text()表示获取上一个节点的文本内容
        #4、@href表示获取上一个"/"路径所表示元素的href属性值
        l = ItemLoader(item=Article51CTOSpiderItem(), response=response)
        l.add_xpath('title','//ul[@class="artical-list"]/li/a[@class="tit"]/text()')
        l.add_xpath('url','//ul[@class="artical-list"]/li/a[@class="tit"]/@href')
        l.add_xpath('summary','//ul[@class="artical-list"]/li/a[@class="con"]/text()')

        # Don't forget this codeline
        return l.load_item()


    def __init__(self, category=None, *args, **kwargs):
        super(Article51CTOSpider, self).__init__(*args, **kwargs)
        print "--init---"
