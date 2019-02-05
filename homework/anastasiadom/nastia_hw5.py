import re
import sys

def strPolindrom(inputValue):
	inputValue=re.sub(r'\s+','', inputValue.lower())
	return 'YES' if inputValue==inputValue[::-1] else 'NO'

print (strPolindrom(sys.argv[1]))