# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# Typical uses of item pipelines are: 管道作用
#
# cleansing HTML data  清除Html数据
# validating scraped data (checking that the items contain certain fields) 验证抓取到的内容是否包含某些字段
# checking for duplicates (and dropping them) 检查重复数据并删除
# storing the scraped item in a database  持久化

import json
import codecs

class SpiderobjectPipeline(object):

    def open_spider(self,spider):
        self.file = codecs.open('items_3.json','w',encoding='utf-8')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        #中文编码处理
        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line.replace(' ','').replace("\n",""))
        return item
