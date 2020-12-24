"""
Assignment 1
Function 2
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


def colour_mixer():
    """ Accept the user's input and check if the user's input is 'red', 'blue' or 'yellow'.
    The user's input is case-insensitive and it might contain whitespaces.

    Decomposition : I decomposed one function into two functions only for the user's input.
    Pattern Matching : I can get correct secondary colour when I mix primary colours.
    Abstraction : No abstraction because this function can only be used with 'red', 'blue', and 'yellow'.
    Automation with algorithms : I considered every conditions with if/and/or statements.

    :post-condition: check if the user's input is 'red', 'blue' or 'yellow'
    :return: call the function named colour_mixer_helper if each input is one of 'red', 'blue' or 'yellow'
    """
    # Accept the user's inputs and preprocess them
    first_colour = input("Enter the 1st colour (Red, Blue, Yellow): ")
    second_colour = input("Enter the 2nd colour (Red, Blue, Yellow): ")
    first_colour = ''.join(first_colour.lower().split())
    second_colour = ''.join(second_colour.lower().split())

    # Make a list of primary colours
    primary_colours = ['red', 'blue', 'yellow']
    error_messages = ["You entered nothing. Try again :(", "Try to enter two different colours"]
    # If both user's inputs are a blank, print error message
    if first_colour == '' and second_colour == '':
        print(f"{error_messages[0]}")
    # If both user's inputs are the same each other, print error message
    elif first_colour == second_colour:
        print(f"{error_messages[1]}")
    # If both user's inputs are not either 'red', 'blue', or 'yellow', print error message
    elif first_colour not in primary_colours or second_colour not in primary_colours:
        print(f"Both two primary colours must be {primary_colours[0]}, {primary_colours[1]}, or {primary_colours[2]}")
    # If both user's inputs are valid, call the function called colour_mixer_helper
    else:
        return colour_mixer_helper(first_colour, second_colour)


def colour_mixer_helper(first_colour, second_colour):
    """ Mix two primary colours into the secondary colour.
    :param first_colour: a string 'red', 'blue', or 'yellow'
    :param second_colour: a string 'red', 'blue', or 'yellow'
    :precondition: the value of both first_colour and second_colour must be 'red', 'blue' or 'yellow
    :postcondition: show the result of mixing first_colour and second_colour
    :return: result of mixing first_colour and second_colour
    >>> colour_mixer_helper('red', 'blue')
    'Purple'
    >>> colour_mixer_helper('yellow', 'red')
    'Orange'
    >>> colour_mixer_helper('yellow', 'blue')
    'Green'
    """
    # Initialize a variable
    result = ""
    # If the user's inputs are either 'red' or 'blue', the secondary colour is Purple
    if (first_colour == 'red' and second_colour == 'blue') or \
            (first_colour == 'blue' and second_colour == 'red'):
        result = "Purple"
    # If the user's inputs are either 'red' or 'yellow', the secondary colour is Orange
    elif (first_colour == 'red' and second_colour == 'yellow') or \
            (first_colour == 'yellow' and second_colour == 'red'):
        result = "Orange"
    # If the user's inputs are either 'blue' or 'yellow', the secondary colour is Green
    elif (first_colour == 'yellow' and second_colour == 'blue') or \
            (first_colour == 'blue' and second_colour == 'yellow'):
        result = "Green"

    # Return the result
    return result


def main():
    # Program starts here
    test = colour_mixer()
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
