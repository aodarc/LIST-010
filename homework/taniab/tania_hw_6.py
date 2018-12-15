from functools import reduce


def count_holes(num):
    holes_dict = {
        0: 1,
        4: 1,
        6: 1,
        8: 2,
        9: 1,
    }

    if not isinstance(num, (int, str)):
        return "ERROR"

    num = abs(int(num))
    # result = 0
    num_list = [int(x) for x in str(num)]

    result = reduce(lambda a, x: a + holes_dict.get(x, 0), num_list, 0)
    # for i in num_list:
    # 	result += holes_dict.get(i, 0)

    return result


print(count_holes('123'))
print(count_holes(906))
print(count_holes('001'))
print(count_holes(-8))
print(count_holes(-8.0))
