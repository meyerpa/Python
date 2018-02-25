# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 00:24:42 2017

@author: Paige Meyer
@date="02/25/2017"
@version= 1.0
PHYS 350 - Computational Physics
Homework 07
Description: The Relaxation Method for multiple values.
    
    When c = 2, the result is approximately 0.796812

"""

import numpy as np
import matplotlib.pyplot as plt


def func(x, c=2):
    # the function given to solve on the homework
    return 1 - np.exp(-c*x)



def solve(initialGuess, function, epsilon=10**-6, c=2):
    """ Returns Relaxation Method Result for Function
    
    parameters
    ----------
    initialGuess: int, float, double
        The initial guess for the solution
    
    epsilon: int, float, double, optional
        The allowable difference to the actual solution. The default
        is 10^-6.
    c: int, float, double, optional
        The value for the extra function parameter. In this case e^-ct
    returns
    -------
    approximation: float
        The resulting approximation for the values which put into the
        function returns itself.
    """
    lessThanEpsilson = False  # seeing if it is less than allowable difference
    xprev = initialGuess
    
    # Relaxation Method
    while not lessThanEpsilson:
        xnew = function(xprev, c)
        # print("Previous:", xprev, "New:", xnew, "Difference: {:.7f}".format(np.abs(xnew-xprev)))
        lessThanEpsilson = np.abs(xnew - xprev) < epsilon
        xprev = xnew
    return xnew

# constants
initial_guess = 1           # starting guess
step = 0.01                 # steps for c
start = 0                   # c starting value
stop = 3                    # c ending value

# calculated variables
num_times = int(np.ceil(np.abs(stop-start)/step)) + 1
solutions = np.empty(num_times, dtype=float)
c_values = np.linspace(start, stop, num_times)

# calculate solution for each c value
for i in range(num_times):
    c = c_values[i]
    solutions[i] = solve(initial_guess, func, 10**-6, c)

# plot c value and solutions
plt.plot(c_values, solutions, label="Approximated Solutions")
plt.legend(loc=2)
plt.title("Relaxation Method 1 - e^-ct")
plt.xlabel("c values")
plt.ylabel("Values")
plt.show()
