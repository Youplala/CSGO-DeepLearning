import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import missingno as msno
import numpy as np
df = pd.read_csv('dataset/rounds.csv', error_bad_lines=False)

# Show the dataset shape and types of columns
df.shape
df.dtypes


# Investigate the empty values in the columns and fill them
df.isnull().any()
df = df.fillna(method='ffill')



unique = df["map_score1"].unique()
print(np.sort(unique)) # We see '-' so we replace it by 0
df["map_score1"] = df["map_score1"].replace(['-'],'0').astype(str).astype(int)
df["map_score2"] = df["map_score2"].replace(['-'],'0').astype(str).astype(int)


# Extract the difference of scores into y
y = df['map_score1'] - df['map_score2']


# Select the useless columns and remove them
useless_columns = [x+str(y) for x in ['team_player', 'player', 'kast'] for y in range(1,11)]
useless_columns = ['id', 'score1', 'score2',
'map_number','date','map_name'] + useless_columns
x = df.drop(useless_columns, axis=1)


# Preview final dataset
x.dtypes
print('New shape: ', x.shape)
x
teamnames=x[['team1','team2']]
teamnamesclean1=teamnames['team1'].drop_duplicates()
teamnamesclean2=teamnames['team2'].drop_duplicates()
teamnamesclean1
sum_of_rating_1_5=['rating1','rating2','rating3','rating4','rating5']
sum_of_rating_6_10=['rating6','rating7','rating8','rating9','rating10']
sum_addr_1_5=['adr1','adr2','adr3','adr4','adr5']
sum_addr_6_10=['adr6','adr7','adr8','adr9','adr10']
sum_kill_1_5=['kill1','kill2','kill3','kill4','kill5']
sum_kill_6_10=['kill6','kill7','kill8','kill9','kill10']
sum_deaths_1_5=['death1','death2','death3','death4','death5']
sum_deaths_6_10=['death6','death7','death8','death9','death10']
x['Sum_kill_1_5']=df[sum_kill_1_5].sum(axis=1,skipna=False)
x['Sum_kill_6_10']=df[sum_kill_6_10].sum(axis=1,skipna=False)
x['Sum_death_1_5']=df[sum_deaths_1_5].sum(axis=1,skipna=False)
x['Sum_death_6_10']=df[sum_deaths_6_10].sum(axis=1,skipna=False)
x['Sum_addr_1_5']=df[sum_addr_1_5].sum(axis=1,skipna=False)
x['Sum_addr_6_10']=df[sum_addr_6_10].sum(axis=1,skipna=False)
x['Sum_Rating_1_5']=df[sum_of_rating_1_5].sum(axis=1,skipna=False)
x['Sum_Rating_6_10']=df[sum_of_rating_6_10].sum(axis=1,skipna=False)
x['avg_kill_1_5']=df[sum_kill_1_5].mean(axis=1,skipna=False)
x['avg_kill_6_10']=df[sum_kill_6_10].mean(axis=1,skipna=False)
x['avg_death_1_5']=df[sum_deaths_1_5].mean(axis=1,skipna=False)
x['avg_death_6_10']=df[sum_deaths_6_10].mean(axis=1,skipna=False)
x['avg_addr_1_5']=df[sum_addr_1_5].mean(axis=1,skipna=False)
x['avg_addr_6_10']=df[sum_addr_6_10].mean(axis=1,skipna=False)
x['avg_Rating_1_5']=df[sum_of_rating_1_5].mean(axis=1,skipna=False)
x['avg_Rating_6_10']=df[sum_of_rating_6_10].mean(axis=1,skipna=False)
x.head()
teamnames=x[['team1','team2']]
teamnamesclean1=teamnames['team1'].drop_duplicates()
teamnamesclean2=teamnames['team2'].drop_duplicates()
teamnamesclean1
teamnamesclean1.append(teamnamesclean2)
teamscleanfull=teamnamesclean1.drop_duplicates()
teamslist=teamscleanfull.values.tolist()
teamsandid=[]
for i in range(len(teamslist)):
    teamsandid.append((teamslist[i],i))
teamsandid

x=x.sort_values('team1')
teamsandid=sorted(teamsandid)
teamsid=[]
teamnames=[]
for i in range(len(teamsandid)):
    teamsid.append(teamsandid[i][1])
    teamnames.append(teamsandid[i][0])
teamsid.append(21000)
teamsid.append(21020)
teamnames.append('FcottoNd')
teamnames.append('DOG77')
x['team1']=x['team1'].replace(teamnames,teamsid)
x['team2']=x['team2'].replace(teamnames,teamsid)

x.to_csv('dataset/new.csv', index=False)
