# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:01:23 2017

@author: Paige Meyer
@date="02/15/2017"
@version= 1.0
PHYS 350 - Computational Physics
Lab 06
Description:

"""

import numpy as np
from numpy.linalg import eigh
import matplotlib.pyplot as plt


def angle(A, B):
    """Returns the angle between numpy arrays A and B

    Parameters
    ----------
    A : numpy array
        Holds each point classifying the vector created
    B : numpy array
        Holds each point classifying the vector created

    Returns
    -------
    angle : float
        The angle in radians between A and B.
    """
    return np.arccos(np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B)))


n = 3           # Number of dimensions for array
a = 0.1         # length of side of triangle in meters
sigma = 0.1     # mass over area for triangle in kg/m^2
InertiaTensor = sigma * a**4 * \
                np.array([[1/12,  -1/24,   0],
                         [-1/24,  1/12,   0],
                         [0,      0,    1/6]])  # angular momentum
omega = np.array([1, 2, 3])
L = np.array([1, -2, 1])

vals, vect = eigh(InertiaTensor)

num_pts = 105

# save principle axes
axis1 = vect[:, 0]
axis2 = vect[:, 1]
axis3 = vect[:, 2]

# assert principle axes are perpendicular
assert(np.dot(axis2, axis1) == 0)
assert(np.dot(axis2, axis3) == 0)
assert(np.dot(axis1, axis3) == 0)

print("Eigenvalue 1 {:0.5f}, Eigenvector 1 {}".format(vals[0], axis1))
print("Eigenvalue 2 {:0.5f}, Eigenvector 2 {}".format(vals[1], axis2))
print("Eigenvalue 3 {:0.5f}, Eigenvector 3 {}".format(vals[2], axis3))
# Note; these do make sense, correspond to arrays with symmetric mass
# distribution of the triangle
# These were the same result as previously, but all Eigenvalues could flip
# 180 degrees and still be correct.
# Also, eigenvalues make sense because as the weight is distributed
# further from the axis of rotation, the higher the eigenvalue.


# for triangle
I = np.array([[1/12,  -1/24, 0],
              [-1/24,  1/12, 0],
              [0,      0,    1/6]])

a_array = np.linspace(0.01, 0.25, num_pts)
I1_array = np.empty(num_pts)
I2_array = np.empty(num_pts)
I3_array = np.empty(num_pts)

for i in range(num_pts):
    new_I = I * sigma * (a_array[i])**4
    vals, vect = eigh(new_I)
    print(vals)
    # save principle axes
    I1_array[i] = vals[0]
    I2_array[i] = vals[1]
    I3_array[i] = vals[2]


# Add plotting commands
plt.plot(a_array, I1_array, 'r', label="First Axis Inertia")
plt.plot(a_array, I2_array, 'b', label="Second Axis Inertia")
plt.plot(a_array, I3_array, 'g', label="Third Axis Inertia")

# formal plot
plt.legend(loc=2)
plt.title("Moments of Inertia")
plt.xlabel("Triangle Side Length (a)")
plt.ylabel("Inertia")
plt.show()
