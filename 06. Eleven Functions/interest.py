"""
Function 4 - Compound Interest
Name : Min Soo (Mike) HWANG
Github ID : Delivery_KiKi
"""


def compound_interest(principal, interest, interest_per_year, number_of_years):
    """ Calculate compound interest.

    Decomposition : I did not use decomposition because the formula is an already decomposed tool.
    Pattern Matching : The formula of compound interest will always do the same calculation.
    Abstraction : No matter what your inputs are, the function will calculate the compound interest.
    Automation with algorithms : The compound interest is calculated by a certain formula.

    :param principal: a floating point number
    :param interest: a floating point number
    :param interest_per_year: a positive integer
    :param number_of_years: a positive integer
    :precondition: principal and interest must be a floating point number
    :precondition: interest_per_year and number_of_years must be a positive integer
    :precondition: interest_per-year and number_of_years must be equal to or greater than zero
    :postcondition: calculates the compound interest based on the inputs
    :return: total amount of money grown up with the compound interest

    >>> compound_interest(13.65, 2.5, 1, 10)
    'Your money will be grown up by $17.47'
    >>> compound_interest(100, 5, 1, 10)
    'Your money will be grown up by $162.89'
    >>> compound_interest(1000, 2.5, 2, 1)
    'Your money will be grown up by $1025.16'
    """
    # Calculate the compound interest based on the inputs
    total_money = principal * ((1 + (interest * 0.01 / interest_per_year)) ** (interest_per_year * number_of_years))
    return "Your money will be grown up by $%s" % str(round(total_money, 2))


def main():
    # Program starts here
    test = compound_interest(1000, 2.5, 2, 1)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
