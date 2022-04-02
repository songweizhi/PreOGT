import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score



# df = pd.read_csv('/Users/songweizhi/Documents/Machine_Learning/diabetes.csv')
# df = pd.read_csv(sklearn.datasets.load_diabetes)
#
#
# target_column = ['diabetes']
# predictors = list(set(list(df.columns)) - set(target_column))
# df[predictors] = df[predictors]/df[predictors].max()
#
#
# X = df[predictors].values
# y = df[target_column].values
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
# print(X_train.shape)
# print(X_test.shape)

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report, accuracy_score
# from sklearn.preprocessing import Normalizer
# from keras.layers import Activation, Dense, Dropout, BatchNormalization, Input
# from keras.models import Model
# #from keras.optimizers import Adam
# from keras.callbacks import ReduceLROnPlateau, EarlyStopping
# #%matplotlib inline
# plt.style.use('fivethirtyeight')
diabetes_df = pd.read_csv('/Users/songweizhi/Documents/Machine_Learning/dataset/diabetes.csv', delimiter=',')
print(diabetes_df.head())
print(diabetes_df.info())
print(diabetes_df.describe())
print(diabetes_df.corr())

f, ax = plt.subplots(1, figsize=(10,8))
sns.heatmap(diabetes_df.corr(), annot=True, ax=ax)
sns.countplot(x=diabetes_df.Outcome)




