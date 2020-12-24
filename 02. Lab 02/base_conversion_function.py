"""
Author: Min Soo Hwang
Github ID: Delivery_KiKi
"""


def base_conversion(new_base, decimal):
    """
    Check if base-10 number is valid for calculation.

    :param new_base: an integer that indicates the destination base
    :param decimal: an integer that indicates a base-10 number
    :return: the result of the function named calculation
    """
    max_allowable_number = new_base ** 4 - 1
    if decimal > max_allowable_number:
        return -1
    elif decimal < 0:
        return -1
    else:
        return calculation(new_base, decimal)


def calculation(new_base, decimal):
    """
    Convert base-10 number to destination base number.

    :param new_base: an integer that indicates the destination base
    :param decimal: an integer that indicates a base-10 number
    :return: the result of the calculation
    """
    quotient_1 = decimal // new_base
    first_number = decimal % new_base
    quotient_2 = quotient_1 // new_base
    second_number = quotient_1 % new_base * 10
    quotient_3 = quotient_2 // new_base
    third_number = quotient_2 % new_base * 100
    forth_number = quotient_3 % new_base * 1000

    return forth_number + third_number + second_number + first_number


def main():
    # Program starts here
    test = base_conversion(2, 8)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
