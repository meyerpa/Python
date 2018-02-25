# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:07:39 2017

@author: Paige Meyer
@date="02/08/2017"
@version= 1.0
PHYS 350 - Computational Physics
Lab 5
Description: Calculates actual first and second derivatives of cosine.
    Then it calculates the forward and central differences of the cosine
    function. From that, it uses the central difference estimate to
    estimate the second difference. It also uses the second difference
    formula to estimate the second derivative.
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """Returns the cosine of x

    Parameters
    ----------
    x : numpy array
        Contains x-values in array that want sin(x) to be determined

    Returns
    -------
    y : numpy array
        Contains the y-values corresponding to sin(x)
    """
    return np.cos(x)


def fprime(x):
    """Returns the negative sine of x

    Parameters
    ----------
    x : numpy array
        Contains x-values in array to apply the function to.

    Returns
    -------
    y : numpy array
        Contains the y-values corresponding to negative sin(x)
    """
    return -np.sin(x)


def fDoublePrime(x):
    """Returns the negative cosine of x

    Parameters
    ----------
    x : numpy array
        Contains x-values in array to apply the function to.

    Returns
    -------
    y : numpy array
        Contains the y-values corresponding to negative cos(x)
    """
    return -np.cos(x)


def derivative(x, y):
    """Approximate first derivative using the forward difference technique

    Parameters
    ----------
    x : numpy array
        The x-value of the function
    y : numpy array
        The y-values cooresponding to the x-values at the function

    Returns
    -------
    dy/dx : numpy array
        The approximation of the derivative in an N-1 dimensional
        numpy array
    """
    # x : np array
    # y : np array
    # Compute forward difference estimate for the derivative for array of N
    # points and values of the function at those points.  The two 1-D arrays
    # must be the same size.
    dy = y[1:] - y[:-1]             # compute y[i+1] - y[i] difference
    dx = x[1:]-x[:-1]               # compute x[i+1] - x[i] difference
    return dy / dx


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


def derivative_second_central(x, y):
    """Approximate second derivative.

    Uses the central difference technique twice to estimate second derivative

    Parameters
    ----------
    x : numpy array
        The x-value of the function
    y : numpy array
        The y-values cooresponding to the x-values at the function

    Returns
    -------
    dy/dx : numpy array
        The approximation of the second derivative in an
        N-4 dimensional numpy array
    """
    yPrime = derivative_central(x, y)
    yDoublePrime = derivative_central(x[1:N-1], yPrime)
    return yDoublePrime


def derivative_second(x, y):
    """Approximate second derivative.

    Parameters
    ----------
    x : numpy array
        The x-value of the function
    y : numpy array
        The y-values cooresponding to the x-values at the function

    Returns
    -------
    d2y/dx2 : numpy array
        The approximation of the second derivative in an
        N-2 dimensional numpy array
    """
    d2y = y[2:] - 2 * y[1:N-1] + y[:N-2]
    dx2 = (x[2:] - x[1:N-1])**2
    return d2y / dx2


# Set the step size based on limits
a = 0
b = 4 * np.pi
N = 100
h = (b - a) / N

# get arrays for x, y, y', and  dy/dx
x = np.arange(a, b, h)
y = f(x)          # Since we are using numpy, this will compute as array
yPrime = fprime(x)
yForward = derivative(x, y)         # yForward will have N-1 elements
yCentral = derivative_central(x, y)  # yCentral will have N-2 elements

# Add plotting commands
plt.plot(x[0:N - 1], y[0:N - 1], 'r-', label="y(x) = cos(x)")
plt.plot(x, yPrime, color="m", label="y\'(x)")
plt.plot(x[0:N - 1], yForward, 'b*', alpha=.5, label="forward dy/dx")
plt.plot(x[1:N - 1], yCentral, 'ko', alpha=.5, label="central dy/dx")

# format plot
plt.legend()
plt.title("Forward, Central, and Actual Derviative")
plt.xlabel("x")
plt.ylabel("y(x), dy/dx, y\'(x)")
plt.show()

# print error estimates for first derivatives
print("Foward Difference Estimation Error", end=" ")
print(np.sum(np.abs(yPrime[0:N-1] - yForward)))
print("Central Difference Estimation Error", end=" ")
print(np.sum(np.abs(yPrime[1:N-1] - yCentral)))
'''
Activity 2 part 3
------------------------------------
With a = 0, b = 4 * np.pi, and N = 10, central difference is more accurate.
    Forward error: 3.4030 and
    Central Error 1.2655 (approximately).
With N = 100 central difference is still more accurate,
    Forward Error: 3.9348
    Central Error: 0.1669

'''

# Second Derivatives
yDoublePrime = fDoublePrime(x)
yDoubleForm = derivative_second(x, y)  # yDoubleForm has N-2 elements
yDoubleCent = derivative_second_central(x, y)  # yDoubleCent has N-4 elements

# Add plotting commands
plt.plot(x[:N - 1], y[:N - 1], 'r-', label="y(x) = cos(x)")
plt.plot(x, yDoublePrime, color="m", label="y\'\'(x)")
plt.plot(x[:N - 2], yDoubleForm, 'b*', alpha=.5, label="approximate d2y/dx2")
plt.plot(x[1:N - 3], yDoubleCent, 'ko', alpha=.5, label="central d2y/dx2")

# formal plot
plt.legend()
plt.title("Second Derivatives")
plt.xlabel("x")
plt.ylabel("y(x), d2y/dx2, y\'\'(x)")
plt.show()
