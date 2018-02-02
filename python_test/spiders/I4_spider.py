import scrapy
from python_test.items import *
from scrapy.http import Request

class I4Spider(scrapy.Spider):
	name = "qyI4"
	print "yhb"
	allowed_domains = ["www.i4.cn"]
	start_urls = [
		"http://www.i4.cn/news_1_0_0_2.html"
	]
	custom_settings = {
		'ITEM_PIPELINES': {
			'python_test.pipelines.I4_pipelines':1,
			'python_test.pipelines.I4_detail_pipelines':3
		},
		'DOWNLOAD_TIMEOUT': 10,
        'RETRY_TIMES': 3,
	}
	
	print "2222"
	#def start_requests(self):
	#	url="http://www.i4.cn/news_1_0_0_2.html"
	#	yield Request(url=url)
	def parse(self,response):
		print "33333"
		#items = []
		#yhb = response.xpath("//*[@id='news']/div/div[1]/div[1]/a[1]")
		#print yhb
		for sel in response.xpath("//*[@id='news']/div/div[1]//div[@class='news_list']"):
			print sel	
			item = I4Item()
			link = sel.xpath("./a[@class='img']/@href").extract()[0]
			print link
			pre = 'http://www.i4.cn/'
			item['link'] = pre + link
			title = sel.xpath("./a[@class='title']/text()").extract()[0]
			item['title'] = title
			item['content'] = sel.xpath("./a[@class='describe']/text()").extract()[0]			
			#items.append(item)
			print '@@@@@@@@@@@@@@@@@@@@@@@'
			yield item
			#print link+"@@@@@@@@@@"
			yield scrapy.Request(pre+link,callback=self.detail)
		#nextpage = response.xpath("//*[@id='news']/div/div[2]/a[10]/@href").extract()[0]
		#next_url = response.urljoin(pre+nextpage)
		#yield scrapy.Request(next_url,callback=self.parse)

	def detail(self,response):
		item = I4_detailItem()
		print "yyyy"
		item['title'] = response.xpath("//*[@id='news_detail']/div/div/div[1]/h1/text()").extract()[0]
		print item['title']
		item['report_date'] = response.xpath("//*[@id='news_detail']/div/div/div[1]/div[1]/div[1]/text()").extract()[0]
		print item['report_date']
		item['read_num'] = response.xpath("//*[@id='news_detail']/div/div/div[1]/div[1]/div[2]/text()").extract()[0]
		item['source'] = response.xpath("//*[@id='news_detail']/div/div/div[1]/div[1]/div[3]/text()").extract()[0]
		yield item	
