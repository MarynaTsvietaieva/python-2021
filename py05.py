# -*- coding: utf-8 -*-

def is_composite(number):
    # checks if a number is a composite - has dividors apart from 1 and itself
    # input from user should be a positive integer
    if not isinstance(number, int) or number < 2:
        return
    if number == 2 :
        return False
    for i in range(2,number-1):
        if number % i == 0:
            return True

    return False

def test_is_composite():
    # test for invalid input - handle it as you wish
    # test for extreme input
    # test for at least 10 standard inputs
    assert is_composite(-1) == None or is_composite("LALA") == None
    print("test for invalid input")
    assert is_composite(2) == False

    print("test for extreme input")
    assert is_composite(14) == True
    assert is_composite(16) == True
    assert is_composite(12) == True
    assert is_composite(10) == True
    assert is_composite(18) == True
    assert is_composite(7) == False
    assert is_composite(3) == False
    assert is_composite(11) == False
    assert is_composite(17) == False
    assert is_composite(23) == False

    print("All tests were passed")

    pass

if __name__ == '__main__':
    test_is_composite()