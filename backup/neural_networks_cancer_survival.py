
# https://machinelearningmastery.com/neural-network-for-cancer-survival-dataset/

import os
import numpy as np
from pandas import read_csv
from matplotlib import pyplot
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow import keras
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# disable warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


haberman_csv = '/Users/songweizhi/Documents/Machine_Learning/dataset/haberman.csv'

df = read_csv(haberman_csv, header=None)
# print(df.shape)
# print(df.describe())
# # plot histograms
# df.hist()
# pyplot.show()



# # summarize the class ratio of the haberman dataset
# from pandas import read_csv
# from collections import Counter
# # define the location of the dataset
# url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/haberman.csv'
# # define the dataset column names
# columns = ['age', 'year', 'nodes', 'class']
# # load the csv file as a data frame
# dataframe = read_csv(haberman_csv, header=None, names=columns)
#
# # summarize the class distribution
# target = dataframe['class'].values
# counter = Counter(target)
# for k,v in counter.items():
# 	per = v / len(target) * 100
# 	print('Class=%d, Count=%d, Percentage=%.3f%%' % (k, v, per))
#


# fit a simple mlp model on the haberman and review learning curves



# load the dataset
df = read_csv(haberman_csv, header=None)
# split into input and output columns
X, y = df.values[:, :-1], df.values[:, -1]
# ensure all data are floating point values
X = X.astype('float32')
# encode strings to integer
y = LabelEncoder().fit_transform(y)
# split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y, random_state=3)
# determine the number of input features
n_features = X.shape[1]
# define model
model = keras.Sequential()
model.add(keras.layers.Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(keras.layers.Dense(1, activation='sigmoid'))
# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy')
# fit the model
history = model.fit(X_train, y_train, epochs=200, batch_size=16, verbose=0, validation_data=(X_test,y_test))

# predict test set
#yhat = model.predict_classes(X_test) # old version
yhat = (model.predict(X_test) > 0.5).astype("int32")

# evaluate predictions
score = accuracy_score(y_test, yhat)
print('Accuracy: %.3f' % score)
# # plot learning curves
# pyplot.title('Learning Curves')
# pyplot.xlabel('Epoch')
# pyplot.ylabel('Cross Entropy')
# pyplot.plot(history.history['loss'], label='train')
# pyplot.plot(history.history['val_loss'], label='val')
# pyplot.legend()
# pyplot.show()


#################### Robust Model Evaluation ####################

# k-fold cross-validation of base model for the haberman dataset


# prepare cross validation
kfold = StratifiedKFold(10)
# enumerate splits
scores = list()
for train_ix, test_ix in kfold.split(X, y):
	# split data
	X_train, X_test, y_train, y_test = X[train_ix], X[test_ix], y[train_ix], y[test_ix]
	# determine the number of input features
	n_features = X.shape[1]
	# define model
	model = keras.Sequential()
	model.add(keras.layers.Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
	model.add(keras.layers.Dense(1, activation='sigmoid'))
	# compile the model
	model.compile(optimizer='adam', loss='binary_crossentropy')
	# fit the model
	model.fit(X_train, y_train, epochs=200, batch_size=16, verbose=0)
	# predict test set
	#yhat = model.predict_classes(X_test)
	yhat = (model.predict(X_test) > 0.5).astype("int32")

	# evaluate predictions
	score = accuracy_score(y_test, yhat)
	print('>%.3f' % score)
	scores.append(score)

# summarize all scores
print('Mean Accuracy: %.3f (%.3f)' % (np.mean(scores), np.std(scores)))


#################### Final Model and Make Predictions ####################

# fit a final model and make predictions on new data for the haberman dataset

# split into input and output columns
X, y = df.values[:, :-1], df.values[:, -1]
# ensure all data are floating point values
X = X.astype('float32')
# encode strings to integer
le = LabelEncoder()
y = le.fit_transform(y)
# determine the number of input features
n_features = X.shape[1]
# define model
model = keras.Sequential()
model.add(keras.layers.Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(keras.layers.Dense(1, activation='sigmoid'))
# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy')
# fit the model
model.fit(X, y, epochs=200, batch_size=16, verbose=0)
# define a row of new data
row = [30, 64, 1]
# make prediction
#yhat = model.predict_classes([row])
yhat = (model.predict([row]) > 0.5).astype("int32")

# invert transform to get label for class
yhat = le.inverse_transform(yhat)
# report prediction
print('Predicted: %s' % (yhat[0]))



