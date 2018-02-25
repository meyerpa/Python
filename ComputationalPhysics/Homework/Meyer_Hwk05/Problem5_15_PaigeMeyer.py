# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:32:34 2017

@author: Paige Meyer
@date="02/08/2017"
@version= 1.0
PHYS 350 - Computational Physics
Homework 5
Description: f(x) = 1 + (1/2) * tanh(2x)
    f'(x) is defined as a function, and a central difference is taken
    to approximate the derivative. This is shown from x ranging from -2
    to 2 graphically.
"""

# Note: Derived 1 + (1/2) * tanh(2x)


import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 + 0.5 * np.tanh(2*x)


def fPrime(x):
    """Derivative of f(x)

    This formula was derived using Wolfram Alpha. I typed in
        "derivative of 1+ (1/2)*tanh(2*x)".
    Which showed the derivative to be sech^2(2x), and this is
    equivalent to (1/cosh(2x))^2.
    """
    return (1/np.cosh(2*x))**2


def derivative_central(x, y):
    """Approximate first derivative using the central difference technique

    Parameters
    ----------
    x : numpy array
        The x-value of the function
    y : numpy array
        The y-values cooresponding to the x-values at the function

    Returns
    -------
    dy/dx : numpy array
        The approximation of the derivative in an N-2 dimensional
        numpy array

    """
    dy = y[2:]-y[:-2]
    dx = (x[2:]-x[:-2])
    return dy / dx

a = -2
b = 2
h = 0.1

x = np.arange(a, b, h)              # array of x-values
y = f(x)                            # array of y-values
yPrime = fPrime(x)                  # array of y'-values
dydx = derivative_central(x, y)     # array of central difference y-values

# Add plotting commands
plt.plot(x, y, 'r-', label="y(x) = 1 + 1/2 * tanh(x)")
plt.plot(x, yPrime, "m--", label="y\'(x)")
plt.plot(x[:-2], dydx, 'bo', alpha=.5, label="dy/dx")

# formal plot
plt.legend()
plt.title("Derivatives")
plt.xlabel("x")
plt.ylabel("y(x), dy/dx, and y\'\'(x)")
plt.show()
