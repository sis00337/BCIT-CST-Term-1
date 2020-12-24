"""
Function 3 - Time Calculator
Name : Min Soo (Mike) HWANG
Github ID : Delivery_KiKi
"""


def time_calculator(seconds):
    """ Convert seconds to weeks, days, hours, minutes, and seconds.

    Decomposition : The parameter will be divided by every units.
    Pattern Matching : Converting seconds into different units is similar with finding quotient and remainder.
    Abstraction : The function is reusable in terms of ideas for finding quotient and remainder.
    Automation with algorithms : I made lists first and assign the value of each unit by adding the quotient.

    :param seconds: a positive integer
    :precondition: seconds must be equal to or greater than zero
    :postcondition: calculates correct weeks, days, hours, minutes, and seconds equivalent to the total seconds
    :return: nothing

    >>> time_calculator(3666)
    0   0   1   1   6
    >>> time_calculator(86400)
    0   1   0   0   0
    >>> time_calculator(1000000)
    1   4   13   46   40
    """
    # Assign values to the variables
    week = 86400 * 7
    day = 86400
    hour = 3600
    minute = 60
    second = 1

    # Make a list of time units
    units = [week, day, hour, minute, second]
    # Initialize a list
    values = [0, 0, 0, 0, 0]
    # Convert seconds to weeks, days, hours, minutes, and seconds
    for number in range(len(units)):
        quotient = seconds // units[number]
        values[number] = str(quotient)
        seconds -= units[number] * quotient
    # Make the list as a line of string
    result = '   '.join(values)

    # Print the result
    print("%s" % result)


def main():
    # Program starts here
    time_calculator(3666)


if __name__ == '__main__':
    # invoke the main function
    main()
