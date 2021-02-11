import pandas as pd
import numpy as np


df = pd.read_csv('dataset/final_dataset.csv',low_memory=False)
matches = pd.read_csv('dataset/matches.csv')

matches.head()
elo = 2000

sorted_df = matches.sort_values(by='id_match')
sorted_df.head(1)
len(sorted_df)
unique_teams = sorted_df.team1.unique()
unique_teams2 = sorted_df.team2.unique()
unique_teams.append(unique_teams2)
len(unique_teams)
len(unique_teams2)
elo = []
dict = {'team': r}
for row in sorted_df.itertuples():
    elo.append()
dict = {'id_match': row.id_match}
for map in row.map:
    i = map['map_number']
    dict['map'+str(i)+'_name'] = map['map_name']
    dict['map'+str(i)+'_score1'] = map['score1']
    dict['map'+str(i)+'_score2'] = map['score2']
df_maps.append(dict)


for i in range(len(df.id_match)):
    temp.append(elo)
df['elo_team1'] = temp
df['elo_team2'] = temp
