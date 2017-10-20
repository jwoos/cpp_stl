#!/usr/bin/env python2

from decimal import Decimal
import math


def answer(n):
    n = Decimal(n)
    two = Decimal('2')
    is_even = not n % two
    bit_count = math.log(n, two)
    moves = 0

    if int(bit_count) != bit_count:
        upper_bit_count = math.ceil(bit_count)
        upper = math.pow(2, upper_bit_count)
        upper_diff = abs(upper - int_n)

        lower_bit_count = math.floor(bit_count)
        lower = math.pow(2, lower_bit_count)
        lower_diff = abs(lower - int_n)

        if upper_diff < lower_diff:
            # if upper_diff is lower, go up
            bit_count = upper_bit_count
            moves += upper_diff
        else:
            # if equal or greater, go down
            bit_count = lower_bit_count
            moves += lower_diff

    moves += bit_count

    return int(moves)

print answer(15)
print answer(4)
print answer(3)
print answer(1)
