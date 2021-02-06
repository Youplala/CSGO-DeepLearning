import pandas as pd

df = pd.read_csv('scrapped/scraper_teams.csv', header=None)
match=pd.DataFrame()
pair=[]
odd=[]
for i, row in df.iterrows():
    if i%2 == 0:
        pair.append(row[0])
    else:
        odd.append(row[0])
match['team1'] = pair
match['team2'] = odd
match
