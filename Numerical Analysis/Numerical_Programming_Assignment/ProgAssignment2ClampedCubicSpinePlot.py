#plotting
import numpy as np
import matplotlib.pyplot as plt
from math import log

def fun(x):
    if x <= 1.0:
        return 0.0 + 0.906512635361 (x-1.0) + 0.0 (x-1.0)**2 + -0.391197762054 (x-1.0)**3
    elif x < 1.67:
        0.287682072452 + 0.776113381343 (x-1.33333333333) + -0.391197762054 (x-1.33333333333)**2 + 0.213448739556 (x-1.33333333333)**3
    else:
        0.510825623766 + 0.586464453159 (x-1.66666666667) + -0.177749022498 (x-1.66666666667)**2 + 0.177749022498 (x-1.66666666667)**3

x = np.arange(0.1, 2, 0.000001);
vfun = np.vectorize(fun)
y = vfun(x)
# set axis labels
ax = plt.gca() 
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
plt.title('Clamped Cubic Spine for ln(x)')
plt.plot(x, map(fun,x), linewidth="2", color="red")
plt.show()
