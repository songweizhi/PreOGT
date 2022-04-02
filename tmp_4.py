import pandas as pd
import seaborn as sns
import matplotlib as plt
sns.set_theme(style="ticks")
import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.use('Agg')
# import matplotlib.pyplot as plt


# csv_in = '/Users/songweizhi/Documents/Machine_Learning/penguins.csv'
# df = pd.read_csv(csv_in)
# sns.pairplot(df, hue="species")
# plt.show()


csv_in = '/Users/songweizhi/Documents/Machine_Learning/diabetes.csv'

diabetes_df = pd.read_csv(csv_in, delimiter=',')
# print(diabetes_df.head())
# print(diabetes_df.info())
# print(diabetes_df.describe())
# print(diabetes_df.corr())


# f, ax = plt.subplots(1, figsize=(10,8))
# sns.heatmap(diabetes_df.corr(), annot=True, ax=ax)
# sns.countplot(x=diabetes_df.Outcome)
# plt.show()


# f, axes = plt.subplots(4,2, figsize=(20,20))
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.Pregnancies, ax=axes[0,0])
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.Glucose, ax=axes[0,1])
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.BloodPressure, ax=axes[1,0])
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.SkinThickness, ax=axes[1,1])
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.Insulin, ax=axes[2,0])
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.BMI, ax=axes[2,1])
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.DiabetesPedigreeFunction, ax=axes[3,0])
# sns.violinplot(x=diabetes_df.Outcome ,y=diabetes_df.Age, ax=axes[3,1])
# plt.show()


# column_names = diabetes_df.columns
# column_names = column_names.drop('Outcome')
# for name in column_names:
#     print('{}\n'.format(name))
#     print(diabetes_df.groupby(['Outcome'])[name].mean())
#     print('*'*50)
#     print()


# f, axes = plt.subplots(4,2, figsize=(20,20))
# sns.distplot(diabetes_df.Pregnancies, ax=axes[0,0])
# sns.distplot(diabetes_df.Glucose, ax=axes[0,1])
# sns.distplot(diabetes_df.BloodPressure, ax=axes[1,0])
# sns.distplot(diabetes_df.SkinThickness, ax=axes[1,1])
# sns.distplot(diabetes_df.Insulin, ax=axes[2,0])
# sns.distplot(diabetes_df.BMI, ax=axes[2,1])
# sns.distplot(diabetes_df.DiabetesPedigreeFunction, ax=axes[3,0])
# sns.distplot(diabetes_df.Age, ax=axes[3,1])
# plt.show()

diabetes_df.SkinThickness.replace(0, diabetes_df.SkinThickness.median(), inplace=True)
diabetes_df.Insulin.replace(0, diabetes_df.Insulin.median(), inplace=True)
diabetes_df.Glucose.replace(0, diabetes_df.Glucose.median(), inplace=True)
diabetes_df.BloodPressure.replace(0, diabetes_df.BloodPressure.median(), inplace=True)
diabetes_df.BMI.replace(0, diabetes_df.BMI.median(), inplace=True)


# f, axes = plt.subplots(4,2, figsize=(20,20))
# sns.distplot(diabetes_df.Pregnancies, ax=axes[0,0])
# sns.distplot(diabetes_df.Glucose, ax=axes[0,1])
# sns.distplot(diabetes_df.BloodPressure, ax=axes[1,0])
# sns.distplot(diabetes_df.SkinThickness, ax=axes[1,1])
# sns.distplot(diabetes_df.Insulin, ax=axes[2,0])
# sns.distplot(diabetes_df.BMI, ax=axes[2,1])
# sns.distplot(diabetes_df.DiabetesPedigreeFunction, ax=axes[3,0])
# sns.distplot(diabetes_df.Age, ax=axes[3,1])
# plt.show()


########################################################################################################################

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer

# Preparation of the data
# 1. Split the data into a training set, dev set and test set
# 2. Normalize the data
X = diabetes_df.drop('Outcome', axis =1).values
y = diabetes_df.Outcome.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
nl = Normalizer()
nl.fit(X_train)
X_train = nl.transform(X_train)
X_dev, X_test, y_dev, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=2)
X_dev = nl.transform(X_dev)
X_test = nl.transform(X_test)

# Network arhitecture
# 3 hidden layers
# Output layer with sigmoid activation

from keras.layers import Activation, Dense, Dropout, BatchNormalization, Input
from keras.models import Model

def nn():
    inputs = Input(name='inputs', shape=[X_train.shape[1],])
    layer = Dense(128, name='FC1')(inputs)
    layer = BatchNormalization(name='BC1')(layer)
    layer = Activation('relu', name='Activation1')(layer)
    layer = Dropout(0.3, name='Dropout1')(layer)
    layer = Dense(128, name='FC2')(layer)
    layer = BatchNormalization(name='BC2')(layer)
    layer = Activation('relu', name='Activation2')(layer)
    layer = Dropout(0.3, name='Dropout2')(layer)
    layer = Dense(128, name='FC3')(layer)
    layer = BatchNormalization(name='BC3')(layer)
    layer = Dropout(0.3, name='Dropout3')(layer)
    layer = Dense(1, name='OutLayer')(layer)
    layer = Activation('sigmoid', name='sigmoid')(layer)
    model = Model(inputs=inputs, outputs=layer)
    return model

model = nn()
model.summary()

