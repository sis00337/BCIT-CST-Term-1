"""
Author: Min Soo Hwang
Github ID: Delivery_KiKi
"""


import random
import string


def create_name(length):
    """
    Check if length of a name is less than or equal to 0.

    :param length: an integer that indicates the length of a name
    :return: the result of the function named create_random_name
    """
    if length <= 0:
        return None
    else:
        return create_random_name(length)


def create_random_name(length):
    """
    Creating a randomized name.

    :param length: an integer that indicates the length of a name
    :return: Capitalized and randomized name
    """
    name = (''.join(random.choices(string.ascii_lowercase, k=length)))
    name_capitalized = name.capitalize()
    return name_capitalized


def main():
    # Program starts here
    test = create_name(12)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
