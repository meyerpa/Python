# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:30:17 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:55:47 2017

@author: Paige
"""



import matplotlib.pyplot as plt
from k__best import choose_features
from read import read_train, read_test
import cross_val as cross
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn.model_selection import cross_val_score

# DATA

X_train, y_train = read_train()
X_test = read_test()

feature_names = choose_features(X_train, y_train, num_features=6)
feature_names.append('ID')
# narrow down data
X_train = X_train[feature_names]
X_test = X_test[feature_names]


clf = MultinomialNB()
clf = clf.fit(X_train, y_train)
n_folds = 5
results = cross_val_score(clf, X_train, y_train.ix[:, 0].ravel(), cv=n_folds)
score = np.mean(results)
print("Cross-validation score {:}".format(score))