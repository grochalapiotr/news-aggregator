import scrapy
import datetime
from ..utils.shortener import Shortener

class VoxspiderSpider(scrapy.Spider):
    name = "voxspider"
    allowed_domains = ["www.vox.com"]
    start_urls = ["https://www.vox.com/"]
    custom_settings={
            "FEEDS": {
                f"articles/vox-{datetime.datetime.now().date()}.json": {"format": "json", 'overwrite': True},
            },
        }

    def parse(self, response):
        urls = response.xpath("//div[@class='c-compact-river']/div/div/div/h2/a/@href").getall()

        for url in urls:
            yield response.follow(url, callback=self.parse_article)

    def parse_article(self, response):
        article_title = response.xpath("//h1/text()").getall()
        article_text = response.xpath("//div[@class='c-entry-content ']/h3/text() | //div[@class='c-entry-content ']/p/text()").getall()
        article_text = ' '.join(article_text).replace("  ", " ")
        if(article_text):
            yield {
                'site': 'vox',
                'url': response.url,
                'title': article_title[0],
                # 'text': atricle_text,
                'summary': Shortener().generate_summary(article_text),
            }
