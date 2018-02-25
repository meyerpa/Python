# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 07:02:04 2017

@author: Paige Meyer
@date="03/12/2017"
@version= 1.0
PHYS 350 - Computational Physics
Homework 08
Description: Finds L1 Lagrange point of a satillite obiting the Earth. 
    As written, it returns something similar to solving in Wolfram Alpha.
    Link is below.
    https://www.wolframalpha.com/input/?i=solve++((6.674e-11*5.974e24)%2F(r%5E2))
    +-+(6.674*10%5E-11*7.348*10%5E22+%2F+(3.884*10%5E8+-+r)%5E2)+-+(2.662*10%5E-6)
    %5E2*r++%3D+0++for+r​
"""

import numpy as np


def lagrange(r, R = 3.844e8, G = 6.674e-11, M = 5.974e24, m = 7.348e22, omega = 2.662e-6):
    """ Lagrange Formula, root finding
    
    parameters
    ----------
    r: float
        radius of the satellite
    R: float, optional
        radius of massive object orbiting centroid. Defaulted to moon's
        radius around Earth.
    G: float, optional
        force of gravity. Defaulted to 6.674 * 10^-11.
    M: float, optional
        Mass of centroid. Defaulted to Earth's mass.
    m: float, optional
        Mass of massiving orbiting object. Defaulted to moon's mass.
    omega: float, optional
        Angular velocity of both the massive orbiting object and the satillite.
        Defaulted to Moon's angular velocity.
    """
    # ensure no divide by zero
    assert(r > 10e-6)
    assert(np.abs(r-R) > 10e-6)
    
    # solve for 0
    return ((G*M / r**2) - (G*m / (R-r)**2)) - omega**2*r


def secant_solver(f, x0, x1, tol=1e-15, n_max=100, n=1):
    """Returns numerical approximation for finding the root of f within a tolerance
    
    parameters
    ----------
    f : function pointer
        The function of which wanting to find the root
    x0: float
        initial guess
    x1: float
        second guess
    tol: float
        tolerance to which would like to acheive
    n_max: integer
        the maximum number of times to use this method
    n: integer, optional
        number which called this method
        
    returns
    -------
    n: integer
        number of times secant method was used
    x: float
        approximation for root
    delta: float
        difference between this estimate and the last (practical error bound)
    
    """
    f0 = f(x0)
    f1 = f(x1)
    
    # ensure will not have divide by zero error
    if np.abs(f1-f0) < 10e-12:
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


# Exercise 6.16 - The Lagrange Point

M = 5.974e24            # Earth's mass
m = 7.348e22            # Moon's mass
G = 6.674e-11           # Force of gravity
R = 3.844e8             # Moon radius around Earth
omega = 2.662e-6        # angular velocity of Moon and Satillite


# Note, we are assuming the orbits are circular
# and the Earth is much more massive than the moon 
# and satillite,  so can use Kepler's Laws.
# Thus, the lagrange function applies, and can solve for one
# of the roots using the secant method, as shown below


# Secant Method
epsilon = 10e-6           # tolerance
r = R/4                   # Initial Satellite radius around Earth
max_times = 1000          # Maximum times to loop
# call the secant function to solve
ans = secant_solver(lagrange, r, r/2, epsilon, max_times)
# print solution
print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
    + "with difference {0:.6f} ".format(ans[2]))
