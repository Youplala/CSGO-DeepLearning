import json
import pandas as pd
import missingno as msno
import numpy as np
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from tensorflow import keras

data = pd.read_csv('dataset/matches.csv')
del data['players']
data.shape
data.dtypes
