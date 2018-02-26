# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 01:09:05 2017

@author: Paige Meyer
"""


import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from k__best import choose_features
import pandas as pd
from read import read_train, read_test
import cross_val as cross

# DATA

X_train, y_train = read_train()
X_test = read_test()

feature_names = choose_features(X_train, y_train, num_features=6)
feature_names.append('ID')
# narrow down data
X_train = X_train[feature_names]
X_test = X_test[feature_names]


depths = range(1, 20)
n_trees = range(1, 100, 5)

predictions= []
classifiers = []
scores = []

# FIT MODEL
for n in n_trees:
    regr = RandomForestRegressor(n_estimators=n, max_depth=3)
    regr.fit(X_train, y_train)
    
    # MAKE PREDICTIONS
    # Predict on new data
    y_pred = regr.predict(X_test)
    predictions.append(y_pred)
    classifiers.append(regr)
    
    n_folds = 5
    score = cross.score(regr, X_train, y_train, n_folds)
    scores.append(score)

    # put predictions into csv
    IDs = pd.DataFrame(X_test["ID"])
    y_pred = pd.DataFrame(y_pred)
    pred_data = IDs.join(y_pred)
    pred_data.columns = ['ID', 'Prediction']
    pred_data.to_csv(path_or_buf="pred_rf{:}.csv".format(n), index=False)


# Plot the results
plt.plot(n_trees, scores)
plt.xlabel("number of trees")
plt.ylabel("score")
plt.title("Random Forest Cross Validation Score")
plt.legend()
plt.show()    

"""
# FIT MODEL
for depth in depths:
    regr = RandomForestRegressor(n_estimators=100, max_depth=depth)
    regr.fit(X_train, y_train)
    
    # MAKE PREDICTIONS
    # Predict on new data
    y_pred = regr.predict(X_test)
    predictions.append(y_pred)
    classifiers.append(regr)
    
    n_folds = 5
    score = cross.score(regr, X_train, y_train, n_folds)
    scores.append(score)

    # put predictions into csv
    IDs = pd.DataFrame(X_test["ID"])
    y_pred = pd.DataFrame(y_pred)
    pred_data = IDs.join(y_pred)
    pred_data.columns = ['ID', 'Prediction']
    pred_data.to_csv(path_or_buf="pred_rf{:}.csv".format(depth), index=False)


# Plot the results
plt.plot(depths, scores)
plt.xlabel("depth")
plt.ylabel("score")
plt.title("Random Forest Cross Validation Score")
plt.legend()
plt.show()
"""
