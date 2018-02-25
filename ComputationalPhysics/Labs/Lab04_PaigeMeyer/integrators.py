# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:08:47 2017
@file: integrators.py
@author: Paige Meyer
@date: 1-30-2016
@version: 1.4
Description: This file contains functions for approximating integrals:
    for example the trapezoidal rule, Simpson's Rule, Adaptive Integrator,
    and adaptive quadrature.
"""


def trapezoidal_rule(integrand, a=0, b=1, N=10):
    """Approximates integration by using the trapezoidal rule

    Returns the approximate area under the curve based on
    the trapezoidal rule approximation

    Parameters
    ----------
    a : double, float, or integer, optional
        interval lower boundary default is 0
    b : double, float, or integer, optional
        interval upper boundary default is 1
    integrand : function pointer
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
    >>> trapezoidal_rule(f, 0, 1)
    0.3350000000000001
    >>> trapezoidal_rule(f, 0, 1, 100000)
    0.3333333333499996

    """
    # Ensure arguments are valid
    assert(b > a)
    assert(N > 0)

    h = (b-a)/N

    s = 0.5*integrand(a) + 0.5*integrand(b)
    for k in range(1, N):
        s += integrand(a+k*h)

    return h*s


def simpsons_rule(integrand, a=0, b=1, N=10):
    """Approximates integration by using Simpson's rule

    Returns the approximate area under the curve based on
    Simpson's Rule approximation

    Parameters
    ----------
    integrand : function pointer
        function to integrate. Assumes that this function takes one argument,
        the x-coordinate and returns the value of the function at a point
    a : double, float, or integer
        interval lower boundary
    b : double, float, or integer
        interval upper boundary
    N : integer, optional
        number of intervals to use for integration, default is 10

    Returns
    -------
    integral: float
        The approximate value for the area under the curve
        as approximated by Simpson's rule

    Examples
    --------
    >>> simpsons_rule(f, 0, 2)
    2.6666666666666665
    >>> simpsons_rule(f, 0, 2, 100)
    2.666666666666667

    """
    # Ensure arguments are valid
    assert(b > a)
    assert(N > 0)
    assert(N % 2 == 0)

    h = (b-a)/N

    s = integrand(a) + integrand(b)
    for k in range(1, N, 2):
        s += 4*integrand(a+k*h)
    for k in range(2, N, 2):
        s += 2*integrand(a+k*h)

    return (1/3)*h*s


def adaptive_integrator(funct, a=0, b=1, tolerance=1e-4, N=10):
    """ Changes the number of intevals until the integral is within tolerance.

    Increment until the integral is within
    tolerance using Simpson's rule of two integrals to find the actual
    error bound.

    Parameters
    ----------
    funct : function pointer
        function to integrate. Assumes that this function takes one argument,
        the x-coordinate and returns the value of the function at a point
    a : double, float, or integer
        interval lower boundary
    b : double, float, or integer
        interval upper boundary
    N : integer, optional
        number of segments to use for Simpson's Rule, default is ten.
    tolerance : float, optional
        the practical error bound

    Returns
    -------
    approximation : float
        The approximate value for the area under the curve
        as approximated by repeatively applying
        Simpson's Rule with an increasing number of intervals.

    Examples
    --------
    >>> def f(x):
            return 4 * (x**3) -2
    >>> adaptive_integrator(f)
    -1.0000000000000004
    >>> adaptive_integrator(f, 0, 3)
    75.0

    """
    first = simpsons_rule(funct, a, b, N)
    second = simpsons_rule(funct, a, b, N+2)
    while abs(first - second) >= tolerance:
        first = second
        N += 2
        second = simpsons_rule(funct, a, b, N+2)
    return second


def adaptive_quadrature(function, a=0, b=1, tolerance=1e-4,  N=4, level=1):
    """ Adaptive Quadrature based on Simpson's Rule Approximation

    This function takes approximates the definite integral of a
    function, starting at a and ending at b. This adaptive
    integration is based on Simpson's Rule for approximating
    integrals. It takes the entire range, and approximates
    the integral. From that it takes the left and right halves
    of the range and approximates those integrals as well.
    Then, it compares the sum of the approximations, and sees
    if the sum is within the tolerance provided, saying it is a
    "good enough" approximation. If it is not, it recurses with
    the left and right hand sides until it uses use a range
    with small enough error.

    Parameters
    ----------
    function : function pointer
        function to integrate. Assumes that this function takes one argument,
        the x-coordinate and returns the value of the function at a point
    a : double, float, or integer
        interval lower boundary
    b : double, float, or integer
        interval upper boundary
    N : integer, optional
        number of segments to use for Simpson's Rule, default is four
    tolerance : float, optional
        the tolerance of error to allow between left + right
        and total approximation
    level : the number of recursions needed to find the approximation

    Returns
    -------
    approximation : float
        The approximate value for the area under the curve
        as approximated by Adaptive Quadrature (repeatively applying
        Simpson's Rule)

    Examples
    --------
    >>> def f(x):
            return 4 * (x**3) -2
    >>> adaptive_quadrature(f)
    -1.0000000000000162
    >>> adaptive_quadrature(f, 0, 3)
    74.99999999999969

    """
    print("a"+str(a))
    print("b"+str(b))
    Sab = simpsons_rule(a, b, function, N)
    Sa = simpsons_rule(a, (a+b)/2, function, N)
    Sb = simpsons_rule((a+b)/2, b, function, N)
    if abs(Sab - Sa - Sb) < 15 * tolerance:
        return Sab
    else:
        # return sum of integration of two halves
        return adaptive_quadrature(function, a, (a+b)/2, tolerance/2, N, level+1) + \
                       adaptive_quadrature(function, (a+b)/2, b, tolerance/2, N, level+1)
