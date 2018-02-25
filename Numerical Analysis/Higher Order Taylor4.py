'''Order Four Taylor Method'''
from math import exp

def frange(x, y, jump):
    tmplist = []
    while x <= y:
        tmplist.append(x)
        x += jump        
    return tmplist

def f(t,y):
    return -t * y + 4*t/y

def fprime(t, y):
    return -(t *(y**2 + 4) *f(t,y) + y *(y**2 - 4))/y**2

def fprime2(t,y):
    # -(t y(t) (y(t)^2 + 4) y''(t) + 2 y'(t) (-4 t y'(t) + y(t)^3 + 4 y(t)))/y(t)^3
    return -(t * y *(y**2 + 4)* fprime(t,y) + 2 *f(t,y) *(-4* t *f(t,y) + y**3 + 4* y))/y**3

def fprime3(t,y):
    # (-t (y(t)^2 + 4) y^(3)(t) y(t)^2 + 24 y'(t)^2 (y(t) - t y'(t)) - 3 y(t) (-8 t y'(t) + y(t)^3 + 4 y(t)) y''(t))/y(t)^4
    return (-t *(y**2 + 4) * fprime2(t,y) * y**2 + 24 *f(t,y)**2 *(y - t *f(t,y)) - 3 *y *(-8 *t* f(t,y) + y**3 + 4* y)* fprime(t,y))/y**4

def t2(t,y, h):
    return f(t,y) + (h/2) * fprime(t,y)

def t4(t,y, h):
    return t2(t,y,h) + (h**2/6)*fprime2(t,y) + (h**3/24)*fprime3(t,y)

def w(ti, wi, h):
    return wi + h * t4(ti, wi, h)

fprime3(1,1)
a = 0.0
b = 1.0
h = 0.01
w0 = 1.0
for i in frange(a+h, b+h, h):
    print(i)
    
    w0 = w(i-h, w0, h)
    print("t{:.3f}: {}".format(i,w0))
print("t{:.3f}: {}".format(b,w0))
from math import exp
def y(t):
    return (4 - 3*exp(-(t**2)))**.5
print("diff: " + str(y(1.0)-w0))

