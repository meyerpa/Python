# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 09:45:38 2017

@author: Paige Meyer
__author__="Paige Meyer"
__date__="01/25/2017"
__version__= 1.1
PHYS 350 - Computational Physics
Lab 3
Description: This package contains functions for randomizing a step,
randomizing a three-dimensional walk,
creating a random walk, and finding the distance to a point.
"""

import numpy as np
from random import random


def coord(step_size):
    """Return positive or negative step 50 percent chance each


    Randomly returns either a negative step 50% of the time
    or a positive step the other 50% of the time.

    Parameters
    ----------
    step_size : double, float, or integer
        The step size

    Returns
    -------
    random_step: double float, or integer
        Positive(50% chance) or negative(50% chance) step.

    Notes
    -----
    Relies on Random.random()

    Examples
    --------
    >>> coord(1)
    1
    >>> coord(1)
    -1
    >>> coord(.5)
    -0.5

    """
    # return negative 1/2 time
    if random() < 0.5:
        return -1*step_size
    # return positve the other 1/2 time
    else:
        return step_size


def coord3D(step_size):
    """Return positive or negative step 50 percent chance each


    Randomly returns a numpy 1x3 array

    Parameters
    ----------
    step : double, float, or integer
        The step size

    Returns
    -------
    random_steps: numpy array containing three floats
        Contains three variables containing three random steps
        (positive or negative step sizes)

    Notes
    -----
    Relies on coord(step)

    Examples
    --------
    >>> coord3D(1)
    array([-1,  1,  1])
    >>> coord3D(1)
    array([ 1, -1, -1])
    >>> coord3D(.5)
    array([ 0.5,  0.5,  0.5])
    >>> coord3D(.5)
    array([ 0.5,  -0.5,  0.5])

    """
    # use the coord function to get multiple random steps
    dx = coord(step_size)       # x step
    dy = coord(step_size)       # y step
    dz = coord(step_size)       # z step
    random_steps = np.array([dx, dy, dz])
    return random_steps


def make_walk(number_steps=1, step_size=1, start_x=0.0, start_y=0.0,
              start_z=0.0):
    """Creates random walk with in x and y with step_size

    Returns one number_steps rows by 3 column numpy array
    containting floats for x positions, y positions, and
    z positions in the first second and third columns
    respectively. and the other for the y-coordinate with
    random walks. Each walk consists of steps filling
    the numpy arrays with updated coordinates, stepping by
    step_size each time. Defaulted to start at (0, 0, 0), but
    can be changed through parameters.

    Parameters
    ----------
    number_steps : int
        The number of steps the walker should take
    step_size : int, float, or double
        Indicates the size of the step for the walk
    start_x : float or double
        Starting x-value of the walk
    start_y : float or double
        Starting y-value of the walk
    start_z : float or double
        Starting y-value of the walk

    Returns
    -------
    pos : numpy array
        Array containing each step's position in the
        x, y, and z

    Notes
    -----
    Asserts that the the number of steps is 1 or more.

    Examples
    --------
    >>> make_walk(3)
    array([[ 0.,  0.,  0.],
       [-1., -1., -1.],
       [-2.,  0., -2.]])
    >>> make_walk(3)
    array([[ 0.,  0.,  0.],
       [-1., -1.,  1.],
       [-2., -2.,  0.]])
    >>> make_walk(3, 0.5, start_x=5, start_y =1, start_z =4)
    array([[ 5. ,  1. ,  4. ],
       [ 4.5,  0.5,  3.5],
       [ 4. ,  1. ,  3. ]])

    """

    # ensure will not run into index error
    assert(number_steps > 0)

    positions = np.empty([number_steps, 3])
    positions[0, :] = [start_x, start_y, start_z]

    # loop through each value stepping forward by step_size
    # or backward 50% of the time and write to the arrays.
    for i in range(1, number_steps):
        dr = coord3D(step_size)     # random step in x, y and z
        positions[i, :] = positions[i-1, :] + dr   # append with new position
    return positions


def mag(positions, x=0.0, y=0.0, z=0.0):
    """Returns array's distance from x and y positions

    Returns array showing distance for each value in array from
    x_pos and y_pos.

    Parameters
    ----------
    positions: numpy array
        Numpy array storing values of each x, y, and z position in
        the first second and third column respectively.
    x: float, double, optional
        The x-position of the coordinate wanting to get distance from.
        (The default is 0.0, which implies the distance from x = 0.0).
    y: float, double, optional
        The x-position of the coordinate wanting to get distance from.
        (The default is 0.0, which implies the distance from y = 0.0).
    z: float, double, optional
        The x-position of the coordinate wanting to get distance from.
        (The default is 0.0, which implies the distance from z = 0.0).

    Returns
    -------
    distance: numpy array
        Array containing distances from (x,y).

    Raises
    ------
    None

    See Also
    --------
    scipy.spatial.distance.pdist
    scipy.spatial.distance.cdist
    scipy.spatial.distance.squareform

    Examples
    --------
    >>> values = np.array([[ 0.,  0.,  0.],
       [ 1., -1., -1.],
       [ 0.,  0., -2.],
       [ 1.,  1., -1.],
       [ 2.,  2., -2.]])
    >>> mag(values)
    array([ 0.        ,  1.73205081,  2.        ,  1.73205081,  3.46410162])

    >>> # Get distance from (0, 0, 7)
    >>> pos = np.array([[ 0.,  0.,  0.],
       [-1., -1.,  1.],
       [ 0., -2.,  0.],
       [ 1., -1.,  1.]])
    >>> mag(x, 0, 0, 7)
    array([ 7.        ,  6.164414  ,  7.28010989,  6.164414)

    """
    x_pos = positions[:, 0]
    y_pos = positions[:, 1]
    z_pos = positions[:, 2]
    distance = np.sqrt((x_pos-x)**2 + (y_pos-y)**2+(z_pos-z)**2)
    return distance
