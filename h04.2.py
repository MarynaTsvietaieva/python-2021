# -*- coding: utf-8 -*-

def sum_of_n_numbers(n):
    # returns the sum of the first n numbers
    # n should be a positive integer
    if type(n) != int:
        raise TypeError("Input value must be an integer.")
    if n < 1:
        raise ValueError("Input value must be an integer bigger than 0.")
    result_sum = 0
    for i in range(1, n + 1):
        result_sum += i

    return result_sum

sum_of_n_numbers(7)
