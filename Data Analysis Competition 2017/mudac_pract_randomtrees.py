# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 00:11:16 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:43:58 2017

@author: Paige
"""
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.cross_validation import ShuffleSplit, train_test_split
from sklearn.learning_curve import validation_curve
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

param_name = "max_features"
param_range = range(1, X_train.shape[1] + 1)

for Forest, color, label in [(RandomForestClassifier, "g", "RF"), 
                             (ExtraTreesClassifier, "r", "ETs")]:
    _, test_scores = validation_curve(
                        Forest(n_estimators=100, n_jobs=-1), X, y,
                        cv = ShuffleSplit(n=len(X), n_iter=10, test_size =0.25),
                        param_name=param_name, param_range=param_range)
    test_scores_mean = np.mean(-test_scores, axis=1)
    plt.plot(param_range, test_scores_mean, label=label, color=color)
    
plt.xlabel(param_name)
plt.xlim(1, np.max(param_range))
plt.ylabel("MSE")
plt.legend(loc="best")
plt.show()
