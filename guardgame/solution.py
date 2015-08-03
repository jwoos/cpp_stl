def answer(x):
    int_str = str(x)
    if len(int_str) > 1:
        print '%s is not single digit' %(int_str)
        str(x)
    else:
        print '%s is single digit' %(int_str)

answer(10)
