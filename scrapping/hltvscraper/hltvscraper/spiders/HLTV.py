import scrapy


class HLTVSpider(scrapy.Spider):
    name = 'hltv'
    start_urls = [
        'https://www.hltv.org/results',
        'https://www.hltv.org/results?offset=100',
    ]
    def parse(self, response):
        yield {
            'teams': response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "line-align", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "team", " " ))]/text()').getall(),
            'score': response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "result-score", " " ))]//span/text()').getall(),
        }
#\35 602 > div > div > div:nth-child(1) > a > div
