from sklearn.ensemble import RandomForestClassifier

# https://scikit-learn.org/stable/getting_started.html#model-evaluation

clf = RandomForestClassifier(random_state=0)

# 2 samples, 3 features
X = [[1,  2,  3], [11, 12, 13]]

# classes of each sample
y = ['apple', 'banana']

# train the model
clf.fit(X, y)

# predict classes of the training data
print(clf.predict(X))
print(clf.predict([[4, 5, 6], [14, 15, 16]]))
print(clf.predict([[14, 15, 16], [4, 5, 6]]))
