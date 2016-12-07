import operator

'''
def find_consecutive(numbers):
    solution_index = []
    enum = list(enumerate(numbers))
    for a_tuple in enum:
        if a_tuple[0] <= enum[-3][0]:
            if map(operator.itemgetter(1), enum)[a_tuple[0]:a_tuple[0] + 3] == [a_tuple[1], a_tuple[1] + 1, a_tuple[1] + 2] or map(operator.itemgetter(1), enum)[a_tuple[0]:a_tuple[0] + 3] == [a_tuple[1], a_tuple[1] - 1, a_tuple[1] - 2]:
                solution_index.append(a_tuple[0])
    for i in enum:
        print int(i[0])
    return solution_index or None
'''


def find_consecutive(numbers):
    solution_index = []
    enum = list(enumerate(numbers))
    for a_tuple in enum:
        if a_tuple[0] <= enum[-3][0]:
            if map(operator.itemgetter(1), enum)[a_tuple[0]:a_tuple[0] + 3] == [a_tuple[1], a_tuple[1] + 1, a_tuple[1] + 2] or map(operator.itemgetter(1), enum)[a_tuple[0]:a_tuple[0] + 3] == [a_tuple[1], a_tuple[1] - 1, a_tuple[1] - 2]:
                solution_index.append(a_tuple[0])
    return solution_index or None

assert find_consecutive([]) == None
assert find_consecutive([0, 1, 9, 10]) == None
assert find_3([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7]) == [0, 4, 6, 7]
assert find_consecutive([1, 2, 3, 2, 1]) == [0, 2]
assert find_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7]
assert find_consecutive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7]
assert find_consecutive([1, 2, 4, 5, 6, 8, 9]) == [2]
