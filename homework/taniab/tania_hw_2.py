import sys
from math import sqrt, pi, exp


def calculate(a: float, b: float, c: float) -> float:
    return 1 / (c * sqrt(2*pi)) * exp(-1 * (a**2 - 2*a*b + b**2) / 2*c**2)


if __name__ == '__main__':
    x, y, z = map(float, sys.argv[1:4])
    result = calculate(x, y, z)
    print(f'{result:.12}')

