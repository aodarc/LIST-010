import sys
import math
print ("This is the name of the script: ", sys.argv[0])
x = float(sys.argv[1])
mu = float(sys.argv[2])
sigma = float(sys.argv[3])
f = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu)**2)/(2*sigma**2))

print(f)
