#!/usr/bin/env python2

def answer(l):
    length = len(l)
    mems = {}
    sorted_list = sorted(l)
    solution = 0

    for i in range(length):
        x = sorted_list[i]
        if x not in mems:
            mems[x] = set()

        for j in range(i + 1, length):
            y = sorted_list[j]

            if i != j:
                inner = mems[x]

                if y in inner:
                    continue
                elif y % x == 0:
                    inner.add(y)

    for k, v in mems.items():
        if not v:
            continue

        for x in v:
            solution += len(mems[x])

    return solution

print answer(list(range(1, 10000)))
