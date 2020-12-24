"""
Function 9 - Prime Numbers with the Sieve of Eratosthenes
Name : Min Soo (Mike) HWANG
Github ID : Delivery_KiKi
"""


def eratosthenes(uppperbound):
    """ Find prime numbers from 0 to given number inclusive.

    Decomposition : I eliminated the multiples of each prime number from the whole list of numbers.
    Pattern Matching : I used sieve of Eratosthenes to find prime numbers.
    Abstraction : I can eliminate the multiples of numbers less than the square root of the given number.
    Automation with algorithms : I eliminated the multiples of numbers by using for loops.

    /*****************************************************************************************************

    The reason why we can only calculate up to the square root of N to get prime numbers.

    The method of the seive of Eratosthenes is to remove the non-prime numbers
    from all positive integers in the range of 0 to destination number inclusive.
    A non-prime number has factors on top of 1 and itself. It means we can express a
    non-prime number like below:
        non_prime_number = a * b
        For example, number 8 can be expressed as 2 * 4.
    According to this principle, either a or b must be less than or equal to the square root of
    non_prime_number.
    Therefore, to get prime numbers, we can remove all the multiples of numbers between 2 and
    the square root of the destination number inclusive.

    *****************************************************************************************************/

    :param uppperbound: a positive integer
    :precondition: upperbound must be equal to or greater than zero
    :postcondition: return a list of every prime number between zero to upperbound inclusive
    :return: a list of every prime number from zero to upperbound inclusive

    >>> eratosthenes(27)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> eratosthenes(45)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    >>> eratosthenes(82)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
    """
    # Make a list of the whole numbers
    number_list = list(range(uppperbound + 1))

    # Eliminate 0 from the list
    if 0 in number_list:
        number_list.remove(0)
    # Eliminate 1 from the list
    if 1 in number_list:
        number_list.remove(1)
    # Calculate the square root of the given number as an integer
    maximum = int(uppperbound ** 0.5) + 1
    # Generate numbers from 2 to square rooted number (maximum number)
    for number in range(2, maximum + 1):
        # Get the multiples of each number starting from multiplying 2
        for multiple in range(number * 2, uppperbound + 1, number):
            # Eliminate the multiples from the list
            if multiple in number_list:
                number_list.remove(multiple)

    # return the list
    return number_list


def main():
    # Program starts here
    test = eratosthenes(82)
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
