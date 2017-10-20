#!/usr/bin/env python2

from decimal import Decimal, getcontext
import math

def decimal_log(num, base):
    return num.log10() / base.log10()

def answer(n):
    getcontext().prec = 350
    n = Decimal(n)
    zero = Decimal('0')
    one = Decimal('1')
    two = Decimal('2')
    three = Decimal('3')
    round_to = Decimal('0.00001')
    moves = 0

    while n > one:
        upper_logged = decimal_log(n + one, two).quantize(round_to)
        # move
        if n != three and upper_logged.remainder_near(one) == zero:
            n = one
            moves += upper_logged.to_integral_exact() + 1
        else:
            if n.remainder_near(two) == zero:
                n /= two
                moves += 1
            else:
                n -= one
                moves += 1

    return int(moves)

print answer('100000000000000000000000000000000000000000000000000000000')
print answer('65')
print answer('32')
print answer('18')
print answer('15')
print answer('4')
print answer('3')
print answer('1')
