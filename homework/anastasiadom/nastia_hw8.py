lst = [9,6,8,4,5,2,3,67,3,7]
tpl = ((1,2) , (4,6) , (3,6) , (3,0) , (3,5))
s = 'aAbBcCdD'

def sorted(l, key = (lambda x: x), reverse = False):
	n = 1
	l = list(l)
	length = len(l)
	while n < length:
		for i in range(length - n):
			if key(l[i]) < key(l[i + 1]):
				l[i], l[i + 1] = l[i + 1], l[i]
		n += 1
	return l[::-1] if reverse else l


print(sorted(s))
print(sorted(s, key = str.upper, reverse = True))
print(sorted(tpl, key = (lambda x: x[1]), reverse = False))
print(sorted(tpl, key = (lambda x: x[0]), reverse = True))
print(sorted(lst, reverse = False))
print(sorted(lst, reverse = True))
