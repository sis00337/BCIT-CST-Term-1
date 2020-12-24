"""
Author: Min Soo Hwang
Github ID: Delivery_KiKi
"""


import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Check if either number_of_rolls or number_of_sides is less than or equal to 0.

    :param number_of_rolls: an integer that indicates the number of rolls
    :param number_of_sides: an integer that indicates the number of sides of a die
    :return: the result of the function named rolling_die
    """
    if number_of_rolls <= 0:
        return 0
    elif number_of_sides <= 0:
        return 0
    else:
        return rolling_die(number_of_rolls, number_of_sides)


def rolling_die(number_of_rolls, number_of_sides):
    """
    Pick a number between minimum and maximum number.

    :param number_of_rolls: an integer that indicates the number of rolls
    :param number_of_sides: an integer that indicates the number of sides of a die
    :return: a randomized number between minimum and maximum number
    """
    min_number = number_of_rolls * 1
    max_number = number_of_rolls * number_of_sides
    random_total = random.randrange(min_number, max_number+1)
    return random_total


def main():
    # Program starts here
    test = roll_die(3, 6)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
