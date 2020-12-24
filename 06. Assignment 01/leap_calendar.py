"""
Assignment 1
Function 8
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""

import calendar


def leap_years(first_year, final_year):
    """ Calculate the number of leap years.

    Decomposition : No decomposition because this function is straightforward.
    Pattern Matching : As using leapdays method, I can believe that the number of leap years will come out.
    Abstraction : No matter what your inputs are, the function will calculate the number of leap years.
    Automation with algorithms : This fuction is straightforward. Accept parameters, calculate, and return.

    :param first_year: a positive integer
    :param final_year: a positive integer
    :precondition: first_year must be equal to or greater than 1, and equal to or less than final_year
    :postconditon: calculates the number of leap years between first_year and final_year
    :return: the number of year between first_year and final_year

    >>> leap_years(1, 2020)
    490
    >>> leap_years(2000, 3000)
    243
    >>> leap_years(2016, 2016)
    1
    """
    # Calculate the number of leap years
    number_of_leap_years = calendar.leapdays(first_year, final_year + 1)
    return number_of_leap_years


def main():
    # Program starts here
    test = leap_years(2000, 2030)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
