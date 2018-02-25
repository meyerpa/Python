# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:07:06 2017

@author: Paige
"""

import matplotlib as plt
import numpy as np


x = np.linspace(-10, 10, 400)
cos = np.cos(x)
sin = np.sin(x)
plt.plot(x, cos, "r", label="cos(x)")        # r for red line
plt.plot(x, sin, "b--", label="sin(x)")      # b-- for blue dashed line
# colors include red(r), green(g), yellow(y), blue(b), cyan(c),
# magenta(m), black(k), white(w)
# line styles include solid line("-"), dashed line("--"),
# solid line("-"), square("s"), dots("o"), smaller dots(".")
plt.xlim(-10, 10)
plt.legend()
plt.xlabel("x")
plt.title("Trigonometric Functions")
plt.ylabel("cos(x) or sin(x)")
# plt.savefig("1-23-2017.png")
plt.show()
