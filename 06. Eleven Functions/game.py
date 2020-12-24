"""
Function 5 - Rock, Paper, Scissors!
Name : Min Soo (Mike) HWANG
Github ID : Delivery_KiKi
"""

import random


def rock_paper_scissors():
    """ Prompt user for the user's choice to play the rock, paper, scissors game.

    The function also check whether the user entered 'rock', 'paper', or 'scissors'.
    The user's input is case-insensitive and it might contain whitespaces.

    Decomposition : I decomposed one function into two functions only for the user's input.
    Pattern Matching : The rock, paper, scissors game has a regularity (scissors > paper > rock > scissors).
    Abstraction : This function is reusable for making a game with three elements.
    Automation with algorithms : I gave the number on 'rock', 'paper', and 'scissors and compared with a random number.

    :postcondition: check whether the user entered 'rock', 'paper', or 'scissors'
    :return: invoke the function named game_helper with the preprocessed input
    """
    # Accept the user's input and preprocess it
    user_input = input("Choose rock, paper, or scissors! : ")
    user_input = ''.join(user_input.lower().split())
    # Make a list of 'rock', 'paper', and 'scissors'
    game_list = ['rock', 'paper', 'scissors']
    error_message = "You entered the wrong input. Try again :("
    # Assign a number of 0, 1, and 2 to 'rock', 'paper', and 'scissors' respectively
    if user_input in game_list:
        if user_input == 'rock':
            user_input = 0
        elif user_input == 'paper':
            user_input = 1
        elif user_input == 'scissors':
            user_input = 2
    # If the user's input is not either 'rock', 'paper' or 'scissors', print the error message
    else:
        print(f"{error_message}")

    # If the user's input is valid, call the function called random_int
    return random_int(user_input)


def random_int(user_input):
    """ Generate a random number

    :param user_input: an integer in a range of 0 to 2 inclusive
    :precondition: user_input must be 0, 1, or 2
    :postcondition: generate a random integer among 0, 1, and 2
    :return: call the function named game_helper with the user's input and randomized number
    """
    # Randomly generate a number from 0 to 2 inclusive
    random_number = random.randint(0, 2)
    # Call the function called game_helper
    return game_helper(user_input, random_number)


def game_helper(user_input, random_number):
    """ Play rock, paper, scissors game based on the user's input and randomly chosen value by the computer.

    The function will show whether the user lost or won and the computer's choice.

    :param user_input: an integer which is 0, 1, or 2
    :param random_number: an integer which is 0, 1, or 2
    :precondition: user_input and random_number must be 0, 1, or 2
    :postcondition: play rock, paper, scissors game and show whether the user lost or not
    :return: nothing

    >>> game_helper(0, 2)
    Computer's choice was scissors.
    You won!!
    >>> game_helper(1, 1)
    Computer's choice was paper.
    It was a tie. Try one more time!
    >>> game_helper(2, 0)
    Computer's choice was rock.
    You lost :(
    """
    # Make a list of 'rock', 'paper', and 'scissors'
    game_list = ['rock', 'paper', 'scissors']
    # Play the game
    if user_input == 0 and random_number == 0:
        print(f"Computer's choice was {game_list[0]}. \nIt was a tie. Try one more time!")
    elif user_input == 0 and random_number == 1:
        print(f"Computer's choice was {game_list[1]}.\nYou lost :(")
    elif user_input == 0 and random_number == 2:
        print(f"Computer's choice was {game_list[2]}.\nYou won!!")

    if user_input == 1 and random_number == 0:
        print(f"Computer's choice was {game_list[0]}.\nYou won!!")
    elif user_input == 1 and random_number == 1:
        print(f"Computer's choice was {game_list[1]}.\nIt was a tie. Try one more time!")
    elif user_input == 1 and random_number == 2:
        print(f"Computer's choice was {game_list[2]}.\nYou lost :(")

    if user_input == 2 and random_number == 0:
        print(f"Computer's choice was {game_list[0]}.\nYou lost :(")
    elif user_input == 2 and random_number == 1:
        print(f"Computer's choice was {game_list[1]}.\nYou won!!")
    elif user_input == 2 and random_number == 2:
        print(f"Computer's choice was {game_list[2]}.\nIt was a tie. Try one more time!")


def main():
    # Program starts here
    rock_paper_scissors()


if __name__ == '__main__':
    # invoke the main function
    main()
