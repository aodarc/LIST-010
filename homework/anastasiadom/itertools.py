from functools import reduce
from itertools import accumulate
from operator import mul

class Tools:

	def reduceStaff(self, lst = None):
		lst = lst or []
		product = reduce((lambda x, y: x*y), lst)
		print(product)

	def filterStaff(self, lst = None):
		lst = lst or []
		grater_than_five = list(filter(lambda x: x>5, lst))
		print(grater_than_five)

	def mapStaff(self, lst = None):
		lst = lst or []
		squared = list(map(lambda x: x**2, lst))
		print(squared)

	def accumulateStaff(self, lst = None):
		lst = lst or []
		mulv = list(accumulate(lst, mul))
		print(mulv)

l = range(1,9)
tools1 = Tools()
tools1.reduceStaff(l)
tools1.filterStaff(l)
tools1.mapStaff(l)
tools1.accumulateStaff(l)
