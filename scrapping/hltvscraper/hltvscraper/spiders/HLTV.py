import scrapy


class HLTVSpider(scrapy.Spider):
    name = 'hltv'
    start_urls = [
        'https://www.hltv.org/results',
        'https://www.hltv.org/results?offset=100',
    ]
    def parse(self, response):
        yield {
            'match': response.css('a.a-reset::attr(href)').re(r'/matches.*'),
        }
