import scrapy

from fyp.models import News, Category


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

        width = 490  # Replace with the desired width value
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
    news_items = []

    for entry in top:
        content_elements = entry.xpath('.//ul/li/a/div/*[self::h1 or self::h2]')
        urls = entry.xpath('.//ul/li/a/@href').extract()
        image_urls = entry.xpath('.//ul/li/a/div/img/@data-src').extract()
        for i, content_element in enumerate(content_elements):
            content = content_element.xpath('text()').get()
            img = image_urls[i] if i < len(image_urls) else None

            for url in urls:
                if url and content:
                    category_name = category_name  # Provide the desired category name here
                    category, created = Category.objects.get_or_create(name=category_name)
                    news_item = News(
                        title=category_name,
                        content=content,
                        url=url,
                        image_url=img,
                        news_image="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,"
                                   "f_auto,q_auto:eco,dpr_1/v1457504255/kkxl6abuoi6ev4ua593f.png",
                        category=category
                    )
                    news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)


from urllib.parse import urljoin

def parse_DunyaNews(response, category_name):
    top = response.xpath('//div[@class="sectionBody"]//div[@class="row"]//div[@class="col-12 col-md-4 col-lg-4"]')
    news_items = []

    for entry in top:
        text_values = entry.xpath('.//div/h3/a')
        content = text_values.xpath('normalize-space(.)').extract_first()
        relative_url = entry.xpath('.//div/a//@href').extract_first()
        url = urljoin('https://www.dunyanews.tv', relative_url) if relative_url else ''
        image_urls = entry.xpath('.//div[@class="media__image"]//img/@src').extract_first()
        category_name = category_name  # Provide the desired category name here
        category, created = Category.objects.get_or_create(name=category_name)
        news_item = News(
            title=category_name,
            content=content,
            url=url,
            image_url=image_urls,
            news_image="https://www.bizasialive.com/wp-content/uploads/2017/04/dunyanews001.jpg",
            category=category
            )
        news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)



class TopSpider(scrapy.Spider):
    name = 'TOP'
    allowed_domains = ['www.bbc.com', 'www.thenews.com.pk', 'dunyanews.tv/en/home']
    start_urls = ['http://www.bbc.com/', 'http://www.bbc.com/news', 'https://www.thenews.com.pk/',
                  'https://dunyanews.tv/en/home']

    def parse(self, response):
        if "www.bbc.com/news" in response.url:
            yield from parse_BBC(response, "BBC Top")
        elif "www.thenews.com.pk" in response.url:
            yield from parse_TheNews(response, "TheNews Top")
        elif "dunyanews.tv/en/home" in response.url:
            yield from parse_DunyaNews(response, "Dunya Top")
