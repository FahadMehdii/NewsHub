from news_hub.fyp import models
from scrapy.exceptions import DropItem


class MyappPipeline(object):
    def process_item(self, item, spider):
        scraped_data = models.MyModel()
        scraped_data.save()
        return item
