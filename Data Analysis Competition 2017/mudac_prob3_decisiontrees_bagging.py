# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 04:24:55 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:31:31 2017

@author: Paige
"""


import sklearn.tree as tree
import pandas as pd
from read import read_train, read_services, read_train_test, read_test
import cross_val as cross
from k__best import choose_features
import matplotlib.pylab as plt
from sklearn.ensemble import BaggingRegressor
import numpy as np

# DATA

X_train, y_train = read_train()
X_test = read_test()

feature_names = choose_features(X_train, y_train, num_features=5)
feature_names.append('ID')
# narrow down data
X_train = X_train[feature_names]
X_test = X_test[feature_names]

# BUILD TREE

classifiers = []
predictions = []
scores = []
n_repeat = 50
n_train = 50
n_test = 1000
noise = 0.1
number_leafs = range(4, 20)

estimators = [("Tree", tree.DecisionTreeRegressor()),
              ("Bagging(Tree)", BaggingRegressor(tree.DecisionTreeRegressor()))]
n_estimators = len(estimators)


for n, (name, estimator) in enumerate(estimators):
    # Compute predictions
    y_predict = np.zeros((n_test, n_repeat))

    for i in range(n_repeat):
        estimator.fit(X_train[i], y_train[i])
        y_predict[:, i] = estimator.predict(X_test)

    # Bias^2 + Variance + Noise decomposition of the mean squared error
    y_error = np.zeros(n_test)

    for i in range(n_repeat):
        for j in range(n_repeat):
            y_error += (y_test[:, j] - y_predict[:, i]) ** 2

    y_error /= (n_repeat * n_repeat)

    y_noise = np.var(y_test, axis=1)
    y_bias = (f(X_test) - np.mean(y_predict, axis=1)) ** 2
    y_var = np.var(y_predict, axis=1)

    print("{0}: {1:.4f} (error) = {2:.4f} (bias^2) "
          " + {3:.4f} (var) + {4:.4f} (noise)".format(name,
                                                      np.mean(y_error),
                                                      np.mean(y_bias),
                                                      np.mean(y_var),
                                                      np.mean(y_noise)))


    
    
for leaf in number_leafs:
    clf = tree.DecisionTreeRegressor(max_leaf_nodes=leaf)
    
    clf.fit(X_train, y_train) 
    y_pred = clf.predict(X_test)
    classifiers.append(clf)
    predictions.append(y_pred)

# cross validate
for i in range(len(number_leafs)):
    n_folds = 3
    score = cross.score(classifiers[i], X_train, y_train, n_folds, scoring="roc_auc")
    print("Score{}".format(number_leafs[i]), score)
    scores.append(score)
    

# Display trees
for i in range(len(number_leafs)):
    dot = "practice_{:}leaves.dot".format(number_leafs[i])
    dot_data = tree.export_graphviz(clf, out_file=dot,
                                    feature_names=feature_names, 
                                    filled=True, rounded=True,)


    IDs = pd.DataFrame(X_test['ID'])
    y_pred = pd.DataFrame(predictions[i])
    pred_data = IDs.join(y_pred)
    pred_data.columns = ['ID', 'Prediction']
    pred_data.to_csv(path_or_buf="pred_decisiontree{:}.csv".format(number_leafs[i]),
                     index=False)

plt.plot(number_leafs, scores)
plt.xlabel("Number of leaves")
plt.ylabel("Score")
plt.title("Decision Tree Score with {:}".format(feature_names))
plt.show()
