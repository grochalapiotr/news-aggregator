import scrapy
import datetime
from ..utils.shortener import Shortener

class PcgamerspiderSpider(scrapy.Spider):
    name = "pcgamerspider"
    allowed_domains = ["www.pcgamer.com"]
    start_urls = ["https://www.pcgamer.com/news/"]
    custom_settings={
            "FEEDS": {
                f"articles/pcgamer-{datetime.datetime.now().date()}.json": {"format": "json", 'overwrite': True},
            },
        }

    def parse(self, response):
        urls = response.xpath("//div[contains(@class, 'listingResult small result')]/a/@href").getall()

        for url in urls:
            yield response.follow(url, callback=self.parse_article)

    def parse_article(self, response):
        article_title = response.xpath("//h1/text()").getall()
        article_text = ' '.join(response.xpath('//div[@id="article-body"]/p/text()').getall()).replace("  ", " ")
        if(article_text):
            yield {
                'site': 'pcgamer',
                'url': response.url,
                'title': article_title[0],
                # 'text': atricle_text,
                'summary': Shortener().generate_summary(article_text),
            }
