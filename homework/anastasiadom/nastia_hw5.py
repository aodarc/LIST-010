import re
import sys

def StrPolindrom(s):
	s1=s.lower()
	s2=re.sub(r'\s+','',s1)
	s3=s2[::-1]
	return 'YES' if s3==s2 else 'NO'

print (StrPolindrom(sys.argv[1]))