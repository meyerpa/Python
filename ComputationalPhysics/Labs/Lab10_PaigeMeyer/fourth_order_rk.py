# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:10:46 2017

@author: Paige Meyer
Description: This file contains a function to find the 
fourth-order runge-kutta derivative approximation.
"""


import numpy as np


def rk4(f, x0, t):
    """Returns Fourth Order Runge-Kutta Appoximation for derivative
    
    parameters
    ----------
    f : function pointer
        The pointer to the derivative
    x0 : numpy array
        initial condition
    t : numpy array
        Times would like to evaluate at. Assumes equal spacing.
        
    returns
    -------
    xlist: numpy array
        Fourth Order Runge-Kutta numerical approximation for derivative.
    """
    # Pass in the function for dx/dt, the initial value, x0, and an array
    # of times and return an array of x values for those times.
    x = x0        # track the current value of x
    xlist = x  # Create an array of x values at all times
    lasttime = t[0]

    for time in t[1:]:
        # step
        h = time - lasttime
        
        # values to sum later
        k1 = h * f(x, lasttime)
        k2 = h * f(x + (k1/2), lasttime + (h/2))
        k3 = h * f(x + (k2/2), lasttime + (h/2))
        k4 = h * f(x + k3, lasttime + h)
        
        # calculate next value using runge-kutta order 4 method
        x = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

        # Add x to the xlist array.  To do this, we have to over-write the
        # xlist array using vstack (which stacks the arrays in 'rows' or
        # vertical stacks).  Since x is a scalar, we have to
        # convert it into an array first, and then 'stack' it.
        xlist = np.vstack((xlist, x))

        # Update the lasttime variable so it is ready for the next loop.
        lasttime = time

    return xlist
