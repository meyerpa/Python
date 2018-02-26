# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:55:47 2017

@author: Paige
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
from sklearn.neural_network import MLPRegressor

# DATA

X_train, y_train = read_train()
X_test = read_test()

feature_names = choose_features(X_train, y_train, num_features=6)
feature_names.append('ID')
# narrow down data
X_train = X_train[feature_names]
X_test = X_test[feature_names]


# normalize data
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
# Don't cheat - fit only on training data
scalar = scaler.fit(X_train)  
X_train = scaler.transform(X_train)  
# apply same transformation to test data
X_test = scaler.transform(X_test) 

clf = MLPRegressor()
clf = clf.fit(X_train, y_train)
n_folds = 5
results = cross_val_score(clf, X_train, y_train.ix[:, 0].ravel(), cv=n_folds)
score = np.mean(results)
print("Cross-validation score {:}".format(score))