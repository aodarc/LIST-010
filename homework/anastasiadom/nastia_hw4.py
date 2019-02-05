import re

def findMostFrequent(text):
    textList = re.sub(r'\W+',' ', text.lower()).split()
    resDict = { item: textList.count(item) for item in textList }
    maxValue = max(resDict.values())
    result = [key for key in resDict if resDict[key] == maxValue]
    # result = dict(filter(lambda x: x[1] == maxValue, resDict.items()))
    return result

print(findMostFrequent('Hello,Hello, my my dear!'))
print(findMostFrequent('to understand recursion you need first to understand recursion...'))
print(findMostFrequent('Mom! Mom! Are you sleeping?!!!'))