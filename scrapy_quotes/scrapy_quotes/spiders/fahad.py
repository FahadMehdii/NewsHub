import scrapy

from fyp.models import Category, News


def parse_BBC(response, category_name):
    top = response.xpath('//div[@class="nw-p-oat"]//div[@class="gel-wrap"]')
    top_top = response.xpath('//div[@class="nw-c-top-stories-primary__story gel-layout gs-u-pb gs-u-pb0@m"]')

    entries = top + top_top
    news_items = []

    for entry in entries:
        content = entry.xpath('.//div/a/*[self::h3]/text()').extract_first()
        relative_url = entry.xpath('.//div/a/@href').extract_first()
        url = 'https://www.bbc.com' + relative_url if relative_url else ''
        image_url = entry.xpath('.//img/@data-src').extract_first()

        if not image_url:
            image_url = entry.xpath('.//img/@src').extract_first()

        width = 800  # Replace with the desired width value
        formatted_url = image_url.format(width=width)

        category_name = category_name  # Provide the desired category name here
        category, created = Category.objects.get_or_create(name=category_name)
        news_items.append(
            News(
                title=category_name,
                url=url,
                content=content,
                image_url=formatted_url,
                news_image='https://encrypted-tbn0.gstatic.com/images?q=tbn'
                           ':ANd9GcS28VrPAYkX2yJ3cU5CBiFd5bZV9hWkrha16Gsq4G1HsfCpzv0xQr6HmPKaEmStJ3MODTU&usqp=CAU',
                category=category
            )
        )

        # Bulk create the news items for improved efficiency
        News.objects.bulk_create(news_items, ignore_conflicts=True)


def parse_TheNews(response, category_name):
    top = response.xpath('//div[@class="main_story_left"]')
    entries = top
    news_items = []

    for entry in entries:
        content = entry.xpath('.//ul/li/a/div/*[self::h1 or self::h2]/text()').extract_first()
        url = entry.xpath('.//ul/li/a/@href').extract_first()
        image_url = entry.xpath('.//ul/li/a/div/img/@data-src').extract_first()
        category_name = category_name  # Provide the desired category name here
        category, created = Category.objects.get_or_create(name=category_name)
        news_items.append(
            News(
                title=category_name,
                url=url,
                content=content,
                image_url=image_url,
                news_image='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYEAAACDCAMAAABcOFepAAAAilBMVEX///8AAAD'
                           '+/v4BAQH7+/ve3t7j4+N0dHS2trYSEhLr6+uVlZUFBQX29vYwMDBxcXGCgoLn5'
                           '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',
                category=category
            )
        )

        # Bulk create the news items for improved efficiency
        News.objects.bulk_create(news_items, ignore_conflicts=True)


class FahadSpider(scrapy.Spider):
    name = 'fahad'
    allowed_domains = ['www.bbc.com', 'www.thenews.com.pk']
    start_urls = ['http://www.bbc.com/', 'http://www.bbc.com/news', 'https://www.thenews.com.pk/']

    def parse(self, response):
        if "news" in response.url:
            yield from parse_BBC(response, "BBC Top")
        if "www.thenews.com.pk" in response.url:
            yield from parse_TheNews(response, "TheNews Top")
