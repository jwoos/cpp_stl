import operator


def answer(names):
    list_list = []
    for name in names:
        integer_list = []
        for character in name:
            number = ord(character) - 96
            integer_list.append(number)
        list_list.append(integer_list)
    print list_list
    sum_list = []
    for a_list in list_list:
        sum_list.append(sum(a_list))
    print sum_list
    name_sum_list = []
    for x in range(0, len(names)):
        temp_list = [sum_list[x], names[x]]
        name_sum_list.append(temp_list)
    ordered_list = sorted(name_sum_list, reverse=True, key=operator.itemgetter(0, 1))
    print name_sum_list
    output = []
    for b_list in ordered_list:
        output.append(b_list[1])
    print output
    return {'output': output, 'name_sum_list': name_sum_list, 'sum_list': sum_list, 'list_list': list_list}
