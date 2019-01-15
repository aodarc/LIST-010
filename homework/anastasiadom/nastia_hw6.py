from functools import reduce
def count_holes(n):
    number = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
    counter = 0
    if isinstance(n, float) or (isinstance(n, str) and not n.isdigit()):
        return 'ERROR'

    counter = reduce((lambda sum, key: sum + number.get(key, 0)), str(int(n)), 0)

    # for key in str(int(n)):
    # 	if number.get(key):
    #     	counter += number.get(key)

    return counter

print(count_holes('123'))
print(count_holes(906))
print(count_holes('001'))
print(count_holes(-8))
print(count_holes(-8.0))

#  count_holes(‘123’)
# 0
# ** count_holes(906)
# 3
# ** count_holes(‘001’)
# 0
# ** count_holes(-8)
# 2
# ** count_holes(-8.0)
# ERROR