import math
x = float(input( "Enter parametr  x:"))
mu = float(input( "Enter parametr  mu:"))
sigma= float(input( "Enter parametr  sigma:"))
dist = float(1/(sigma*math.sqrt(2*math.pi)))*math.exp((-(x - mu)**2)/(2*(sigma)**2))
print(dist)