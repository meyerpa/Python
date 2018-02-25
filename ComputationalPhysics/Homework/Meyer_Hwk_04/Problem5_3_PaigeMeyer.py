# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:55:27 2017

@author: Paige Meyer
__author__="Paige Meyer"
__date__="02/02/2017"
__version__= 1.0
PHYS 350 - Computational Physics
Homework 4
Description: This assignment uses the trapezoid rule to
    approximate the value of the error function integral.
    It is based off of a different version of Newmann
    Exercise 5.3
"""

from math import exp
from integrators import trapezoidal_rule


def integrand(t=1):
    """This function returns e^(t^2)

    Parameters
    ----------
    t : integer, float, double, optional
        Variable use in the function.

    Returns
    -------
    e : integer, float, double
        e^(t^2)
    """
    return exp(t**2)


def E(b, step=.1):
    """Approximates the integral e^(t^2) from 0 to b, with step sizes provided.

    Parameters
    ----------
    b : integer, float, double
        The ending point of the interval
    step: integer, float, double
        The size of each subinterval

    Returns
    -------
    num : float, double
        The number approximating the integral
    """
    a = 0
    n = int((b-a)/step)
    return trapezoidal_rule(integrand, a, b, n)


print(E(3))
