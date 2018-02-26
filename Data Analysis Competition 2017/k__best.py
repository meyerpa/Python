# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:55:00 2017

@author: Paige
"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


def choose_features(X_train, y_train, num_features=3):
    
    feature_names = list(X_train)
    
    chooser = SelectKBest(k=4)
    
    chooser.fit_transform(X_train, y_train)
    
    # get feature names
    mask = chooser.get_support() #list of booleans
    new_features = [] # The list of your K best features
    
    for boolean, feature in zip(mask, feature_names):
        if boolean:
            new_features.append(feature)
            
    return new_features