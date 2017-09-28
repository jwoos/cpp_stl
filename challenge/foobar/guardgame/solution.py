def answer(x):
    sum = 0
    int_str = str(x)
    for a_number in list(int_str):
        sum += int(a_number)
    if sum < 10:
        return sum
    else: 
        return answer(sum)

def main():
    print answer(1234123)
    print answer(123)
    print answer(5321)

if __name__ == "__main__": main()
