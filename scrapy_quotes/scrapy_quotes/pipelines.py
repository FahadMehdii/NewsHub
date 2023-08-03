# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class ScrapyQuotesPipeline:
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):

    def item_completed(self, results, item, info):
        if not results:
            raise DropItem("Item contains no images")
        item['images'] = [image for ok, image in results if ok]
        return item
