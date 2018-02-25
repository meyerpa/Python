# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:58:56 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:05:29 2017

@author: Paige
"""

import numpy as np
from numpy.linalg import eigh


a = np.array([[1, 4],
              [4, 1]])
print('Vector: \n{}'.format(a))


vals, vect = eigh(a)

# save principle axes
axis1 = vect[:, 0]
axis2 = vect[:, 1]
# assert principle axes are perpendicular
assert(np.dot(axis2, axis1) == 0)

print("Eigenvalue 1: {:0.5f}, Eigenvector 1: {}".format(vals[0], axis1))
print("Eigenvalue 2: {:0.5f}, Eigenvector 2: {}".format(vals[1], axis2))

# extra credit 
b = np.array([[0, -1],
              [1,  0]])
print('\nVector:\n{}'.format(b))

vals, vect = eigh(b)

# save principle axes
axis1 = vect[:, 0]
axis2 = vect[:, 1]
# assert principle axes are perpendicular
assert(np.dot(axis2, axis1) == 0)

print("Eigenvalue 1: {:0.5f}, Eigenvector 1: {}".format(vals[0], axis1))
print("Eigenvalue 2: {:0.5f}, Eigenvector 2: {}".format(vals[1], axis2))
