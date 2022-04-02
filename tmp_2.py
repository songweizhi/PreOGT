import pandas as pd
from sklearn.model_selection import train_test_split


df_in = '/Users/songweizhi/Documents/Research/PreTR_ML/data_in_2483/combined.txt'

df = pd.read_table(df_in)

# Assign data from first four columns to X variable
X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

print(X_train)
print(X_test)
print(y_train)
print(y_test)


# # Assign data from first fifth columns to y variable
# y = df.select_dtypes(include=[object])

# from sklearn.neural_network import MLPClassifier
# mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
# mlp.fit(X_train, y_train.values.ravel())
#
# predictions = mlp.predict(X_test)
