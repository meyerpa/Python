# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:49:40 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:42:18 2017

@author: Paige Meyer
"""



import matplotlib.pyplot as plt
from k__best import choose_features
from read import read_train, read_test
import cross_val as cross
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

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
trees = np.arange(1, 100)

predictions= []
classifiers = []
scores = []

# FIT MODEL
for n_tree in trees:
    # defaulted to base_estimator as decision tree regressor
    regr = GradientBoostingRegressor(n_estimators=n_trees)
    regr.fit(X_train, y_train)
    
    # MAKE PREDICTIONS
    # Predict on new data
    y_pred = regr.predict(X_test)
    predictions.append(y_pred)
    classifiers.append(regr)
    
    n_folds = 5
    score = cross.score(regr, X_train, y_train, n_folds)
    scores.append(score)

plt.plot(trees, scores)
plt.xlabel("Number Trees")
plt.ylabel("Score")
plt.title("Schochastic Gradient Boosted Decision Tree")
plt.show()

high_score = max(scores)
best_n_trees = trees[high_score == scores]
print("Cross-validation {:} with {:} trees".format(high_score, best_n_trees))
