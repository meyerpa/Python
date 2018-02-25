# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:38:19 2017

@author: Paige
"""

import numpy as np

'''
def func(x):
    # Defining the function for x = f(x)
    return 5 * (1 - np.exp(-x))
'''


def func(x):
    # return 2 * x**2
    # return np.exp(1-x**2)
    return np.sqrt(1 - np.log(x))

x = 0.5                # initial guess
N = 50                 # Number of times to loop

for i in range(N):
    f = func(x)
    print("i:", i, " x =", x, " f(x) =", f, " diff:", np.abs(f-x))
    x = f
