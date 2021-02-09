import scrapy


class MatchDetailSpider(scrapy.Spider):
    name = 'hltv_match_detail'
    start_urls = ['https://www.hltv.org/results']

    def parse(self, response):
        match_links = response.css('div.results-all div.result-con > a.a-reset')
        yield from response.follow_all(match_links, self.parse_author)

        pagination_links = response.css('a.pagination-next')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        
        yield {
            'team1': extract_with_css('div.team1-gradient div.teamName::text'),
            'team2': extract_with_css('div.team2-gradient div.teamName::text'),
            'scores': response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "team", " " ))]//a+//div/text()').getall(),
            'date': extract_with_css('.timeAndEvent .date::text'),
        }
