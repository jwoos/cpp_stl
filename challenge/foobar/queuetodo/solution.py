#!/usr/bin/env python2
"""
n XOR 0 = n
n XOR n = 0
"""

def xor(a, b):
    diff = b - a

    if diff == 0:
        return a
    elif diff < 4:
        return reduce(lambda c, d: c ^ d, range(a, b + 1))
    else:
        return xor(a, a // 4 * 4 + 4) ^ xor(b // 4 * 4, b)


def answer(start, length):
    line = [(
        start + (length - i) * length,
        start + (length - i) * length + i - 1
    ) for i in range(length, 0, -1)]

    row = [xor(a, b) for a, b in line]

    return reduce(lambda a, b: a ^ b, row)

print(answer(0, 3))
print(answer(17, 4))
print(answer(17, 250))
print(answer(17, 2500))
