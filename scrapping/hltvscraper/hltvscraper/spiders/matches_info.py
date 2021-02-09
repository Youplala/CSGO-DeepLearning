import scrapy


class MatchDetailSpider(scrapy.Spider):
    name = 'hltv_match_detail'
    start_urls = ['https://www.hltv.org/results']

    def parse(self, response):
        match_links = response.css('div.results-all div.result-con > a.a-reset')
        yield from response.follow_all(match_links, self.parse_match)

    def parse_match(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def get_maps():
            maps = response.css('div.mapholder > div.played div.mapname::text').getall()
            map_json = []
            i=1
            for map in maps:
                map_json.append({
                    'map'+ str(i) +'_name': map,
                })
                i+=1
            return map_json

        yield {
            'team1': extract_with_css('div.team1-gradient div.teamName::text'),
            'team2': extract_with_css('div.team2-gradient div.teamName::text'),
            'score1': extract_with_css('div.team1-gradient > div::text'),
            'score2': extract_with_css('div.team2-gradient > div::text'),
            'date': extract_with_css('.timeAndEvent .date::text'),
            'map': get_maps()
        }
