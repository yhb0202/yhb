# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    # define the fields for your item here like:
	#print '11'
    title = scrapy.Field()

class I4Item(scrapy.Item):
	
    link = scrapy.Field() # 链接
    title = scrapy.Field() # 标题
    #time = scrapy.Field()  #发布时间
    content = scrapy.Field()  #内容
    pass

class I4_detailItem(scrapy.Item):
    title = scrapy.Field()
    report_date = scrapy.Field()
    source = scrapy.Field()
    read_num = scrapy.Field()
    pass	
