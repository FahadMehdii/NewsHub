import scrapy

from fyp.models import Category, News


def parse_category(response, category_name):
    entries = response.xpath(
        '//div[contains(@class, "video-content") and contains(@class, "latest-page-new")]//div['
        'contains(@class, "singleBlock")]//li[contains(@class, "border-box")]'
    )

    news_items = []

    for entry in entries:
        content = entry.xpath('.//div[contains(@class, "entry-title")]//h2/text()').extract_first()
        url = entry.xpath('a/@href').extract_first()
        image_urls = entry.xpath('.//div[contains(@class, "pic")]//img/@src').extract_first()
        image_urls = image_urls.replace("s_", "")
        news_image = "https://i.pinimg.com/originals/ac/5f/a7/ac5fa7237dfa4f8c443949102754f90e.png"
        category, created = Category.objects.get_or_create(name=category_name)

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

    # Bulk create the news items for improved efficiency
    News.objects.bulk_create(news_items, ignore_conflicts=True)


class GeonewsSpider(scrapy.Spider):
    name = 'GeoNews'
    allowed_domains = ['geo.tv']
    start_urls = ['http://www.geo.tv/category/home', 'https://www.geo.tv/category/pakistan',
                  'https://www.geo.tv/category/sci-tech', 'https://www.geo.tv/category/business',
                  'https://www.geo.tv/category/entertainment', 'https://www.geo.tv/category/sports',
                  'https://www.geo.tv/category/world']

    def parse(self, response):
        if "pakistan" in response.url:
            yield from parse_category(response, "Geo Pakistan")
        elif "sci-tech" in response.url:
            yield from parse_category(response, "Geo Technology")
        elif "business" in response.url:
            yield from parse_category(response, "Geo Business")
        elif "entertainment" in response.url:
            yield from parse_category(response, "Geo Entertainment")
        elif "sports" in response.url:
            yield from parse_category(response, "Geo Sports")
        elif "world" in response.url:
            yield from parse_category(response, "Geo World")
