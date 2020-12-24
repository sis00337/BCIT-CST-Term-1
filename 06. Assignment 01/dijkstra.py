"""
Assignment 1
Function 11
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


def dijkstra(given_list):
    """ Rearrange the given list in order of the Dutch National Flag.

    Decomposition : I rearranged the list colour by colour.
    Pattern Matching : I counted the number of each colour first, initialized the list, and rearranged the list.
    Abstraction : No matter what your input is, the function will rearrange your list.
    Automation with algorithms : I counted the number of each colour and added to the list in the designated order.

    :param given_list: a list containing randomly shuffled strings
    :precondition: the elements of given_list must be 'red', 'white' or 'blue'
    :post-condition: rearrange the given list in order of the Dutch National Flag
    :return: nothing

    >>> empty_list = []
    >>> dijkstra(empty_list)
    >>> print(empty_list)
    []
    >>> short_list = ['white', 'red', 'blue']
    >>> dijkstra(short_list)
    >>> print(short_list)
    ['red', 'white', 'blue']
    >>> long_list = ['blue', 'red', 'blue', 'white', 'white', 'blue', 'blue']
    >>> dijkstra(long_list)
    >>> print(long_list)
    ['red', 'white', 'white', 'blue', 'blue', 'blue', 'blue']
    >>> red_list = ['red', 'red', 'red', 'red']
    >>> dijkstra(red_list)
    >>> print(red_list)
    ['red', 'red', 'red', 'red']
    >>> white_list = ['white', 'white', 'white', 'white']
    >>> dijkstra(white_list)
    >>> print(white_list)
    ['white', 'white', 'white', 'white']
    >>> blue_list = ['blue', 'blue', 'blue', 'blue']
    >>> dijkstra(blue_list)
    >>> print(blue_list)
    ['blue', 'blue', 'blue', 'blue']
    """
    # Count the number of each colour
    reds = given_list.count('red')
    whites = given_list.count('white')
    blues = given_list.count('blue')

    # Initialize the given list
    for element in range(len(given_list[:])):
        given_list.pop()
    # Add all the 'red' to the list
    for number_red in range(0, reds):
        given_list.append('red')
    # Add all the 'white' to the list
    for number_white in range(0, whites):
        given_list.append('white')
    # Add all the 'blue' to the list
    for number_blue in range(0, blues):
        given_list.append('blue')


def main():
    # Program starts here
    dutch = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white', 'blue', 'red']
    dijkstra(dutch)
    print(dutch)


if __name__ == '__main__':
    # invoke the main function
    main()
