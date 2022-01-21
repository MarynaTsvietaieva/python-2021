# -*- coding: utf-8 -*-

def is_birth_number(check_str):
    # check if a string represents a birth number
    # valid birth number:
    # has a '/' on position 7
    # sum of digits is divisible by 11

    if check_str[6] != '/':
         raise ValueError("On the seventh position should be '/'")
    if(check_str.count('/') != 1):
          raise ValueError("Birth number should contain only one '/'")
    date, id_number = check_str.split('/')
    digit_sum = 0
    if(len(date) != 6):
          raise ValueError("There must be 6 digits before the slash and 4 after")
    if(len(id_number) != 4):
          raise ValueError("There must be 6 digits before the slash and 4 after")
    for digit in date:

        if (digit.isnumeric() == False):
           raise TypeError("Elements must be numbers")
        digit_sum += int(digit)
    for digit in id_number:
        if (digit.isnumeric() == False):
          raise TypeError("Elements must be numbers")
        digit_sum += int(digit)

    if (digit_sum % 11 == 0):
        print("This is birth number")
        return True
    else:
        print("This isn't birth number")
        return False
is_birth_number('111111/1112')
