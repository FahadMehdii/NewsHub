import scrapy

from fyp.models import News, Category


def parse_sci_tec(response, category_name):
    top_top = response.xpath('//div[@class="sport-section1"]')
    top = response.xpath('//div[@class="technology-featured-section tech-featured"]')
    games_top = response.xpath('//div[@class="sports-features-wrapper tech-game"]//div[@class="row"]')
    review_gadgets_top = response.xpath('//div[@class="sports-features-wrapper"]//div[@class="row"]')
    reviews_gadgets_featured_games = response.xpath('//div[@class="technology-featured-section technology-featured-section2"]')
    more_news = response.xpath('//div[@class="col-md-6 sportcustomsecton2"]')
    more_news_2 = response.xpath('//div[@class="row moresectionrow mob-ro-content"]')

    entries = top_top + top + games_top + review_gadgets_top + reviews_gadgets_featured_games + more_news + more_news_2
    news_items = []

    for entry in entries:
        content_elements = entry.xpath('.//div/a/*[self::h3 or self::h2]')
        urls = entry.xpath('.//div/a/@href').extract()
        image_urls = entry.xpath('.//div/a/div/img/@data-src').extract()

        for i, content_element in enumerate(content_elements):
            content = content_element.xpath('text()').get()
            img = image_urls[i] if i < len(image_urls) else None

            for url in urls:
                if url and content:
                    category, created = Category.objects.get_or_create(name=category_name)
                    news_item = News(
                        title=content,  # Using content as the title of the news item
                        content=content,
                        url=url,
                        image_url=img,
                        news_image="https://th.bing.com/th/id/R.016d2930c1bb05504385260ff6a6a9bf?rik=IdtbqSCn%2fvmH0g&pid=ImgRaw&r=0",
                        category=category
                    )
                    news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)


def parse_pakistan(response, category_name):
    top_top = response.xpath('//div[@class="sport-section1"]')
    top = response.xpath('//div[@class="horizontal-news1 sportsecton2"]')
    gb_ajk_kp_bs_p_i = response.xpath('//div[@class="col-md-12"]')
    more_news = response.xpath('//div[@class="sports-demo"]')

    entries = top_top + top + gb_ajk_kp_bs_p_i + more_news
    news_items = []

    for entry in entries:
        content_elements = entry.xpath('.//div/a/*[self::h3 or self::h2]')
        urls = entry.xpath('.//div/a/@href').extract()
        image_urls = entry.xpath('.//div/a/div/img/@data-src').extract()

        for i, content_element in enumerate(content_elements):
            content = content_element.xpath('text()').get()
            img = image_urls[i] if i < len(image_urls) else None

            for url in urls:
                if url and content:
                    category, created = Category.objects.get_or_create(name=category_name)
                    news_item = News(
                        title=content,  # Using content as the title of the news item
                        content=content,
                        url=url,
                        image_url=img,
                        news_image="https://th.bing.com/th/id/R.016d2930c1bb05504385260ff6a6a9bf?rik=IdtbqSCn%2fvmH0g&pid=ImgRaw&r=0",
                        category=category
                    )
                    news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)


def parse_Business(response, category_name):
    top = response.xpath('//div[@class="business-featured-big-thumbnails"]')
    latest_market_news = response.xpath('//div[@class="latest-market-news"]')
    latest_market_news2 = response.xpath('//div[@class="latest-market-news-small-thumbs"]')
    featured = response.xpath('//div[@class="featured-big-thumbnails busines-featured"]')
    more_news = response.xpath('//div[@class="col-md-6 sportcustomsecton2"]')
    more_news2 = response.xpath('//div[@class="row moresectionrow mob-ro-content"]')

    entries = top + latest_market_news + latest_market_news2 + featured + more_news + more_news2
    news_items = []

    for entry in entries:
        content_elements = entry.xpath('.//div/a/*[self::h3 or self::h2 or self::h4]')
        urls = entry.xpath('.//div/a/@href').extract()
        image_urls = entry.xpath('.//div/a/div/img/@data-src').extract()

        for i, content_element in enumerate(content_elements):
            content = content_element.xpath('text()').get()
            img = image_urls[i] if i < len(image_urls) else None

            for url in urls:
                if url and content:
                    category, created = Category.objects.get_or_create(name=category_name)
                    news_item = News(
                        title=content,  # Using content as the title of the news item
                        content=content,
                        url=url,
                        image_url=img,
                        news_image="https://th.bing.com/th/id/R.016d2930c1bb05504385260ff6a6a9bf?rik=IdtbqSCn%2fvmH0g&pid=ImgRaw&r=0",
                        category=category
                    )
                    news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)


def parse_world(response, category_name):
    top_top = response.xpath('//div[@class="sport-section1"]')
    top = response.xpath('//div[@class="horizontal-news1 sportsecton2"]')
    featured_feature_top = response.xpath('//div[@class="col-md-6 sportcustomsection transition metal "]')
    featured_M_N = response.xpath('//div[@class="col-md-6 sportcustomsecton2"]')
    more_news2 = response.xpath('//div[@class="row moresectionrow mob-ro-content"]')

    entries = top_top + top + featured_feature_top + featured_M_N + more_news2
    news_items = []

    for entry in entries:
        content_elements = entry.xpath('.//div/a/*[self::h3 or self::h2]')
        urls = entry.xpath('.//div/a/@href').extract()
        image_urls = entry.xpath('.//div/a/div/img/@data-src').extract()

        for i, content_element in enumerate(content_elements):
            content = content_element.xpath('text()').get()
            img = image_urls[i] if i < len(image_urls) else None

            for url in urls:
                if url and content:
                    category, created = Category.objects.get_or_create(name=category_name)
                    news_item = News(
                        title=content,  # Using content as the title of the news item
                        content=content,
                        url=url,
                        image_url=img,
                        news_image="https://th.bing.com/th/id/R.016d2930c1bb05504385260ff6a6a9bf?rik=IdtbqSCn%2fvmH0g&pid=ImgRaw&r=0",
                        category=category
                    )
                    news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)


def parse_entertainment(response, category_name):
    top_top = response.xpath('//div[@class="sport-section1"]')
    top = response.xpath('//div[@class="horizontal-news1 sportsecton2"]')
    spotlight_music_fashion_film_tv_gossip = response.xpath('//div[@class="sport-morenewsection-inner"]')
    more_news = response.xpath('//div[@class="sports-demo"]')

    entries = top_top + top + spotlight_music_fashion_film_tv_gossip + more_news
    news_items = []

    for entry in entries:
        content_elements = entry.xpath('.//div/a/*[self::h3 or self::h2]')
        urls = entry.xpath('.//div/a/@href').extract()
        image_urls = entry.xpath('.//div/a/div/img/@data-src').extract()

        for i, content_element in enumerate(content_elements):
            content = content_element.xpath('text()').get()
            img = image_urls[i] if i < len(image_urls) else None

            for url in urls:
                if url and content:
                    category, created = Category.objects.get_or_create(name=category_name)
                    news_item = News(
                        title=content,  # Using content as the title of the news item
                        content=content,
                        url=url,
                        image_url=img,
                        news_image="https://th.bing.com/th/id/R.016d2930c1bb05504385260ff6a6a9bf?rik=IdtbqSCn%2fvmH0g&pid=ImgRaw&r=0",
                        category=category
                    )
                    news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)


def parse_sports(response, category_name):
    entries = (
        response.xpath('//div[@class="sport-section1"]') +
        response.xpath('//div[@class="horizontal-news1 sportsecton2"]') +
        response.xpath('//div[@class="sports-features-wrapper"]') +
        response.xpath('//div[@class="sport-morestores-inner"]') +
        response.xpath('//div[@class="sports-demo"]')
    )
    news_items = []

    for entry in entries:
        content_elements = entry.xpath('.//div/a/*[self::h3 or self::h2]')
        urls = entry.xpath('.//div/a/@href').extract()
        image_urls = entry.xpath('.//div/a/div/img/@data-src').extract()

        for i, content_element in enumerate(content_elements):
            content = content_element.xpath('text()').get()
            img = image_urls[i] if i < len(image_urls) else None

            for url in urls:
                if url and content:
                    category, created = Category.objects.get_or_create(name=category_name)
                    news_item = News(
                        title=content,  # Using content as the title of the news item
                        content=content,
                        url=url,
                        image_url=img,
                        news_image="https://th.bing.com/th/id/R.016d2930c1bb05504385260ff6a6a9bf?rik=IdtbqSCn%2fvmH0g&pid=ImgRaw&r=0",
                        category=category
                    )
                    news_items.append(news_item)

    News.objects.bulk_create(news_items, ignore_conflicts=True)


class TribuneSpider(scrapy.Spider):
    name = 'tribune'
    allowed_domains = ['tribune.com.pk']
    start_urls = ['http://tribune.com.pk/', 'https://tribune.com.pk/pakistan', 'https://tribune.com.pk/business',
                  'https://tribune.com.pk/world', 'https://tribune.com.pk/technology',
                  'https://tribune.com.pk/life-style', 'https://tribune.com.pk/sports']

    def parse(self, response):
        if "pakistan" in response.url:
            yield from parse_pakistan(response, "Express Pakistan")
        elif "business" in response.url:
            yield from parse_Business(response, "Express Business")
        elif "technology" in response.url:
            yield from parse_sci_tec(response, "Express Technology")
        elif "world" in response.url:
            yield from parse_world(response, "Express World")
        elif "life-style" in response.url:
            yield from parse_entertainment(response, "Express Entertainment")
        elif "sports" in response.url:
            yield from parse_sports(response, "Express Sports")
