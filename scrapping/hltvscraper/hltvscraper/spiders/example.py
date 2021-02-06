import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'hltv'
    def start_requests(self):
        urls = [
            'https://www.hltv.org/results',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
