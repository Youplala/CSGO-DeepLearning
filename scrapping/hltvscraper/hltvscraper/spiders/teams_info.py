import scrapy
from datetime import datetime
import dateparser

class TeamDetails(scrapy.Spider):
    name = 'hltv_team_detail'
    start_urls = ['https://www.hltv.org/ranking/teams/2021/march/15']
    #for i in range(1,200):
    #    start_urls.append('https://www.hltv.org/results?offset='+str(i*100)+'&content=stats')

    def parse(self, response):
        team_links = response.css('div.ranked-team.standard-box div.more > a.moreLink:nth-child(1)')
        yield from response.follow_all(team_links, self.parse_teams)

    def parse_teams(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def get_teams():
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

        yield {
            'id_match': response.url.split('/')[-2],
            'team1': extract_with_css('div.team1-gradient div.teamName::text'),
            'team2': extract_with_css('div.team2-gradient div.teamName::text'),
            'score1': extract_with_css('div.team1-gradient > div::text'),
            'score2': extract_with_css('div.team2-gradient > div::text'),
            'date': str(dateparser.parse(extract_with_css('.timeAndEvent .date::text'), date_formats=['%d %B %Y'])).split()[0],
            'map': get_teams(),
            'players': get_players()
        }
