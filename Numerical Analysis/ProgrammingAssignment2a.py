# Composite Trapezoid Rule
from math import inf
def f(x):
    return 5 / (1 + x**4)

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def rrap(start, end):
    h = start + end
    summ = f(start) + f(end)
    return h/2 * summ

a = 0
b = 1
step = 1
epsilon = 10**-5
compTrapLast = inf
while True:
    data = list(frange(a, b, step))
    compTrapNew = compTrap(data)
    print("n = " + str(int(1/step)) + ": " + str(compTrapNew))
    if abs(compTrapLast - compTrapNew) < epsilon:
        print("Answer " + "{:.5f}".format(compTrapNew) + " with n = " + str(int(1/step)))
        break;
    else:
        step /= 2
        compTrapLast = compTrapNew
