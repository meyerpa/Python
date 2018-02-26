# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:42:18 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 01:09:05 2017

@author: Paige Meyer
"""


import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from k__best import choose_features
import pandas as pd
from read import read_train, read_test
import cross_val as cross
from sklearn.ensemble import AdaBoostRegressor

# DATA

X_train, y_train = read_train()
X_test = read_test()

feature_names = choose_features(X_train, y_train, num_features=6)
feature_names.append('ID')
# narrow down data
X_train = X_train[feature_names]
X_test = X_test[feature_names]


depth = 3
n_trees = 50

predictions= []
classifiers = []
scores = []

# FIT MODEL
# defaulted to base_estimator as decision tree regressor
regr = AdaBoostRegressor(n_estimators=n_trees)
regr.fit(X_train, y_train)

# MAKE PREDICTIONS
# Predict on new data
y_pred = regr.predict(X_test)
predictions.append(y_pred)
classifiers.append(regr)

n_folds = 3
score = cross.score(regr, X_train, y_train, n_folds)
scores.append(score)

# put predictions into csv
IDs = pd.DataFrame(X_test["ID"])
y_pred = pd.DataFrame(y_pred)
pred_data = IDs.join(y_pred)
pred_data.columns = ['ID', 'Prediction']
pred_data.to_csv(path_or_buf="pred_rf{:}.csv".format(depth), index=False)

   
