def tip_calculator(total, percent_int):
    return int(total) + ((int(total) * int(percent_int)) / 100)


def temperature_conversion(current_temp, current_unit, to_unit):
    pass


def c_to_k(current_temp):
    pass


def k_to_c(current_temp):
    pass


def f_to_c(current_temp):
    pass


def c_to_f(current_temp):
    pass


def f_to_k(current_temp):
    pass


def k_to_f(current_temp):
    pass


def main():
    choice = input('Tip or temperature?')
    if choice.lower() == 'tip':
        total = input('What is the total?\n')
        percent_int = input('What is the tipping rate?\n')
        print(tip_calculator(total, percent_int))
    elif choice.lower() == 'temperature':
        current_temp = input('What is the current temperature?\n')
        current_unit = input('What is the current unit?\n')
        to_unit = input('What unit should it be changed to? \n')
        print(temperature_conversion(current_temp, current_unit, to_unit))

if __name__ == '__main__':
    main()
