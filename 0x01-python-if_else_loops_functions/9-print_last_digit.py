def print_last_digit(number):
    if number > 0:
        number = number % 10
    else:
        number = abs(number % -10)
    print(number, end="")
    return number
