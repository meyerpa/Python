# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:10:05 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:49:40 2017

@author: Paige Meyer
"""


import matplotlib.pyplot as plt
from k__best import choose_features
from read import read_train, read_test
import cross_val as cross
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import cross_val_score

from sklearn.naive_bayes import BernoulliNB

# DATA

X_train, y_train = read_train()
X_test = read_test()

feature_names = choose_features(X_train, y_train, num_features=6)
feature_names.append('ID')
# narrow down data
X_train = X_train[feature_names]
X_test = X_test[feature_names]

trees = np.arange(1, 100)

estimators = [('logistic', LogisticRegression()),
              ('cart', DecisionTreeRegressor()),
              ('svm', SVC()),
              ('knn', KNeighborsRegressor()),
              ('BernouliNB', BernoulliNB())]

ensemble = VotingClassifier(estimators)
n_folds = 5
results = cross_val_score(ensemble, X_train, y_train.ix[:, 0].ravel(), cv=n_folds)
score = np.mean(results)
print("Cross-validation score {:}".format(score))
