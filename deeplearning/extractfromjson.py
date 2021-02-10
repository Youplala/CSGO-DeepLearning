import json
import pandas as pd
import missingno as msno

f = open('matches.json',)

# returns JSON object as a dictionary
data = json.load(f)
#msno.matrix(df)
df = pd.DataFrame(data)
del df['players']
df.head()
mapnumber = []
for i in range(1,6):
    mapnumber.append('map'+str(i))
map_df = pd.DataFrame(columns=mapnumber)
pd.merge(df, map_df)
for row in df.itertuples(index=False):
    i=1
    for map in row.map:
        df[map['map_number']] = map['map_name']
print(df.head())
