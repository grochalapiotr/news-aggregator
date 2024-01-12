import scrapy
import datetime
from ..utils.shortener import Shortener
from ..utils.sentiment_analyzer import SentimentAnalyzer

class NewsspiderSpider(scrapy.Spider):
    name = "newsspider"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/news"]
    custom_settings={
            "FEEDS": {
                f"articles/bbc-{datetime.datetime.now().date()}.json": {"format": "json", 'overwrite': True},
            },
        }

    def parse(self, response):
        urls = response.xpath("//*[contains(@data-entityid, 'container-top-stories#')]/div[2]/div/a/@href").getall()

        for url in urls:
            article_page = "https://www.bbc.com" + url
            yield response.follow(article_page, callback=self.parse_article)

    def parse_article(self, response):
        article_title = response.xpath("//h1/text()").getall()
        article_text = ' '.join(response.xpath('//article//div[@data-component="text-block"]/div/p/text()').getall()).replace("  ", " ")
        if(article_text):
            yield {
                'site': 'bbc',
                'url': response.url,
                'sentiment': SentimentAnalyzer().analyze_sentiment(article_text),
                'title': article_title[0],
                # 'text': article_text,
                'summary': Shortener().generate_summary(article_text),
            }