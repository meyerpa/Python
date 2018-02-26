# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:25:00 2017

@author: Paige Meyer
"""


import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from read import read_train, read_test
import matplotlib.pylab as plt


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
        
for feature in new_features:
    y = y_train.as_matrix().reshape(1, len(y_train))[0]
    for (xe, ye) in zip(X_train[feature].as_matrix(), y):
        plt.scatter(xe, ye)
    plt.title(feature)
    plt.ylabel('Negative')
    plt.xlabel(feature)
    plt.show()


