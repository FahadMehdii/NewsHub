import scrapy

from fyp.models import News, Category


def parse_category(response, category_name):
    Highlights = response.xpath('//div[(@class="    mt-2  slideshow--list  ")]//article[(@class="story relative overflow-hidden  box    mb-2  pb-2")]')
    news_items = []

    for entry in Highlights:
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

class DawnhighlightsSpider(scrapy.Spider):
    name = 'DawnHighlights'
    allowed_domains = ['dawn.com']
    start_urls = ['http://www.dawn.com/', 'https://www.dawn.com/pakistan', 'https://www.dawn.com/business',
                  'https://www.dawn.com/world']

    def parse(self, response):
        if "pakistan" in response.url:
            yield from parse_category(response, "Dawn Pakistan Entertainment")
        elif "business" in response.url:
            yield from parse_category(response, "Dawn Business Entertainment")
        elif "world" in response.url:
            yield from parse_category(response, "Dawn World Entertainment")
