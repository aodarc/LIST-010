import re
from collections import Counter
def find_most_frequent(text):
    textList = re.sub(r'\W+',' ',text.lower()).split()
    resDict = Counter(textList)

    maxValue = max(resDict.values())
    result = [key for key in resDict if resDict[key] == maxValue]
    # result = dict(filter(lambda x: x[1] == maxValue, resDict.items()))
    return result

print(find_most_frequent('Hello,Hello, my my dear!'))
print(find_most_frequent('to understand recursion you need first to understand recursion...'))
print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))