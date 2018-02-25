# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:08:47 2017
@file: integrators.py
@author: Paige Meyer
@date: 1-30-2016

"""


def trapezoidal_rule(a, b, f, N=10):
    """Approximates integration by using the trapezoidal rule

    Returns the approximate area under the curve based on
    the trapezoidal rule approximation

    Parameters
    ----------
    a : double, float, or integer
        interval start

    b : double, float, or integer
        interval end
    f : function pointer
        function to integrate. Assumes that this function takes one argument,
        the x-coordinate and returns the value of the function at a point
    N : integer, optional
        number of intervals to use for integration, default is 10

    Returns
    -------
    integral: float
        The approximate value for the area under the curve
        as approximated by the trapezoid rule

    Examples
    --------
    >>> def f(x):
            return x**2
    >>> trapezoidal_rule(0,1,f)
    0.3350000000000001
    >>> trapezoidal_rule(0, 1, f, 100000)
    0.3333333333499996

    """
    # Ensure arguments are valid
    assert(b > a)
    assert(N > 0)

    h = (b-a)/N

    s = 0.5*f(a) + 0.5*f(b)
    for k in range(1, N):
        s += f(a+k*h)

    return h*s


def simpson_rule(a, b, f, N=10):
    """Approximates integration by using Simpson's rule

    Returns the approximate area under the curve based on
    Simpson's Rule approximation

    Parameters
    ----------
    a : double, float, or integer
        interval start

    b : double, float, or integer
        interval end
    f : function pointer
        function to integrate. Assumes that this function takes one argument,
        the x-coordinate and returns the value of the function at a point
    N : integer, optional
        number of intervals to use for integration, default is 10

    Returns
    -------
    integral: float
        The approximate value for the area under the curve
        as approximated by Simpson's rule

    Examples
    --------
    >>> simpson_rule(0,2,f)
    2.6666666666666665
    >>> simpson_rule(0,2,f, 100)
    2.666666666666667

    """
    # Ensure arguments are valid
    assert(b > a)
    assert(N > 0)

    h = (b-a)/N

    s = f(a) + f(b)
    for k in range(1, N):
        if k % 2 == 1:
            s += 4*f(a+k*h)
        else:
            s += 2*f(a+k*h)

    return (1/3)*h*s
