# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:22:12 2017

@author: Paige Meyer
@date="02/06/2017"
@version= 1.4
PHYS 350 - Computational Physics
Lab 4
Description: This lab finds actual values of an integral, and approximates the
    values as well. One of the functions is the Stefan Boltzmann function.
"""


from integrators import simpsons_rule, trapezoidal_rule, adaptive_integrator
from math import exp, pi


def test_function(x):
    """Finds value of function f(x) = 4x^3 -2

    Parameters
    ----------
    x : integer, float, double, optional
        The x value of the integrand, defaulted to zero.

    Returns
    -------
    value : float
        The value of the function at the certain x value.

    """
    return 4*(x**3) - 2


def integral_of_test_function(a, b):
    """Returns integral value from a to b of  4x^3 -2: b^4 - a^4 - 2b + 2a

    Parameters
    ----------
    a : integer, float, double
        The start of the interval
    b : integer, float, double
        The end of the interval

    Returns
    -------
    value : float
        b^4 - a^4 - 2b + 2a

    """
    assert(a < b)       # ensure a is the interval start

    return (b)**4 - (a)**4 - 2*(b-a)


def boltzmann_integrand(x=0):
    """Return's value of function f(x) = x^3 / (e^x - 1)

    Parameters
    ----------
    x : integer, float, double, optional
        The x value of the integrand, defaulted to zero.

    Returns
    -------
    value : float
        The value of the boltzmann integrand at the certain x value.
    """
    # Sam's idea: find undefined value at x=0
    # by taking limit when x=0 using L'hopital's Rule
    # which resulting in y=0 as x->0
    if x == 0:
        return 0
    else:
        return x**3 / (exp(x)-1)


def boltzmann(x=0):
    """Returns value of the boltzmann integral--4pi / 15

    Parameters
    ----------
    x : integer, float, double, optional
        This parameter doesn't affect the return value, but is useful
        if the programmer forgot that the boltmann function doesn't
        need a parameter

    Returns
    -------
    value : float
        The value of the boltmann integral--4 pi / 15

    """
    return pi**4 / 15


a = -1.
b = 2.
n = 10

print("Finding the integral of 4x^3 -2...")
print("On {} to {} with {} subintervals.".format(a, b, n))

# actual value
actual = integral_of_test_function(a, b)
print("Actual value", actual)

# trapezoidal rule
trap = trapezoidal_rule(test_function, a, b, n)
print("Trapezoidal rule", trap)
print("Trapezoid Rule Error", abs(trap-actual))

# Simpson's rule
simp = simpsons_rule(test_function, a, b, n)
print("Simpson's Rule", simp)
print("Simpson's Rule Error", abs(simp-actual))


""" Part 3:
    For the same n, simpson is more accurate with a =-1, and b =2
            Trapezoid           Simpson
    n=1:       27               15
    n=5:       1.08             3.16
    n=10:      .270             5.33 * 10^-15
    n=100:     .00270           5.33*10^-15

"""


a = 0
b = 60
N = 100000

print("\nFinding the Stefan Boltzmann Function...")
print("On {} to {} with {} subintervals.".format(a, b, N))

# actual values
actual = boltzmann()
print("Actual value", actual)

# trapezoidal rule
trap = trapezoidal_rule(boltzmann_integrand, a, b, N)
print("Trapezoid value", trap)
print("Trapezoid Rule Error", abs(trap-actual))

# simpson's rule
simp = simpsons_rule(boltzmann_integrand, a, b, N)
print("Simpson's Rule", simp)
print("Simpson's Rule Error", abs(simp-actual))

"""
Part 4
------
Note: I figured over 10 decimal places of precision of
should be precise enough because if we multiple N
by 10, it doesn't give a more accurate answer.
Also, using a smaller a (divided by a 10), doesn't
result in a more precise answer. Finally, regarding b
if b is doubled, the answer become less accurate as
well since N stays relatively the same.
"""

# adaptive integrator
adap = adaptive_integrator(boltzmann_integrand, a, b)
print("Adaptive Integrator", adap)
print("Adaptive Integrator Error", abs(adap-actual))
