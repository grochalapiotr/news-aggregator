from scrapy.crawler import CrawlerProcess
from news_aggregator.utils.mail_handler import Mail_Handler
from news_aggregator.spiders.voxspider import VoxspiderSpider
from news_aggregator.spiders.newsspider import NewsspiderSpider
from news_aggregator.spiders.pcgamerspider import PcgamerspiderSpider


def main():
    mail = ''           #receiver mail
    # process = CrawlerProcess()
    # process.crawl(NewsspiderSpider)
    # process.crawl(VoxspiderSpider)
    # process.crawl(PcgamerspiderSpider)
    # process.start()

    Mail_Handler().send_email(mail)

    
if __name__ == '__main__':
    main()