from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_iris()

x, y = data.data, data.target

clf = RandomForestClassifier(n_estimators=10)
clf.fit(x,y)
y_pred = clf.predict(x)

print(accuracy_score(y, y_pred))