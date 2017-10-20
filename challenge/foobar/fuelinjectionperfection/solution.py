#!/usr/bin/env python2

import math


def answer(n):
    n = int(n)
    moves = 0

    while n > 1:
        upper_logged = math.log(n + 1, 2)
        print upper_logged
        if n != 3 and upper_logged % 1 == 0:
            n = 1
            moves += upper_logged + 1
        else:
            if n % 2 == 0:
                n /= 2
                moves += 1
            else:
                n -= 1
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
