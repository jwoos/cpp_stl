"""
n XOR 0 = n
n XOR n = 0
n XOR (n - d) = d if n and n - d are not powers of two
"""

def answer(start, length):
    # this times out
    solution = start
    go = length

    while go > 0:
        for i in range(go):
            solution ^= start + (length * i)

        start += 1
        go -= 1

    return solution

print(answer(1000000, 100))
