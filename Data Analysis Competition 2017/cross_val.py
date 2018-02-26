# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:15:09 2017

@author: Paige
"""


from sklearn.cross_validation import KFold, cross_val_score
import numpy as np

def score(clf, X_train, y_train, n_folds, scoring="roc_auc"):
    # score Model
    kf = KFold(len(y_train)//4, n_folds=5, shuffle=False)
    scores = cross_val_score(clf, X_train, y_train, cv=kf, scoring=scoring)
    score = np.mean(scores)
    return score