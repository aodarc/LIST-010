def magic_numbers():
	minValue, maxValue = None, None

	for i in range(-200, 1000):
		if minValue is None and i*1 is i*1:
			minValue = i
		if i*1 is i*1 and i+1 is not i+1:
			maxValue = i+1

	# print ('[{}; {})'.format(minValue, maxValue))
	print (f'[{minValue}; {maxValue})')

magic_numbers()