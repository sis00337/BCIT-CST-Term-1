"""
Assignment 1
Function 1
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


def roman_numeral(positive_int):
    """ Convert an integer to Roman numeral.

    Decomposition : The parameter will be divided by every single number in the list.
    Pattern Matching : Finding Roman numeral is similar with finding quotient and remainder.
    Abstraction : The function is reusable in terms of ideas for finding quotient and remainder.
    Automation with algorithms : I made lists first and make a Roman numeral by multiplying the quotient.

    :param positive_int: an integer in a range of 1 to 10,000 inclusive
    :precondition: positive_integer must be equal to or greater than one and equal to or less than ten-thousand
    :postcondition: returns the correct Roman numeral equivalent to the integer
    :return: Roman numeral equivalent to the integer

    >>> roman_numeral(4)
    'IV'
    >>> roman_numeral(94)
    'XCIV'
    >>> roman_numeral(950)
    'CML'
    """
    # Make a list of Roman numeral characters
    roman_chr = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    # Make a list of numbers corresponding the Roman numeral
    integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # Initialize a variable
    result = ''
    # Calculate the Roman numeral equivalent to the given number
    for number in range(len(roman_chr)):
        quotient = positive_int // integers[number]
        result += roman_chr[number] * quotient
        positive_int -= integers[number] * quotient

    return result


def main():
    # Program starts here
    test = roman_numeral(90)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
