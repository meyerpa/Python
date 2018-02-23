#plotting
import numpy as np
import matplotlib.pyplot as plt
from math import log

def fun(x):
    return 0 + 0.714285714285714*(x-1) +  0.317237193168295*(x-1)**2 +  -1.58618596584148*(x-1)**3 + 2.14247946387946*(x-1)**4 + -2.74820175568131*(x-1)**5
print(fun(1.5))
x = np.arange(0.1, 2, 0.000001);
vfun = np.vectorize(fun)
y = vfun(x)
# set axis labels
ax = plt.gca() 
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
plt.title('Hermite Polynomial for ln(x)')
plt.plot(x, map(fun,x), linewidth="2", color="red")
plt.show()

