def answer(x):
    int_str = str(x)
    if len(int_str) > 1:
        int_str_list = list(int_str)
        int_int_list = []
        for a_number in int_str_list:
            int_int_list.append(int(a_number))
        int_sum = sum(int_int_list)
        return answer(int_sum)
    else:
        return x
        print x

answer(123)
