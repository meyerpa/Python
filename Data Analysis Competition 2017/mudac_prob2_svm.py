# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:31:31 2017

@author: Paige
"""


import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from read import read_train, read_test
import sklearn.svm as svm

# DATA

X_train, _, y_train, _ = read_train()
X_test = read_test()

feature_names = list(X_train)

chooser = SelectKBest(chi2, k=4)

fit_transformed_features = chooser.fit_transform(X_train, y_train)
shape = fit_transformed_features.shape

# get feature names
mask = chooser.get_support() #list of booleans
new_features = [] # The list of your K best features

for boolean, feature in zip(mask, feature_names):
    if boolean:
        new_features.append(feature)

classifiers = []
iden = []
predictions = []


clf = svm.SVC(kernel='linear', gamma=1) 
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
classifiers.append(clf)
predictions.append(y_pred)


# Send to test file
IDs = pd.DataFrame(X_test['ID'])
y_pred = pd.DataFrame(y_pred)
pred_data = IDs.join(y_pred)
pred_data.columns = ['ID', 'Prediction']
pred_data.to_csv(path_or_buf="prediction_svc.csv", index=False)
