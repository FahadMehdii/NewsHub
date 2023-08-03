from scrapy import Spider
from scrapy_quotes.items import ScrapyQuotesItem
from fyp.models import MyModel

class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@itemprop="text"]/text()').extract()
        data = MyModel()
        data.field1 = quotes
        data.save()
