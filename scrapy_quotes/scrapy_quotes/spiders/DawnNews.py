import scrapy
from fyp.models import Category, News


def parse_category(response, category_name):
    entries = response.xpath('//div[(@class="container")]//div[(@class="mb-4")]//article[('
                             '@data-layout="story")]')

    news_items = []

    for entry in entries:
        content = entry.xpath('.//h2/a/text()').extract_first()
        category, created = Category.objects.get_or_create(name=category_name)
        url = entry.xpath('.//h2/a/@href').extract_first()
        image_urls = entry.xpath('.//figure/div/a/picture/img/@src').extract_first()
        news_image = "https://www.dawn.com/_img/social-default.jpg"
        news_items.append(
            News(
                title=category_name,
                url=url,
                content=content,
                image_url=image_urls,
                news_image=news_image,
                category=category
            )
        )
    News.objects.bulk_create(news_items, ignore_conflicts=True)


def parse_tech_sports(response, category_name):
    entries = response.xpath('//div[(@class="container mx-auto px-2 sm:px-0")]//div[(@class="mb-4 border-b '
                             'border-gray-200")]//article[('
                             '@data-layout="story")]')

    news_items = []

    for entry in entries:
        content = entry.xpath('.//h2/a/text()').extract_first()
        category, created = Category.objects.get_or_create(name=category_name)
        url = entry.xpath('.//h2/a/@href').extract_first()
        image_urls = entry.xpath('.//figure/div/a/picture/img/@src').extract_first()
        news_image = "https://www.dawn.com/_img/social-default.jpg"
        news_items.append(
            News(
                title=category_name,
                url=url,
                content=content,
                image_url=image_urls,
                news_image=news_image,
                category=category
            )
        )
    News.objects.bulk_create(news_items, ignore_conflicts=True)


class DawnnewsSpider(scrapy.Spider):
    name = 'DawnNews'
    allowed_domains = ['dawn.com']
    start_urls = ['https://www.dawn.com/pakistan', 'https://www.dawn.com/business',
                  'https://www.dawn.com/world', 'https://www.dawn.com/sport', 'https://www.dawn.com/tech']

    def parse(self, response):
        if "pakistan" in response.url:
            yield from parse_category(response, "Dawn Pakistan")
        elif "business" in response.url:
            yield from parse_category(response, "Dawn Business")
        elif "world" in response.url:
            yield from parse_category(response, "Dawn World")
        elif "sport" in response.url:
            yield from parse_tech_sports(response, "Dawn Sports")
        elif "tech" in response.url:
            yield from parse_tech_sports(response, "Dawn Technology")
