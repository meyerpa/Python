# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 01:09:05 2017

@author: Paige
"""

print(__doc__)

# Author: Tim Head <betatim@gmail.com>
#
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import pandas as pd


# DATA

feature = "Diabetes"
# get X and y data
train = pd.read_csv("train.csv", delimiter=",")
train = train.drop_duplicates() # ensure no duplicates
y_train = train[feature].to_frame()
names = y_train[feature].unique()
X_train = train.drop(feature, 1)
X_names = list(X_train)

# Get test data
test = pd.read_csv("test.csv", delimiter=",")
X_test = test

max_depth = 3
regr_multirf = MultiOutputRegressor(RandomForestRegressor(max_depth=max_depth))
regr_multirf.fit(X_train, y_train)

regr_rf = RandomForestRegressor(n_estimators=20, max_depth=max_depth)
regr_rf.fit(X_train, y_train)

# Predict on new data
y_multirf = regr_multirf.predict(X_test)
y_rf = regr_rf.predict(X_test)

# put predictions into csv
IDs = pd.DataFrame(X_test["ID"])
y_pred = pd.DataFrame(y_multirf)
pred_data = IDs.join(y_pred)
pred_data.columns = ['ID', 'Prediction']
pred_data.to_csv(path_or_buf="prediction_multirf.csv", index=False)



# score models
scores = cross_val_score(regr_rf, X_train, y_train)
score_multi = cross_val_score(y_multirf, X_train, y_train)

# Plot the results
plt.figure()
a = 0.4
#plt.scatter(y_test[:, 0], y_test[:, 1],
#            c="navy", s=s, marker="s", alpha=a, label="Data")
plt.plot(y_multirf,
            c="cornflowerblue", alpha=a,
            label="Multi RF")
plt.plot(y_rf,
            c="c", marker="^", alpha=a,
            label="RF")
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("target 1")
plt.ylabel("target 2")
plt.title("Comparing random forests and the multi-output meta estimator")
plt.legend()
plt.show()