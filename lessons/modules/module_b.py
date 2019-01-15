import human_code

import package
from .package import module1


from .module_a import *
# import math
# import base64  # 1
#
# # base64 = lambda s: -s
# # base64 = 'some string'
#
# from math import sin as s
#
# hotabych = 'Anton'
#
#
# print(s)
# # print(base64.b16decode('das'))
# print("module A")
# print(math.pi)


def main() -> None:
	print('Module B is runing')
	# print(math.pi)
	# print(base64)
	# print(hotabych)
	print(module1)
	print(package.INIT_P)

if __name__ == '__main__':
	main()
	# print(__name__, ': MODULE B __name__')


