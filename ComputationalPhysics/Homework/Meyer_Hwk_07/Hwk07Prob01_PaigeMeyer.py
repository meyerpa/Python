# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:05:29 2017

@author: Paige Meyer
@date="02/25/2017"
@version= 1.0
PHYS 350 - Computational Physics
Homework 07
Description: 

"""

import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt


def Normalize(x):
    """Returns the normalized x vector

    Parameters
    ----------
    s : numpy array
        Holds each point in the vector

    Returns
    -------
    s : numpy array
        Holds each normalized point in the vector, total length is one
    """
    return x / np.sqrt(np.dot(np.conjugate(x), x))


def Psi(valH, vectH, PsiInitial, t):
    """Return the wave funcction at a certain time t

    Parameters
    ----------
    valH : numpy array
        Array of eigenvalues
    vectH : numpy array
        Array of eigenvectors
    PsiInitial : numpy array
        Normalized initial wavefunction
    t : float, optional
        time to evaluate the wavefunction

    Returns
    -------
    PsiFinal : float
        Energy at any time t for this system
    """
    PsiValue0 = np.dot(np.conjugate(vectH[:,0]), PsiInitial) * np.exp(-1j * valH[0] * t) * vectH[:,0]
    PsiValue1 = np.dot(np.conjugate(vectH[:,1]), PsiInitial) * np.exp(-1j * valH[1] * t) * vectH[:,1]
    return PsiValue0 + PsiValue1
    
# time = 100                 # number of times to loop
# x = np.array([1, 1j])
# x = Normalize(x)

# psiInit = np.array([1, 0])      # Initial molecule state
# Hamiltonian Matrix (determines molecular states change with time)
C = np.array([[0, -1j],
              [1j, 0]])  

vals, vect = eig(C)
print("vals", vals)
print("Eigenvector:", Normalize(vect[0,:]))
print("Eigenvector7:", Normalize(vect[1,:]))
