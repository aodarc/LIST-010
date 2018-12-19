from math import exp, pi, sqrt
from sys import argv

x, m, s = map(float, (argv[1], argv[2], argv[3]))

def f(x):
    return exp(-((x-m)**2)/((s**2)*2))/(sqrt(2*pi)*s)
    
print(f(x))
