# itertools, map/lambda/reduce/filter
from itertools import cycle

# usage of cycle() for dict generation
# relust: {1: 1, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 3}
keys = range(1,10)
d = dict(zip(keys, cycle(range(1,4))))
print(d)

# getting the list of odd nums
# relust: [1, 3, 5, 7]
l = range(9)
odd_numbers = filter(lambda x: x%2, l)
print(list(odd_numbers))

# map all functions to the list of argumens
# result:
# 0 [0, 0]
# 1 [1, 2]
def multiply(x):
    return x*x
def add(x):
    return x+x

funcs = [multiply, add]
for i in range(2):
    value = list(map(lambda x: x(i), funcs))
    print(i, value)