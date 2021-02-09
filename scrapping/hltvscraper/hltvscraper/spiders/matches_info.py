import scrapy
from datetime import datetime
import dateparser


class MatchDetailSpider(scrapy.Spider):
    name = 'hltv_match_detail'
    start_urls = ['https://www.hltv.org/results&content=stats']
    for i in range(1,200):
        start_urls.append('https://www.hltv.org/results?offset='+str(i*100)+'&content=stats')

    def parse(self, response):
        match_links = response.css('div.results-all div.result-con > a.a-reset')
        yield from response.follow_all(match_links, self.parse_match)


    def parse_match(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def get_maps():
            map_json = []
            i=1
            for map in response.css('div.mapholder'):
                name = map.css('div.played div.mapname::text').get()
                score1 = map.css('div.results.played > div.results-left div.results-team-score::text').get()
                score2 = map.css('div.results.played > span.results-right div.results-team-score::text').get()

                app={
                    'map_name': name,
                    'map_number': i,
                    'score1': score1,
                    'score2': score2
                }
                if app['map_name'] != None:
                    map_json.append(app)
                    i+=1
            return map_json

        def get_players():
            player_json = []
            i=1
            for team in response.css('div#all-content table.table.totalstats'):
                team_name = team.css('tr.header-row a.teamName.team::text').get()
                for line in team.css('tr'):
                    name = line.css('span.player-nick::text').get()
                    kda = line.css('td.kd::text').get()
                    adr = line.css('td.adr::text').get()
                    kast = line.css('td.kast::text').get()
                    rating = line.css('td.rating::text').get()
                    app={
                        'teamname' : team_name,
                        'nick' : name,
                        'kill' : kda.split('-')[0],
                        'death' : kda.split('-')[1],
                        'adr': adr,
                        'kast' : kast,
                        'rating' : rating
                    }

                    if app['nick'] != None:
                        player_json.append(app)
                        i+=1
            return player_json

        yield {
            'id_match': response.url.split('/')[-2],
            'team1': extract_with_css('div.team1-gradient div.teamName::text'),
            'team2': extract_with_css('div.team2-gradient div.teamName::text'),
            'score1': extract_with_css('div.team1-gradient > div::text'),
            'score2': extract_with_css('div.team2-gradient > div::text'),
            'date': str(dateparser.parse(extract_with_css('.timeAndEvent .date::text'), date_formats=['%d %B %Y'])).split()[0],
            'map': get_maps(),
            'players': get_players()

        }
