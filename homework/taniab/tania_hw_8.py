# bubble sort
test = [{'value': 1625065},
 {'value': 94},
 {'value': 59},
 {'value': 910},
 {'value': 1385556},
 {'value': 176},
 {'value': 347051},
 {'value': -401731},
 {'value': -24559}]


def bubble(iterable, key=None, reversed=False):
    lst = list(iterable)
    key = key if key is not None else lambda elem: elem
    length = len(lst) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if key(lst[i]) > key(lst[i+1]):
                is_sorted = False
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if reversed:
            return lst[::-1]
    return lst


print(bubble(test, key=lambda x: x['value']))
