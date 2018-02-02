import scrapy
from python_test.items import *
class qiubaiSpider(scrapy.Spider):
	name = 'qiubai'
	allowed_domains = ["http://www.30s30.com/"]
	start_urls = [
		"http://www.30s30.com/"
	]
	custom_settings = {
		'ITEM_PIPELINES':{'python_test.pipelines.qiubai_pipelines':1}
	}
	def parse(self,response):
		model = qiubaiItem()
		for sel in response.xpath("/html/body/div[7]/div/ul"):
			#print sel.xpath("/div[1]/a/text()")
			t = sel.xpath("/li/a/h3/text()")
			print t
		#	print sel
