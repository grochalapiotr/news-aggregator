import json
from news_aggregator.spiders.newsspider import NewsspiderSpider
from news_aggregator.spiders.voxspider import VoxspiderSpider
from scrapy.crawler import CrawlerProcess


def main():
    process = CrawlerProcess()
    process.crawl(NewsspiderSpider)
    process.crawl(VoxspiderSpider)
    process.start()
    

# f = open('bbc_articles.json')

# data = json.load(f)

# merged_text = ''.join(data[0]['text'])

# # print(data[0]['url'])
# # print(data[0]['title'])
# # print(data[0]['text'])
# print(merged_text)

if __name__ == '__main__':
    main()