import re


def is_palindrome(string):
    string = str(string) if not isinstance (string, str) else string

    pattern = r"\s+"
    cleaned = re.sub(pattern, '', string.lower())
    return 'YES' if cleaned == cleaned[::-1] else 'NO'


print(is_palindrome(0))
print(is_palindrome('puppy'))
print(is_palindrome('mystring1Gni rts ym'))