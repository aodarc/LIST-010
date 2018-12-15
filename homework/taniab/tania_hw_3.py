from string import digits, ascii_uppercase


def convert_n_to_m(x, n, m):
    # generate char to value map for base < 36
    chars = f'{digits}{ascii_uppercase}'
    values = range(0, 36)
    char_value_map = dict(zip(chars, values))

    # check if the number is string or int
    if not isinstance(x, (str, int)):
        return False

    # check if each digit is in the char_value_map and if it less than base
    digit = 0
    for char in str(x).upper():
        if char not in char_value_map:
            return False
        value = char_value_map[char]

        if not value < n:
            return False
        digit *= n
        digit += value

    # revers char_value map to value_char
    value_char_map = dict((v, k) for k, v in char_value_map.items())
    result = []

    # if the target base is 1, return for each position
    if m == 1:
        result = '0' * digit
    else:
        while digit:
            digit, remain = divmod(digit, m)
            result.append(value_char_map[remain])
        result.reverse()
        result = ''.join(result)
    return result


assert convert_n_to_m([123], 4, 3) is False, 'Error in case1'
assert (convert_n_to_m("0123", 5, 6) == '102'), 'Error in case2'
assert (convert_n_to_m("123", 3, 5) is False), 'Error in case3'
assert (convert_n_to_m(123, 4, 1) == '000000000000000000000000000'), 'Error in case3'
assert (convert_n_to_m(-123.0, 11, 16) is False), 'Error in case4'
assert (convert_n_to_m("A1Z", 36, 16) == '32E7'), 'Error in case5'
