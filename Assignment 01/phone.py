"""
Assignment 1
Function 7
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


def number_translator():
    """ Prompt the user for 10-digit alphabetical phone number.

    The function also check if the user entered number in the right format.
    The user's input is case-insensitive and it might contain whitespaces.

    Decomposition : I decomposed one function into two functions only for the user's input.
    Pattern Matching : Each alphabet corresponds to the integer between 2 to 9 inclusive.
    Abstraction : This function is also reusable for longer phone number.
    Automation with algorithms : I made lists in a list and assigned the value to each alphabet.

    :postcondition: check if the user entered phone number in the 'XXX-XXX-XXXX' format
    :return: call the function named number_translator_helper with the preprocessed input
    """
    # Accept the user's input and preprocess it
    user_input = input("Enter your alphabetical phone number with dashes(XXX-XXX-XXXX) : ")
    user_input = ''.join(user_input.upper().split())

    error_message = "You entered the wrong phone number. Try again :("
    # If the user's input does not fit the format, print the error message
    if len(user_input) != 12:
        print(f"{error_message}")
    # If the user's input is valid, call the function called number_translator_helper
    else:
        return number_translator_helper(user_input)


def number_translator_helper(user_input):
    """ Generate phone number equivalent to alphabetical number

    :param user_input:
    :precondition: user_input must be in "XXX-XXX-XXXX" format
    :precondition: user_input must not contain any special character except dashes
    :postcondition: convert the alphabetical phone number to numeric phone number
    :return: 10-digit phone number that correspond with alphabetical number which is the user's input

    >>> number_translator_helper('555-GET-THIN')
    '555-438-8446'
    >>> number_translator_helper('888-CAR-RENT')
    '888-227-7368'
    >>> number_translator_helper('555-GET-FOOD')
    '555-438-3663'
    """
    # Make a list of lists grouping the alphabets
    alphabet_list = [['A', 'B', 'C'], ['D', 'E', 'F'],
                     ['G', 'H', 'I'], ['J', 'K', 'L'],
                     ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
                     ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
    # Make the user's input as a list
    user_input_list = list(user_input)
    # Generate the phone number corresponding the alphabetical number
    for number in range(len(user_input_list)):
        for letter in range(len(alphabet_list)):
            if user_input_list[number] in alphabet_list[letter]:
                user_input_list[number] = str(letter + 2)
    # Make the list as a line of string
    result = ''.join(user_input_list)
    # Return the result as a string
    return result


def main():
    # Program starts here
    test = number_translator()
    print(test)


if __name__ == '__main__':
    # invoke the main function
    main()
