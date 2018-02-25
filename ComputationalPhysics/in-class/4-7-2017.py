# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:43:36 2017

@author: Paige
"""

import random as random
import matplotlib.pylab as plt

random.seed(42)
N = 1000
results = []
for i in range(N):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    results.append(die1 + die2)

plt.hist(results, bins=11)
plt.xlabel("Sum of two die")
plt.ylabel("Count out of "+str(N))
plt.show()