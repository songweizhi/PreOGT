import pandas as pd
from sklearn.model_selection import train_test_split


df_in = '/Users/songweizhi/Documents/Research/PreTR_ML/data_in_2483/combined.txt'


df = pd.read_table(df_in)
X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)




from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
X, y = make_regression(n_samples=200, random_state=1)
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
regr = MLPRegressor(random_state=1, max_iter=500).fit(X_train, y_train)
print(regr.predict(X_test[:2]))
#print(regr.predict(y_test[:2]))
