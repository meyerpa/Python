# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:35:49 2017

@author: Paige Meyer

Code for finding intial vertical velocity 
needed to toss a ball to a height of 30 
meters in 3 seconds.
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def func(x, t):
    # Returns the derivative. This is dr/dt = (y, x)
    return np.array([x[1], -9.8])


def diff(v0):
    """Retuns the difference between target height xf 
    and and the actual height acheived for initial velocity v0. 
    
    Note: times should define an array of times called times,
    and a function that gives the derivative called func.  
    """
    xf = 30         # final height
    xa = [0, v0]
    x = rk4(func, xa, times)
    return x[-1, 0] - xf


def secant_solver(f, x0, x1, tol=1e-15, n_max=100, n=1):
    """Finds root (0) of function 0 with initial 
    """
    f0 = f(x0)
    f1 = f(x1)
    # ensure will not have divide by zero error
    if np.abs(f1-f0) < tol:
        delta = np.abs(x1 - x0)             # difference
        return (n, x1, delta)
    
    # compute new x
    x = x1 - f1*(x1 - x0) / (f1 - f0)
    delta = np.abs(x - x1)                  # difference
    
    # if new x is within tolerence, return otherwise do again
    if delta < tol or n > n_max:
        return (n, x, delta)
    else:
        return secant_solver(f, x1, x, tol, n_max, n+1)

    
def rk4(f, x0, t):
    # Pass in the function for dx/dt, the initial value, x0, and an array
    # of times and return an array of x values for those times.
    x = x0        # track the current value of x
    xlist = x  # Create an array of x values at all times
    lasttime = t[0]

    for time in t[1:]:
        # This loop needs to compute h based on time and lasttime
        # (since it isn't automatically "known" to the euler function)
        h = time - lasttime
        k1 = h * f(x, lasttime)
        k2 = h * f(x + (k1/2), lasttime + (h/2))
        k3 = h * f(x + (k2/2), lasttime + (h/2))
        k4 = h * f(x + k3, lasttime + h)
        x = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

        # Add x to the xlist array.  To do this, we have to over-write the
        # xlist array using vstack (which stacks the arrays in 'rows' or
        # vertical stacks).  Since x is a scalar, we have to
        # convert it into an array first, and then 'stack' it.
        xlist = np.vstack((xlist, x))

        # Update the lasttime variable so it is ready for the next loop.
        lasttime = time

    return xlist

# Set up limits and step number
a = 0.0              # start time
b = 3.0              # end time
N = 1000             # steps
h = (b - a) / N      # step size

# print final height
print("Final height", rk[-1, 0])

# Find final answer using secant solver
(n, x, diff) = secant_solver(diff, 15, 20, tol=1e-4, n_max=20)
print("Used Secant solver {:} times to find initial velocity {:.5f}\
 with error {:.5f}".format(n, x, diff))

# initial conditions
x0 = np.array([0., x])    # x(a) =initial height, initial velocity.
times = np.arange(a, b, h)
rk = rk4(func, x0, times)

# plotting commands
plt.plot(times, rk[:, 0])
plt.grid()
plt.title("Rk4")
plt.show()
