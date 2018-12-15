import re


def find_most_frequent(text):
    regex = r"[\s\.\!\,\-\d\?]+"
    cleansed_text = re.split(regex, text.lower())

    words_weight_dict = {}
    for word in cleansed_text:
        words_weight_dict[word] = words_weight_dict.setdefault(word, 0) + 1

    max_val = max(words_weight_dict.values())
    result_words_list = (k for k in words_weight_dict if words_weight_dict[k] == max_val)
    return sorted(result_words_list)


print(find_most_frequent('Hello,Hello, my dear!'))
print(find_most_frequent('to understand recursion you need first to understand recursion...'))
print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))