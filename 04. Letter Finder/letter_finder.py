"""
Letter Finder
Name : Min Soo (Mike) HWANG
Github ID : Delivery_KiKi
"""

from typing import TextIO
from io import StringIO
from itertools import combinations


def a_finder(filename: str, letter: str) -> None:
    """ Open a text file, preprocess the data, and find probability that a set of letters contains the certain letter.

    :precondition: the functions in a_finder must be correctly operated
    :postcondition: open a text file, process the data, and find probability that
                    a set of letters among the second line of text contains the certain letter
    :return: nothing
    """
    with open(filename) as file_object:
        text_list = process_data(file_object)
    calculate_probability(letter, text_list)


def process_data(file_object: TextIO) -> list:
    """ Take the text file, split a line of text by a space, and store the value to a list.

    :param file_object: an object of the text file.
    :precondition: each line of text must be separated by space and each line must be separated by <Enter> key
    :postcondition: make a list of the lists that contain the information of each line of text separating by a space
    :return: a list of lists that contains the information of each line of text

    >>> text_file = StringIO('')
    >>> process_data(text_file)
    []
    >>> text_file = StringIO('\\n\\n\\n\\n\\n')
    >>> process_data(text_file)
    [[''], [''], [''], [''], ['']]
    >>> text_file = StringIO('1.3 3.4\\n2 4.2\\n-1 1\\n')
    >>> process_data(text_file)
    [['1.3', '3.4'], ['2', '4.2'], ['-1', '1']]
    >>> text_file = StringIO('4\\na a b c\\n2\\n')
    >>> process_data(text_file)
    [['4'], ['a', 'a', 'b', 'c'], ['2']]
    """
    text_list = [line.replace('\n', '').split(' ') for line in file_object]
    return text_list


def calculate_probability(letter: str, text_list: list) -> None:
    """ Find the probability that the sequence of letters contains the certain letter.

    :param letter: a letter that will be used for calculating the probability
    :param text_list: a list of the lists that contain the information of each row of the text file
    :precondition: letter can be any letters but spaces
    :precondition: the length of text_list must be 3
    :precondition: text_list[0] must be a string of a number between 1 to 10 inclusive
    :precondition: the length of text_list[1] must be the same as the numerical value of text_list[0]
                   and made up of any characters but spaces
    :precondition: text_list[1] must be a string of a number between 1 to the numerical value of text_list[0] inclusive
    :postcondition: print the probability that sequence of letters in text_list[1] contains letter
    :return: nothing

    >>> string_to_find = 'a'
    >>> line_list = [['4'], ['a', 'a', 'b', 'c'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.8333 probability that a pair of items selected will contain one or more 'a'
    >>> string_to_find = 'b'
    >>> line_list = [['1'], ['a'], ['1']]
    >>> calculate_probability(string_to_find, line_list)
    0.0 probability that a pair of items selected will contain one or more 'b'
    >>> string_to_find = 'c'
    >>> line_list = [['5'], ['c', 'b', 'a', 't', 'a'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.4 probability that a pair of items selected will contain one or more 'c'
    >>> string_to_find = '&'
    >>> line_list = [['4'], ['&', '&', 'a', 't'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.8333 probability that a pair of items selected will contain one or more '&'
    >>> string_to_find = 'A'
    >>> line_list = [['4'], ['A', 'A', 'a', 't'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.8333 probability that a pair of items selected will contain one or more 'A'
    >>> string_to_find = 'Z'
    >>> line_list = [['4'], ['Z', 'Z', 'a', 't'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.8333 probability that a pair of items selected will contain one or more 'Z'
    >>> string_to_find = '0'
    >>> line_list = [['4'], ['0', '0', 'a', 't'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.8333 probability that a pair of items selected will contain one or more '0'
    >>> string_to_find = '9'
    >>> line_list = [['4'], ['9', '9', 'a', 't'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.8333 probability that a pair of items selected will contain one or more '9'
    >>> string_to_find = '1234567890'
    >>> line_list = [['4'], ['1234567890', '1234567890', 'a', 't'], ['2']]
    >>> calculate_probability(string_to_find, line_list)
    0.8333 probability that a pair of items selected will contain one or more '1234567890'
    """
    try:
        letters = text_list[1]
        n_list = list(range(len(letters)))
        number_k = int(text_list[2][0])
        result = set()
        combination_list = list(combinations(n_list, number_k))
        for index in combination_list[:]:
            for number in index:
                if letters[number] == letter:
                    result.add(index)
        probability = round(len(result) / len(combination_list), 4)
        print(f"{probability} probability that a pair of items selected will contain one or more '{letter}'")
    except ZeroDivisionError:
        print('CHECK THE TEXT FILE.')
        print("The second line in the text file must include letters divided by a space.")
    except IndexError:
        print('CHECK THE TEXT FILE.')
        print("The third line in the text file must include an integer.")


def main() -> None:
    """
    Drives the program.
    """
    # import doctest
    # doctest.testmod(verbose=True)
    a_finder('find_probability.txt', 'a')


if __name__ == "__main__":
    main()
