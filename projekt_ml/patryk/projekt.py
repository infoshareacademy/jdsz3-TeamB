from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import numpy as np
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('CreditNumeric.csv')
df = df.drop(['Unnamed: 0'], axis=1)

df = df.drop(['Gender', 'Student', 'Married', 'Ethnicity'], axis=1)
x = df.drop(['Rating'], axis=1).values
y = df.Rating.values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

model = SVR(kernel='linear', gamma='auto')

scores = cross_val_score(model, x_train, y_train, cv=5)
score = scores.mean()
model.fit(x_train, y_train)
print(score)

score2 = model.score(x_test, y_test)
print(score2)

print(list(df.columns.values))
x_new = [[10000, 0, 0, 0, 5, 0, 0, 0, 0, 2]]
y_new = model.predict(x_new)
print("X=%s, Predicted=%s" % (x_new[0], y_new[0]))
