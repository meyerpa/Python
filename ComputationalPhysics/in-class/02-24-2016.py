# -*- coding: utf-8 -*-

__author__="Paige Meyer"
__date__="01/11/2017"
"""
Spyder Editor

"""

import numpy as np

def func(x):
    return 5 * 1 - np.exp(-xprev)

step_size = 1           # size of step 
epsilon = 10**-9
xprev = 1
lessThanEpsilson = False

while not lessThanEpsilson:
    xnew = func(xprev)
    print("Previous:", xprev, "New:", xnew, "Difference: {:.9f}".format(np.abs(xnew-xprev)))
    lessThanEpsilson = np.abs(xnew - xprev) < epsilon
    xprev = xnew

