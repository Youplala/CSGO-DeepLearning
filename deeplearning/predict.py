
# Import all the necessary libraries
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from tensorflow import keras
from sklearn.linear_model import LinearRegression

# Read the csv file ignoring errors
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
useless_columns = ['id', 'score1', 'score2', 'map_score1', 'map_score2', 'map_number','team1', 'team2', 'date','map_name'] + useless_columns
x = df.drop(useless_columns, axis=1)


# Preview final dataset
x.dtypes
print('New shape: ', x.shape)
x.head(10)


'''

#new = pd.read_csv('dataset/newdataset2.csv')
#new = a.drop(['team1', 'team2'], axis=1)



unique = new["map_score1"].unique()
print(np.sort(unique)) # We see '-' so we replace it by 0
df["map_score1"] = df["map_score1"].replace(['-'],'0').astype(str).astype(int)
df["map_score2"] = df["map_score2"].replace(['-'],'0').astype(str).astype(int)


# Extract the difference of scores into y
y = new['map_score1'] - new['map_score2']

y
# Select the useless columns and remove them
#useless_columns = [x+str(y) for x in ['team_player', 'player', 'kast'] for y in range(1,11)]
useless_columns = []
useless_columns = ['map_score1', 'map_score2','team1', 'team2'] + useless_columns
x = new.drop(useless_columns, axis=1)

x
new.dtypes
x.isnull().any()
new

'''

#df = df.fillna(method='ffill')
# Separate data into test and train
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.2, random_state=7)


# Trying out a simple Linear Regression
lr = LinearRegression().fit(train_x, train_y)
y_pred = lr.predict(test_x)
accuracy = lr.score(test_x,test_y)
print('Linear Regression accuracy: ', accuracy*100,'%')

rounded = np.rint(y_pred)
a = np.subtract(np.array(pd.DataFrame(test_y, columns=['actual'])), np.array(pd.DataFrame(rounded, columns=['pred'])))

def accuracy(a, i):
    acc = len([x for x in a if np.abs(x)<=i]) / len(a) * 100
    return acc

print('### Linear Regression Accuracy ###\n')
for i in range(1,5):
    print('Accuracy +-', i, 'rounds: ', accuracy(a, i))


'''
# Scale data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
train_x = sc.fit_transform(train_x)
test_x = sc.transform(test_x)
'''

# Instanciate Deep Learning Keras model
model = keras.Sequential([
    keras.layers.Dense(512, input_dim=train_x.shape[1], activation='relu'),
    keras.layers.Dropout(0.5, seed=7),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dropout(0.5, seed=7),
    keras.layers.Dense(1),
])


# Parameters
loss       = 'mse'
optimizer  = 'adam'
metrics    = ['mae']
epochs     = 60
validation = 0.3
batch      = 32


# Compile and fit model
model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
history = model.fit(train_x,train_y,epochs=epochs,validation_split=validation, batch_size = batch)


# Predict and compute mean loss
prediction = model.predict(test_x)
rounded = np.rint(prediction)
score = model.evaluate(test_x,test_y)
print(f'Test loss: {score[0]} / Test accuracy: {score[1]}')

model.save('model')

# Compute difference between prediction true value and prediction
a = np.subtract(np.array(pd.DataFrame(test_y, columns=['actual'])), np.array(pd.DataFrame(rounded, columns=['pred'])))

def accuracy(a, i):
    acc = len([x for x in a if np.abs(x)<=i]) / len(a) * 100
    return acc

print('### Deep Neural network Accuracy ###\n')
for i in range(1,5):
    print('Accuracy +-', i, 'rounds: ', accuracy(a, i))


# Plot predicition distribution
preds = pd.DataFrame(rounded, columns=['preds'])
sns.displot(prediction)
plt.title('Distribution of the predicted difference of rounds')
plt.show()


#Plot loss vs validation loss
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
