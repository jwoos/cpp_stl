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
#    for x in sum_list:
 #       if sum_list.count(x) >= 2:


    dictionary = dict(sum_list, names)
    ordered_list = sorted(dictionary.items(), reverse = True)
    print dictionary
    print ordered_list
    output = []
    for b_list in ordered_list:
        output.append(b_list[1])
    print output
    return output


answer(['banana', 'apple', 'mango'])
