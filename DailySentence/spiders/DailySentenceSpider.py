# -*- coding: utf-8 -*-

import scrapy
from DailySentence.items import DailysentenceItem

class DailySentenceSpider(scrapy.Spider):
	name = 'dailysentence'
	allowed_domains = ["brainyquote.com"]
	start_urls = [
		"https://www.brainyquote.com/quotes_of_the_day.html"
	]

	def parse(self, response):
		item = DailysentenceItem()
		for info in response.xpath('//div[@class="m_panel"]'):
			item['quote'] = info.xpath('//a[@title="view quote"]/text()').extract_first()
			item['author'] = info.xpath('//a[@title="view author"]/text()').extract_first()
			yield item