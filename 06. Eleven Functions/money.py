"""
Function 10 - Money Distributor
Name : Min Soo (Mike) HWANG
Github ID : Delivery_KiKi
"""


def cash_money(total):
    """ Convert money into each Canadian monetary unit including penny.

    Decomposition : I divided the whole amount of money by each unit.
    Pattern Matching : Converting money into different units is similar with finding quotient and remainder.
    Abstraction : The function is reusable in terms of ideas for finding quotient and remainder.
    Automation with algorithms : I multiplied 100 to the given floating point number to avoid the error of floats.

    :param total: a floating point number with two decimal places
    :precondition: total must has two decimal places
    :postcondition: calculates the number of each monetary unit
    :return: a list including the number of bills and coins

    >>> cash_money(14.62)
    [0, 0, 0, 1, 0, 2, 0, 2, 1, 0, 2]
    >>> cash_money(62.74)
    [0, 1, 0, 1, 0, 1, 0, 2, 2, 0, 4]
    >>> cash_money(316.21)
    [3, 0, 0, 1, 1, 0, 1, 0, 2, 0, 1]
    """
    # Make the given number be an integer by multiplying 100
    total = round(total * 100)
    # Make a list of the Canadian monetary units which are multiplied 100
    units = [10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]
    # Initialize a list
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Break down the whole amount of money into each monetary unit
    for number in range(len(units)):
        quotient = total // units[number]
        values[number] += quotient
        total -= units[number] * quotient

    # Return the list that includes the number of bills and coins
    return units


def main():
    # Program starts here
    test = cash_money(316.09)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
