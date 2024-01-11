import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = "newsspider"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/news"]
    custom_settings={
            "FEEDS": {
                f"articles/bbc.json": {"format": "json"},
            },
        }

    def parse(self, response):
        urls = response.xpath("//*[contains(@data-entityid, 'container-top-stories#')]/div[2]/div/a/@href").getall()

        for url in urls:
            article_page = "https://www.bbc.com" + url
            yield response.follow(article_page, callback=self.parse_article)

    def parse_article(self, response):
        article_title = response.xpath("//h1/text()").getall()
        atricle_text = response.xpath('//article//div[@data-component="text-block"]/div/p/text()').getall()
        yield {
            'site': 'bbc',
            'url': response.url,
            'title': article_title,
            'text': atricle_text,
        }