import scrapy
from python_test.items import DmozItem
class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://dmoztools.net/Computers/Programming/Languages/Python/Books/"
	]
	custom_settings = {
		'ITEM_PIPELINES': {'python_test.pipelines.Dmoz_pipelines':1}
	#	'MYSQL_HOST': "127.0.0.1",
	#	'MYSQL_DBNAME': 'test',
	#	'MYSQL_USER': 'root',
	#	'MYSQL_PASSWD': "yuan0202",
	}
	
	#ITEM_PIPELINES = {'python_test.piplines.DmozPipeline':1}
	print "2222"
	def parse(self,response):
		#items = []
		for sel in response.xpath("//*[@id='site-list-content']/div"):
			item = DmozItem()
			t = sel.xpath('div[3]/a/div[1]/text()').extract()
			item['title'] = t
			#print item
			#items.append(item)
			print '@@@@@@@@@@@@@@@@@@@@@@@'
			yield item
