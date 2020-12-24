"""
Assignment 1
Function 6
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""

import random


def number_generator():
    """ Generate six random integers between 1 to 49 inclusive.

    Decomposition : I organized the function step by step (list - random number - sorting)
    Pattern Matching : As using random module, I can believe that randomized numbers will come out.
    Abstraction : The function is reusable because I used the module and method which is already existed.
    Automation with algorithms : I made a list of integers first and randomly chose six numbers from it.

    :postcondition: return a sorted list of six integers between 1 to 49 inclusive in ascending order
    :return: list of six random integers between 1 to 49 inclusive sorted in ascending order
    """
    # Make a list of numbers between 1 to 49 inclusive
    number_range = list(range(1, 50))
    # Randomly pick 6 numbers from the list
    random_number = random.sample(number_range, 6)
    # Sort the list of the 6 numbers in ascending order
    sorted_random_number = sorted(random_number)
    # Return the sorted list
    return sorted_random_number


def main():
    # Program starts here
    test = number_generator()
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
