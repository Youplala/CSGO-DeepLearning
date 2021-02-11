import json
import pandas as pd
import missingno as msno
import numpy as np
f = open('matches.json',)

# returns JSON object as a dictionary
data = json.load(f)
#msno.matrix(df)
df = pd.DataFrame(data)
#del df['players']
df.head()

len(df['id_match'])

df_maps=[]
for row in df.itertuples(index=False):
    dict = {'id_match': row.id_match}
    for map in row.map:
        i = map['map_number']
        dict['map'+str(i)+'_name'] = map['map_name']
        dict['map'+str(i)+'_score1'] = map['score1']
        dict['map'+str(i)+'_score2'] = map['score2']
    df_maps.append(dict)

maps = pd.DataFrame(df_maps)


#print(df.head())

a = pd.merge(df, maps, on='id_match', how='inner')

len(a['id_match'])
del a['map']
a.head()

a.to_csv('dataset/matches.csv', index =False)

df_players = []
for row in a.itertuples(index = False):
    dict = {'id_match': row.id_match}
    for player in row.players:
        out = {**dict, **player}
        df_players.append(out)
df_players = pd.DataFrame(df_players)
df_players.head()
df = a.merge(df_players, how='left')
del df['players']
df.head()
print(len(df))
df.to_csv('dataset/final_dataset.csv', header=True, index=False)
print('Extraction complete')
