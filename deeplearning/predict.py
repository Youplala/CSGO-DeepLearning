import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import missingno as msno
import numpy as np
import tensorflow as tf
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from tensorflow import keras
from sklearn.linear_model import LinearRegression

df = pd.read_csv('dataset/rounds.csv', error_bad_lines=False)
df.shape
df.dtypes
useless_columns = [x+str(y) for x in ['team_player', 'player', 'kast'] for y in range(1,11)]
useless_columns = ['id', 'score1', 'score2', 'map_number','team1', 'team2', 'date','map_name'] + useless_columns
data = df.drop(useless_columns, axis=1)
unique = data["map_score1"].unique()
print(np.sort(unique))
unique2 = data["map_score2"].unique()
data["map_score1"] = data["map_score1"].replace(['-'],'0').astype(str).astype(int)
data["map_score2"] = data["map_score2"].replace(['-'],'0').astype(str).astype(int)

data.dtypes
data.shape
data.head(10)
data.isnull().any()
data = data.fillna(method='ffill')
y = data['map_score1'] - data['map_score2']
data = data.drop(['map_score1', 'map_score2'], axis=1)
data.head()

train_x, test_x, train_y, test_y = train_test_split(data, y, test_size = 0.3, random_state=7)


lr = LinearRegression().fit(train_x, train_y)
y_pred = lr.predict(test_x)
accuracy = lr.score(test_x,test_y)
print(accuracy*100,'%')

#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#train_x = sc.fit_transform(train_x)
#test_x = sc.transform(test_x)

model = keras.Sequential([
    keras.layers.Dense(1024, input_dim=train_x.shape[1], kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(512, kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(512, kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(512, kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(256, kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(256, kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(256, kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(128, kernel_initializer='normal', activation='relu'),
    keras.layers.Dense(1, kernel_initializer='normal', activation='linear'),
])
model.compile(loss='mse', optimizer='adam', metrics=['mae', 'mape'])
history = model.fit(train_x,train_y,epochs=50,validation_split=0.3, batch_size = 5000)
prediction = model.predict(test_x)
rounded = np.rint(prediction)

a = np.subtract(np.array(pd.DataFrame(test_y, columns=['actual'])), np.array(pd.DataFrame(rounded, columns=['pred'])))
sns.displot(a)



len([x for x in a if np.abs(x)<2]) / len(a) * 100

pred = pd.DataFrame(rounded, columns=['pred'])
df = pd.merge(pd.DataFrame(test_y, columns=['true']), pred)

print(pred)
plt.title('Loss / Mean Squared Error')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()
# plt.plot(test_y, color = 'red', label = 'Real data')
# plt.plot(prediction, color = 'blue', label = 'Predicted data')
# plt.title('Prediction')
# plt.legend()
# plt.show()


sns.displot(pd.DataFrame(prediction))
plt.show()
