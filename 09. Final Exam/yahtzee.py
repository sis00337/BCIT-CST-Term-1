"""
COMP 1510
09. Final Exam - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


import random


def EMPTY_SCORE() -> int:
    """
    Return -1 to indicate a blank in a score sheet.

    :return: -1
    """
    return -1


def ZERO_SCORE() -> int:
    """
    Return 0 to indicate score zero.

    :return: 0
    """
    return 0


def FULL_HOUSE() -> int:
    """
    Return 25 to indicate the score of Full House.

    :return: 25
    """
    return 25


def SMALL_STRAIGHT() -> int:
    """
    Return 30 to indicate the score of Small straight.

    :return: 30
    """
    return 30


def LARGE_STRAIGHT() -> int:
    """
    Return 40 to indicate the score of Large straight.

    :return: 40
    """
    return 40


def BONUS_POINT() -> int:
    """
    Return 35 to indicate the score of Bonus point.

    :return: 35
    """
    return 35


def YAHTZEE() -> int:
    """
    Return 50 to indicate the score of Yahtzee.

    :return: 50
    """
    return 50


def YAHTZEE_BONUS() -> int:
    """
    Return 100 to indicate the score of Yahtzee Bonus.

    :return: 100
    """
    return 100


def REQUIREMENT_FOR_BONUS_POINT() -> int:
    """
    Return 63 to indicate the minimum score in upper section to get a bonus point.

    :return: 63
    """
    return 63


def MAX_ROLLS() -> int:
    """
    Return 3 to indicate the maximum number of chances that the player can roll dice.

    :return: 3
    """
    return 3


def INITIAL_DICE() -> int:
    """
    Return 0 to indicate the initial value of dice.

    :return: 0
    """
    return 0


def NUMBER_OF_DICE() -> int:
    """
    Return 5 to indicate the number of dice.

    :return: 5
    """
    return 5


def NUMBER_OF_COMBINATIONS() -> int:
    """
    Return 13 to indicate the number of combinations in the score sheet in Yahtzee game.

    :return: 13
    """
    return 13


def roll_dice(player_dice: list) -> None:
    """
    Generate random integers from 1 to 6 for as many as dices the player didn't keep (Out of max 5 dice).

    :param player_dice: a list that contains a list of dice the player wants to roll and a list of dice the player kept.
    :precondition: the length of player_dice must be 2
    :precondition: the sum of the length of player_dice[0] and player_dice[1] must be 5
    :post-condition: show a sorted list containing as many random numbers as the number of dice the player didn't keep
    :post-condition: show a list containing the dice that the player has kept
    :return: None
    """
    print('Press <ENTER> to roll dice.')
    input()
    player_dice[0] = [random.randint(1, 6) for _ in range(len(player_dice[0]))]
    print(f"{sorted(player_dice[0])}      Keeping Dice : {sorted(player_dice[1])}\n")


def select_dice_to_keep(player_dice: list) -> None:
    """
    Selects which dice the player wants to keep.

    :param player_dice: a list that contains a list of dice the player rolled and a list of dice the player kept.
    :precondition: the length of player_dice must be 2
    :precondition: the sum of the length of player_dice[0] and player_dice[1] must be 5
    :post-condition: If the player's input is valid, call the function named select_dice_to_keep_helper.
                     Otherwise, print the error message.
    :return: None
    """
    determinant = True
    while determinant:
        print(f"Current Dice : {sorted(player_dice[0])}")
        player_choice = input('Which dice do you want to keep? Separate by a comma. '
                              '(e.g. 3, 3 | 4, 4, 4 | 1, 2, 3, 4 | 1, 2, 3, 4, 5)\n'
                              'Press <ENTER> if you want to keep nothing.\n')
        if player_choice == "":
            determinant = False
        else:
            player_choice = ''.join(player_choice.split())
            player_choice = player_choice.split(',')
            try:
                determinant = select_dice_to_keep_helper(determinant, player_dice, player_choice)
            except ValueError:
                print('You entered the wrong input. Please try again.')


def select_dice_to_keep_helper(determinant: bool, player_dice: list, player_choice: list) -> bool:
    """
    Determine the dice set which the user wants to keep is valid.

    :param determinant: a boolean value that can determine where the while loop should break
    :param player_dice: a list that contains a list of dice the player rolled and a list of dice the player kept.
    :param player_choice: a list that contains the information of the player's input split by a comma
    :precondition: the initial value of determinant must be True
    :precondition: the length of player_dice must be 2
    :precondition: the sum of the length of player_dice[0] and player_dice[1] must be 5
    :precondition: the length of user_choice must be equal to or greater than 1
    :post-condition: If the player's input is valid,
                     the value of 'Current dice' and 'Keeping dice' will be updated and return False.
                     Otherwise, print the error message and return True.
    :return: True or False

    >>> deter = True
    >>> dice = [[1, 1, 2, 3, 3], []]
    >>> user_choice = [1, 1, 2, 2]
    >>> select_dice_to_keep_helper(deter, dice, user_choice)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [[1, 1, 2, 3, 3], []]
    >>> user_choice = [1, 1]
    >>> select_dice_to_keep_helper(deter, dice, user_choice)
    False
    >>> deter = True
    >>> dice = [[1, 1, 2], [3, 3]]
    >>> user_choice = [3, 3]
    >>> select_dice_to_keep_helper(deter, dice, user_choice)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [[1, 1, 2], [3, 3]]
    >>> user_choice = [1, 1, 2, 2]
    >>> select_dice_to_keep_helper(deter, dice, user_choice)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [[1, 1, 2], [3, 3]]
    >>> user_choice = [1, 1]
    >>> select_dice_to_keep_helper(deter, dice, user_choice)
    False
    """
    player_choice = list(map(int, player_choice))
    player_set = list(set(player_choice))
    count_dice_list = [player_dice[0].count(number) for number in player_set]
    count_player_list = [player_choice.count(number) for number in player_set]
    count_truth = [count_dice_list[number] < count_player_list[number] for number in range(len(count_dice_list[:]))]
    truth_list = [number in player_dice[0] for number in player_choice[:]]
    if False in truth_list or True in count_truth:
        print('You entered the wrong input. Please try again.')
    else:
        for item in player_choice[:]:
            player_dice[0].remove(item)
            player_dice[1].append(item)
        determinant = False
    return determinant


def select_dice_to_release(player_dice: list) -> None:
    """
    Release some dice from the keeping dice.

    :param player_dice: a list that contains a list of dice the player rolled and a list of dice the player kept.
    :precondition: the length of player_dice must be 2
    :precondition: the sum of the length of player_dice[0] and player_dice[1] must be 5
    :post-condition: If the player's input is valid, call the function named select_dice_to_release_helper.
                     Otherwise, print the error message.
    :return: None
    """
    determinant = True
    while determinant:
        print(f"Keeping Dice : {sorted(player_dice[1])}")
        player_choice = input('Which dice do you want to release? Separate by a comma. '
                              '(e.g. 3, 3 | 4, 4, 4 | 1, 2, 3, 4 | 1, 2, 3, 4, 5)\n'
                              'Press <ENTER> if you want to release nothing.\n')
        if player_choice == "":
            determinant = False
        else:
            player_choice = ''.join(player_choice.split())
            player_choice = player_choice.split(',')
            try:
                determinant = select_dice_to_release_helper(determinant, player_dice, player_choice)
            except ValueError:
                print('You entered the wrong input. Please try again.')


def select_dice_to_release_helper(determinant: bool, player_dice: list, player_choice: list) -> bool:
    """
    Determine the dice set which the user wants to release is valid.

    :param determinant: a boolean value that can determine where the while loop should break
    :param player_dice: a list that contains a list of dice the player wants to roll and a list of dice the player kept.
    :param player_choice: a list that contains the information of the player's input split by a comma
    :precondition: the length of player_dice must be 2
    :precondition: the sum of the length of player_dice[0] and player_dice[1] must be 5
    :precondition: the length of user_choice must be equal to or greater than 1
    :post-condition: If the player's input is valid,
                     the value of 'Current dice' and 'Keeping dice' will be updated and return False.
                     Otherwise, print the error message and return True.
    :return: True or False

    >>> deter = True
    >>> dice = [[1], [3, 3, 3, 3]]
    >>> user_choice = [3, 3]
    >>> select_dice_to_release_helper(deter, dice, user_choice)
    False
    >>> deter = True
    >>> dice = [[1], [3, 3, 3, 3]]
    >>> user_choice = [1, 3, 3]
    >>> select_dice_to_release_helper(deter, dice, user_choice)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [[1, 1], [3, 3, 4]]
    >>> user_choice = [3, 3]
    >>> select_dice_to_release_helper(deter, dice, user_choice)
    False
    >>> deter = True
    >>> dice = [[1, 5, 6], [2, 3]]
    >>> user_choice = [2, 2]
    >>> select_dice_to_release_helper(deter, dice, user_choice)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [[1, 5, 6], [2, 3]]
    >>> user_choice = [3]
    >>> select_dice_to_release_helper(deter, dice, user_choice)
    False
    >>> deter = True
    >>> dice = [[2, 3, 4, 5], [6]]
    >>> user_choice = [1]
    >>> select_dice_to_release_helper(deter, dice, user_choice)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [[2, 3, 4, 5], [6]]
    >>> user_choice = [6]
    >>> select_dice_to_release_helper(deter, dice, user_choice)
    False
    """
    player_choice = list(map(int, player_choice))
    player_set = list(set(player_choice))
    count_dice_list = [player_dice[1].count(number) for number in player_set]
    count_player_list = [player_choice.count(number) for number in player_set]
    count_truth = [count_dice_list[number] < count_player_list[number] for number in range(len(count_dice_list[:]))]
    truth_list = [number in player_dice[1] for number in player_choice[:]]
    if False in truth_list or True in count_truth:
        print('You entered the wrong input. Please try again.')
    else:
        for item in player_choice[:]:
            player_dice[1].remove(item)
            player_dice[0].append(item)
        determinant = False
    return determinant


def turn(player_name: str, player_dice: list, player_score: dict) -> None:
    """
    Make player roll the dice three times in each turn and show options after rolling dice

    :param player_name: a string that represents the player's name
    :param player_dice: a list that contains a list of dice the player rolled and a list of dice the player kept.
    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :precondition: every function in your_turn must be working correctly
    :post-condition: If the player chose number 1 from the options, the player will roll the dice again.
                     If the player chose 2, the player can keep some dice from the current dice or release
                     some dice from the keeping dice.
                     If the player chose 3, the player will mark the score sheet and pass the turn to the other player.
    :return: None
    """
    print(f"{player_name}'s turn.\n")
    for roll in range(MAX_ROLLS()):
        print(f'This is roll #{roll + 1}')
        roll_dice(player_dice)
        yahtzee_set = set(player_dice[0] + player_dice[1])
        if len(yahtzee_set) == 1:
            print(f"{'=' * 20}\nYAHTZEE\n{'=' * 20}")
        player_choice = options_at_every_roll(roll)
        if player_choice == 1:
            pass
        elif player_choice == 2:
            select_dice_to_keep(player_dice)
            select_dice_to_release(player_dice)
        elif player_choice == 3:
            mark_the_sheet(player_dice, player_score)
            break


def options_at_every_roll(roll: int) -> int:
    """
    Check if the player rolled the dice one more time, keep some dice, or select the combination at every roll.

    :param roll: an integer that indicates the number of counts of rolls
    :precondition: roll must be an integer between 0 to 2 inclusive
    :post-condition: If the player's input is valid, return the input as an integer.
                     Otherwise, print an error message.
    :return: an integer corresponding to the player's input
    """
    while True:
        print('What do you want to do??')
        player_choice = input("1) Roll the dice one more time\n"
                              "2) Keep or Release some dice\n"
                              "3) Select a combination\n")
        player_choice = player_choice.strip()
        if roll == 0 or roll == 1:
            if player_choice in ['1', '2', '3']:
                return int(player_choice)
        elif roll == 2:
            if player_choice in ['1', '2']:
                print('This is 3rd roll.')
                print('You cannot roll or keep the dice more. Please select a combination.\n')
            elif player_choice == '3':
                return int(player_choice)
        if player_choice not in ['1', '2', '3']:
            print('You entered the wrong input. Please try again.\n')


def mark_the_sheet(player_dice: list, player_score: dict) -> None:
    """
    Let user choose a combination from the current dice roll.

    :param player_dice: a list that contains a list of dice the player rolled and a list of dice the player kept.
    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :precondition: the length of player_dice must be 2
    :precondition: the sum of the length of player_dice[0] and player_dice[1] must be 5
    :post-condition: show the player the numbered list of the combination in Yahtzee game and
                     call the function called upper_or_lower_section
    :return: None
    """
    upper_section = ('Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes')
    lower_section = ('Three of a kind', 'Four of a kind', 'Full House', 'Small straight',
                     'Large straight', 'Chance', 'YAHTZEE')
    print(f"Your Dice : {sorted(player_dice[0] + player_dice[1])}")
    print('*' * 15 + ' UPPER SECTION ' + '*' * 15)
    for number in range(len(upper_section)):
        print(f'{number + 1}. {upper_section[number]}')
    print('*' * 15 + ' LOWER SECTION ' + '*' * 15)
    for number in range(len(lower_section)):
        print(f'{number + 7}. {lower_section[number]}')
    choose_a_combination(player_dice, player_score)


def choose_a_combination(player_dice: list, player_score: dict) -> None:
    """
    Get the player's choice equivalent to which combination the player wants to use and calculate the score.

    :param player_dice: a list that contains a list of dice the player rolled and a list of dice the player kept.
    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :precondition: the length of player_dice must be 2
    :precondition: the sum of the length of player_dice[0] and player_dice[1] must be 5
    :post-condition: If the player's input is valid, call the function called choose_a_combination_helper.
                     Otherwise, print an error message.
    :return: None
    """
    determinant = True
    while determinant:
        mark_choice = input('Choose a number above that you want to use as a combination:\n')
        mark_choice = mark_choice.strip()
        try:
            dice_list = player_dice[0] + player_dice[1]
            mark_choice = int(mark_choice)
            determinant = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        except ValueError:
            print('You entered the wrong input. Please try again.')


def choose_a_combination_helper(determinant: bool, dice_list: list, mark_choice: int, player_score: dict) -> bool:
    """
    Calculate the combination depending on the player's choice.

    :param determinant: a boolean value that can determine where the while loop should break
    :param dice_list: a list that contains the spot of each 5 dice
    :param mark_choice: an integer form of the player's input
    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :precondition: the initial value of determinant must be True
    :precondition: the length of dice_list must be 5
    :precondition: mark_choice must be an integer corresponding to the player's input
    :precondition: the initial value of every value in player_score must be -1
    :post-condition: call the function that calculates the combination depending on the player's choice
    :post-condition: return the value from the function that the player chose
    :return: True or False

    >>> deter = True
    >>> dice = [1, 1, 1, 1, 5]
    >>> player_choice = 0
    >>> player = {'Aces': -1}
    >>> choose_a_combination_helper(deter, dice, player_choice, player)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [1, 1, 1, 1, 5]
    >>> player_choice = 14
    >>> player = {'Aces': -1}
    >>> choose_a_combination_helper(deter, dice, player_choice, player)
    You entered the wrong input. Please try again.
    True
    >>> deter = True
    >>> dice = [1, 1, 1, 1, 5]
    >>> player_choice = 1
    >>> player = {'Aces': -1}
    >>> choose_a_combination_helper(deter, dice, player_choice, player)
    False
    >>> deter = True
    >>> dice = [1, 1, 1, 1, 5]
    >>> player_choice = 1
    >>> player = {'Aces': 0}
    >>> choose_a_combination_helper(deter, dice, player_choice, player)
    You have already chosen [Aces] before. Please try again.
    True
    >>> deter = True
    >>> dice = [1, 1, 1, 1, 5]
    >>> player_choice = 8
    >>> player = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
    ... 'Three of a kind': 24, 'Four of a kind': -1, 'Full House': 25, 'Small straight': 30,
    ... 'Large straight': 40, 'Chance': 20, 'Yahtzee': 1}
    >>> choose_a_combination_helper(deter, dice, player_choice, player)
    False
    >>> deter = True
    >>> dice = [1, 1, 1, 1, 5]
    >>> player_choice = 8
    >>> player = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
    ... 'Three of a kind': 24, 'Four of a kind': 0, 'Full House': 25, 'Small straight': 30,
    ... 'Large straight': 40, 'Chance': 20, 'Yahtzee': 1}
    >>> choose_a_combination_helper(deter, dice, player_choice, player)
    You have already chosen [Four of a kind] before. Please try again.
    True
    """
    function_list = [is_three_of_a_kind, is_four_of_a_kind, is_full_house, is_small_straight,
                     is_large_straight, is_chance, is_yahtzee]
    if mark_choice < 1 or mark_choice > 13:
        print('You entered the wrong input. Please try again.')
    elif 1 <= mark_choice <= 6:
        determinant = is_upper_section(player_score, mark_choice, dice_list)
    for number in range(7, 14):
        if mark_choice == number:
            determinant = function_list[number - 7](player_score, dice_list)
    return determinant


def is_chance(player_score: dict, dice_list: list) -> bool:
    """
    Confirm that the player has not chosen Chance as a combination and
    calculate the sum of all the spots on the current dice.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: the initial value of every value in player_score must be -1
    :predondition: player_score must have a key called 'Chance'
    :precondition: dice_list must contains 5 integers that indicate the spots on the dice (1 - 6 inclusive)
    :post-condition: If the player has not chosen the combination called 'Chance' yet,
                     calculate the score and return False.
                     If the player has already chosen 'Chance' before, print an error message and return True.
    :return: True or False

    >>> dice = [1, 2, 3, 4, 5]
    >>> player_dict = {'Chance': -1}
    >>> is_chance(player_dict,dice)
    False
    >>> dice = [1, 2, 3, 4, 5]
    >>> player_dict = {'Chance': 0}
    >>> is_chance(player_dict,dice)
    You have already chosen [Chance] before. Please try again.
    True
    >>> dice = [1, 1, 1, 1, 1]
    >>> player_dict = {'Chance': -1}
    >>> is_chance(player_dict,dice)
    False
    >>> dice = [1, 1, 1, 1, 1]
    >>> player_dict = {'Chance': 'ABC'}
    >>> is_chance(player_dict,dice)
    You have already chosen [Chance] before. Please try again.
    True
     >>> dice = [6, 6, 6, 6, 6]
    >>> player_dict = {'Chance': 234567}
    >>> is_chance(player_dict,dice)
    You have already chosen [Chance] before. Please try again.
    True
    """
    if player_score['Chance'] != EMPTY_SCORE():
        print('You have already chosen [Chance] before. Please try again.')
        return True
    else:
        player_score['Chance'] = sum(dice_list)
        return False


def is_upper_section(player_score: dict, mark_choice: int, dice_list: list) -> bool:
    """
    Calculate Aces, Twos, Threes, Fours, Fives, or Sixes depending on the player's input.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param mark_choice: an integer that corresponds the player's input from upper_or_lower_section
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: player_score must have six keys.
    :precondition: the initial value of every value in player_score must be -1
    :precondition: mark_choice must be an integer between 1 to 6 inclusive
    :precondition: dice_list must contains 5 integers that indicate the spots on the dice (1 - 6 inclusive)
    :post-condition: If the player has not chosen the combination that matches to mark_choice yet,
                     calculate the score, store the score as a value of key, and return False.
                     If the player has already chosen the combination, print an error message and return True.
    :return: True or False

    >>> score = {1: -1, 2: -1, 3: 12, 4: -1, 5: -1, 6: -1}
    >>> player_choice = 3
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_upper_section(score, player_choice, dice)
    You have already chosen [3] before. Please try again.
    True
    >>> score = {'Ace': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1}
    >>> player_choice = 1
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_upper_section(score, player_choice, dice)
    False
    >>> score = {'Ace': -1, 'Twos': 6, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1}
    >>> player_choice = 2
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_upper_section(score, player_choice, dice)
    You have already chosen [Twos] before. Please try again.
    True
    >>> score = {'a': 'abc', 'b': 6, 'c': 3, 'd': 'super', 'e': -1, 'f': 'man'}
    >>> player_choice = 5
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_upper_section(score, player_choice, dice)
    False
    """
    score_keys = list(player_score.keys())
    for index in range(len(score_keys[:])):
        if index == (mark_choice - 1) and player_score[score_keys[index]] == EMPTY_SCORE():
            player_score[score_keys[index]] = dice_list.count(mark_choice) * mark_choice
            return False
        elif index == (mark_choice - 1) and player_score[score_keys[index]] != EMPTY_SCORE():
            print(f"You have already chosen [{score_keys[index]}] before. Please try again.")
            return True


def is_full_house(player_score: dict, dice_list: list) -> bool:
    """
    Calculate Full House depending on the current dice.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: player_score must have a key called 'Full House'
    :precondition: the initial value of every value in player_score must be -1
    :precondition: dice_list must contains 5 integers that indicate the spots on the dice (1 - 6 inclusive)
    :post-condition: If the player has not chosen the combination called 'Full House' yet,
                     calculate the score and return False.
                     If the player has already chosen 'Full House' before, print an error message and return True.
    :return: True or False

    >>> score = {'Full House': -1}
    >>> number_list = [1, 0, 2, 1, 1, 1]
    >>> is_full_house(score, number_list)
    False
    >>> score = {'Full House': -1}
    >>> number_list = [2, 3, 0, 0, 0, 0]
    >>> is_full_house(score, number_list)
    False
    >>> score = {'Full House': 25}
    >>> number_list = [2, 3, 0, 0, 0, 0]
    >>> is_full_house(score, number_list)
    You have already chosen [Full House] before. Please try again.
    True
    >>> score = {'Full House': -1, 1: 'ABC', 2: '123', 3: 678}
    >>> number_list = [2, 3, 0, 0, 0, 0]
    >>> is_full_house(score, number_list)
    False
    >>> score = {'Full House': 0, 1: 'ABC', 2: '123', 3: 678}
    >>> number_list = [2, 3, 0, 0, 0, 0]
    >>> is_full_house(score, number_list)
    You have already chosen [Full House] before. Please try again.
    True
    """
    same_number_list = [dice_list.count(number) for number in range(1, 7)]
    if player_score['Full House'] != EMPTY_SCORE():
        print("You have already chosen [Full House] before. Please try again.")
        return True
    elif 2 in same_number_list and 3 in same_number_list:
        player_score['Full House'] = FULL_HOUSE()
        return False
    elif 2 not in same_number_list or 3 not in same_number_list:
        player_score['Full House'] = ZERO_SCORE()
        return False


def is_four_of_a_kind(player_score: dict, dice_list: list) -> bool:
    """
    Confirm that the player has not chosen Four of a kind as a combination and
    calculate Four of a kind depending on the current dice.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: player_score must have a key called 'Four of a kind'
    :precondition: the initial value of every value in player_score must be -1
    :precondition: dice_list must contains 5 integers that indicate the spots on the dice (1 - 6 inclusive)
    :post-condition: If the player has not chosen the combination called 'Four of a kind' yet,
                     calculate the score and return False.
                     If the player has already chosen 'Four of a kind' before, print an error message and return True.
    :return: True or False

    >>> score = {'Four of a kind': -1}
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_four_of_a_kind(score, dice)
    False
    >>> score = {'Four of a kind': -1}
    >>> dice = [4, 4, 4, 4, 6]
    >>> is_four_of_a_kind(score, dice)
    False
    >>> score = {'Four of a kind': 25}
    >>> dice = [1, 1, 1, 1, 5]
    >>> is_four_of_a_kind(score, dice)
    You have already chosen [Four of a kind] before. Please try again.
    True
    >>> score = {'Four of a kind': -1, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [6, 6, 6, 6, 6]
    >>> is_four_of_a_kind(score, dice)
    False
    >>> score = {'Four of a kind': 0, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [2, 3, 4, 5, 6]
    >>> is_four_of_a_kind(score, dice)
    You have already chosen [Four of a kind] before. Please try again.
    True
    """
    same_number_list = [dice_list.count(number) for number in range(1, 7)]
    if player_score['Four of a kind'] != EMPTY_SCORE():
        print("You have already chosen [Four of a kind] before. Please try again.")
        return True
    elif (4 or 5) in same_number_list:
        player_score['Four of a kind'] = sum(dice_list)
        return False
    elif (4 or 5) not in same_number_list:
        player_score['Four of a kind'] = ZERO_SCORE()
        return False


def is_three_of_a_kind(player_score: dict, dice_list: list) -> bool:
    """
    Confirm that the player has not chosen Three of a kind as a combination and
    calculate Three of a kind depending on the current dice.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: player_score must have a key called 'Three of a kind'
    :precondition: the initial value of every value in player_score must be -1
    :precondition: dice_list must contains 5 integers that indicate the spots on the dice (1 - 6 inclusive)
    :post-condition: If the player has not chosen the combination called 'Three of a kind' yet,
                     calculate the score and return False.
                     If the player has already chosen 'Three of a kind' before, print an error message and return True.
    :return: True or False

    >>> score = {'Three of a kind': -1}
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_three_of_a_kind(score, dice)
    False
    >>> score = {'Three of a kind': -1}
    >>> dice = [4, 4, 4, 4, 6]
    >>> is_three_of_a_kind(score, dice)
    False
    >>> score = {'Three of a kind': 25}
    >>> dice = [1, 1, 1, 1, 5]
    >>> is_three_of_a_kind(score, dice)
    You have already chosen [Three of a kind] before. Please try again.
    True
    >>> score = {'Three of a kind': -1, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [6, 6, 6, 6, 6]
    >>> is_three_of_a_kind(score, dice)
    False
    >>> score = {'Three of a kind': 0, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [2, 3, 4, 5, 6]
    >>> is_three_of_a_kind(score, dice)
    You have already chosen [Three of a kind] before. Please try again.
    True
    """
    same_number_list = [dice_list.count(number) for number in range(1, 7)]
    if player_score['Three of a kind'] != EMPTY_SCORE():
        print("You have already chosen [Three of a kind] before. Please try again.")
        return True
    elif (3 or 4 or 5) in same_number_list:
        player_score['Three of a kind'] = sum(dice_list)
        return False
    elif (3 or 4 or 5) not in same_number_list:
        player_score['Three of a kind'] = ZERO_SCORE()
        return False


def is_large_straight(player_score: dict, dice_list: list) -> bool:
    """
    Confirm that the player has not chosen Large straight as a combination and
    calculate Large straight depending on depending on the player's input.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: player_score must have a key called 'Large straight'
    :precondition: the initial value of every value in player_score must be -1
    :precondition: dice_list must contain 5 integers that are between 1 to 6 inclusive
    :post-condition: If the player has not chosen the combination called 'Large straight' yet,
                     calculate the score and return False.
                     If the player has already chosen 'Large straight' before, print an error message and return True.
    :return: True or False

    >>> score = {'Large straight': -1}
    >>> dice = [1, 1, 1, 1, 1]
    >>> is_large_straight(score, dice)
    False
    >>> score = {'Large straight': -1}
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_large_straight(score, dice)
    False
    >>> score = {'Large straight': 40}
    >>> dice = [1, 2, 3, 4, 6]
    >>> is_large_straight(score, dice)
    You have already chosen [Large straight] before. Please try again.
    True
    >>> score = {'Large straight': -1, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [2, 3, 3, 5, 6]
    >>> is_large_straight(score, dice)
    False
    >>> score = {'Large straight': 0, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [2, 3, 4, 5, 6]
    >>> is_large_straight(score, dice)
    You have already chosen [Large straight] before. Please try again.
    True
    """
    dice_set = set(sorted(dice_list))
    if player_score['Large straight'] != EMPTY_SCORE():
        print("You have already chosen [Large straight] before. Please try again.")
        return True
    elif {1, 2, 3, 4, 5} == {1, 2, 3, 4, 5}.intersection(dice_set):
        player_score['Large straight'] = LARGE_STRAIGHT()
        return False
    elif {2, 3, 4, 5, 6} == {2, 3, 4, 5, 6}.intersection(dice_set):
        player_score['Large straight'] = LARGE_STRAIGHT()
        return False
    else:
        player_score['Large straight'] = ZERO_SCORE()
        return False


def is_small_straight(player_score: dict, dice_list: list) -> bool:
    """
    Confirm that the player has not chosen Small straight as a combination and
    calculate Small straight depending on depending on the player's input.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: player_score must have a key called 'Small straight'
    :precondition: the initial value of every value in player_score must be -1
    :precondition: dice_list must contain 5 integers that are between 1 to 6 inclusive
    :post-condition: If the player has not chosen the combination called 'Small straight' yet,
                     calculate the score and return False.
                     If the player has already chosen 'Small straight' before, print an error message and return True.
    :return: True or False

    >>> score = {'Small straight': -1}
    >>> dice = [1, 1, 1, 1, 1]
    >>> is_small_straight(score, dice)
    False
    >>> score = {'Small straight': -1}
    >>> dice = [1, 2, 3, 4, 5]
    >>> is_small_straight(score, dice)
    False
    >>> score = {'Small straight': 40}
    >>> dice = [1, 2, 3, 4, 6]
    >>> is_small_straight(score, dice)
    You have already chosen [Small straight] before. Please try again.
    True
    >>> score = {'Small straight': -1, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [2, 3, 3, 5, 6]
    >>> is_small_straight(score, dice)
    False
    >>> score = {'Small straight': 0, 1: 'ABC', 2: '123', 3: 678}
    >>> dice = [2, 3, 4, 5, 6]
    >>> is_small_straight(score, dice)
    You have already chosen [Small straight] before. Please try again.
    True
    """
    dice_set = set(sorted(dice_list))
    if player_score['Small straight'] != EMPTY_SCORE():
        print("You have already chosen [Small straight] before. Please try again.")
        return True
    elif {1, 2, 3, 4} == {1, 2, 3, 4}.intersection(dice_set):
        player_score['Small straight'] = SMALL_STRAIGHT()
        return False
    elif {2, 3, 4, 5} == {2, 3, 4, 5}.intersection(dice_set):
        player_score['Small straight'] = SMALL_STRAIGHT()
        return False
    elif {3, 4, 5, 6} == {3, 4, 5, 6}.intersection(dice_set):
        player_score['Small straight'] = SMALL_STRAIGHT()
        return False
    else:
        player_score['Small straight'] = ZERO_SCORE()
        return False


def is_yahtzee(player_score: dict, dice_list: list) -> bool:
    """
    Determine whether the current dice is yahtzee or not and calculate Yahtzee.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :param dice_list: a list containing currently rolled dice and kept dice by the player
    :precondition: player_score must have a key called 'Yahtzee'
    :precondition: the initial value of every value in player_score must be -1
    :precondition: dice_list must contains 5 integers that indicate the spots on the dice (1 - 6 inclusive)
    :post-condition: If the player got the 5 same numbers of dice and if the player has not chosen the combination
                     called 'Yahtzee' yet, assign 1 as the value of key 'Yahtzee' and return False.
                     If the player got the 5 same numbers of dice and if the player has already chosen 'Yahtzee' before,
                     add 1 to the value of key 'Yahtzee' and return False.
                     Otherwise, assign 0 as the value of key 'Yahtzee' and return False.
    :return: False

    >>> dice = [1, 2, 3, 4, 5]
    >>> player_dict = {'Yahtzee': -1}
    >>> is_yahtzee(player_dict, dice)
    False
    >>> dice = [1, 2, 3, 4, 5]
    >>> player_dict = {'Yahtzee': 1}
    >>> is_yahtzee(player_dict, dice)
    False
    >>> dice = [1, 1, 1, 1, 1]
    >>> player_dict = {'Yahtzee': -1}
    >>> is_yahtzee(player_dict, dice)
    False
    >>> dice = [1, 1, 1, 1, 1]
    >>> player_dict = {'Yahtzee': 2, '1': 999, 'Aces': 5}
    >>> is_yahtzee(player_dict, dice)
    False
     >>> dice = [6, 6, 6, 6, 6]
    >>> player_dict = {'Yahtzee': 5, 1: 'ABC', 2: 345}
    >>> is_yahtzee(player_dict, dice)
    False
    """
    same_number_list = [dice_list.count(number) for number in range(1, 7)]
    if 5 in same_number_list and player_score['Yahtzee'] == EMPTY_SCORE():
        player_score['Yahtzee'] = 1
    elif 5 in same_number_list and player_score['Yahtzee'] >= 1:
        player_score['Yahtzee'] += 1
    else:
        player_score['Yahtzee'] = ZERO_SCORE()
    return False


def sum_score(player_score: dict) -> int:
    """
    Calculate the sum of the scores.

    :param player_score: a dictionary that contains the categories on the Yahtzee score card as keys
                         and the value of each categories as values
    :precondition: every value in player_score must be an integer that is equal to or greater than 0
    :precondition: player_score must have at least one key-value combination
    :post-condition: calculate the sum of the scores and return the value as an integer
    :post-condition: If sum of values of first six keys in player_score is equal to or greater than 63,
                     add 35 to the sum of scores.
    :return: an integer corresponding the sum of the scores

    >>> player_dict = {1: 1, 2: 2, 3: 3, 'AB': 4}
    >>> sum_score(player_dict)
    10
    >>> player_dict = {'ab': 10, 2: 20, 'Small Straight': 30, 'AB': 40}
    >>> sum_score(player_dict)
    135
    >>> player_dict = {'ab': 0, 2: 0, 'Small Straight': 0, 'AB': 0}
    >>> sum_score(player_dict)
    0
    >>> player_dict = {'ab': 100}
    >>> sum_score(player_dict)
    135
    >>> player_dict = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 12, 'Fives': 20, 'Sixes': 24, 'Full House': 25}
    >>> sum_score(player_dict)
    137
    """
    sum_result = []
    for key, value in player_score.items():
        if key != 'Yahtzee':
            sum_result.append(value)
        elif key == 'Yahtzee' and value == 1:
            sum_result.append(value * YAHTZEE())
        elif key == 'Yahtzee' and value >= 2:
            sum_result.append(YAHTZEE() + (value - 1) * YAHTZEE_BONUS())
    if sum(sum_result[0:6]) >= REQUIREMENT_FOR_BONUS_POINT():
        result = sum(sum_result) + BONUS_POINT()
        return result
    else:
        return sum(sum_result)


def create_player() -> tuple:
    """
    Create the players' name by getting the input from the user.

    :post-condition: return the player's inputs as strings that all leading and trailing spaces removed
    :return: a tuple that contains strings that correspond to the user's inputs
    """
    player_1_name = input("Please enter the name for 1st player: \n")
    player_1_name = player_1_name.strip()
    player_2_name = input("Please enter the name for 2nd player: \n")
    player_2_name = player_2_name.strip()
    return player_1_name, player_2_name


def initialize_player_score() -> dict:
    """
    Create a score sheet like in the Yahtzee game as a dictionary.

    :post-condition: return a dictionary that represents a score sheet in the Yahtzee game with an initial value of -1
    :return: a dictionary that contains the categories on the Yahtzee score card as keys
             and the value of each categories as values

    >>> initialize_player_score()
    {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Three of a kind': -1, \
'Four of a kind': -1, 'Full House': -1, 'Small straight': -1, 'Large straight': -1, 'Chance': -1, 'Yahtzee': -1}
    """
    score_list = ('Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Three of a kind', 'Four of a kind',
                  'Full House', 'Small straight', 'Large straight', 'Chance', 'Yahtzee')
    initial_score_data = [EMPTY_SCORE() for _ in range(NUMBER_OF_COMBINATIONS())]
    player_score = dict(zip(score_list, initial_score_data))
    return player_score


def yahtzee() -> None:
    """
    Execute the Yahtzee game.

    :precondition: the functions that are used in yahtzee must be correctly working
    :post-condition: execute the Yahtzee game
    :return: None
    """
    player_1_name, player_2_name = create_player()
    player_1_score, player_2_score = initialize_player_score(), initialize_player_score()
    while EMPTY_SCORE() in list(player_1_score.values()) and EMPTY_SCORE() in list(player_2_score.values()):
        player_1_dice = [[INITIAL_DICE() for _ in range(NUMBER_OF_DICE())], []]
        player_2_dice = [[INITIAL_DICE() for _ in range(NUMBER_OF_DICE())], []]
        turn(player_1_name, player_1_dice, player_1_score)
        turn(player_2_name, player_2_dice, player_2_score)
    more_than_two_yahtzee(player_1_name, player_2_name, player_1_score, player_2_score)
    show_result(player_1_name, player_2_name, player_1_score, player_2_score)


def show_result(player_1_name: str, player_2_name: str, player_1_score: dict, player_2_score: dict) -> None:
    """
    Show the game result and who the winner is.

    :param player_1_name: a string that represents the name defined by the first player
    :param player_2_name: a string that represents the name defined by the second player
    :param player_1_score: a dictionary that represents the first player's score sheet of the Yahtzee game
    :param player_2_score: a dictionary that represents the second player's score sheet of the Yahtzee game
    :precondition: the function that is used in more_than_two_yahtzee must be correctly working.
    :precondition: All values in player_1_score and player_2_score must be an integer that is equal to or greater than 0
    :precondition: player_1_score and player_2_score must have at least one key-value combination
    :postcondition: show the game result and who the winner is
    :return: None

    >>> player_1 = 'Ken'
    >>> player_2 = 'Sandy'
    >>> player_1_sheet = {1: 1, 2: 2, 3: 3, 'AB': 4}
    >>> player_2_sheet = {'ab': 10, 2: 20, 'Small Straight': 30, 'AB': 40}
    >>> show_result(player_1, player_2, player_1_sheet, player_2_sheet)
    Ken : 10
    Sandy : 135
    Congratulation!!! The winner is Sandy!!!
    >>> player_1 = 'Ken'
    >>> player_2 = 'Sandy'
    >>> player_1_sheet = {'ab': 10, 2: 20, 'Small Straight': 30, 'AB': 40}
    >>> player_2_sheet = {'ab': 100}
    >>> show_result(player_1, player_2, player_1_sheet, player_2_sheet)
    Ken : 135
    Sandy : 135
    It was a tie game...
    >>> player_1 = 'Ken'
    >>> player_2 = 'Sandy'
    >>> player_1_sheet = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 12, 'Fives': 20, 'Sixes': 24, 'Full House': 25}
    >>> player_2_sheet = {'ab': 100}
    >>> show_result(player_1, player_2, player_1_sheet, player_2_sheet)
    Ken : 137
    Sandy : 135
    Congratulation!!! The winner is Ken!!!
    >>> player_1 = 'Ken'
    >>> player_2 = 'Sandy'
    >>> player_1_sheet = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 24,
    ... 'Three of a kind': 24, 'Four of a kind': 24, 'Full House': 25, 'Small straight': 30, 'Large straight': 40,
    ... 'Chance': 24, 'Yahtzee': 1}
    >>> player_2_sheet = {'Aces': 2, 'Twos': 4, 'Threes': 6, 'Fours': 8, 'Fives': 10, 'Sixes': 12,
    ... 'Three of a kind': 0, 'Four of a kind': 0, 'Full House': 25, 'Small straight': 0, 'Large straight': 40,
    ... 'Chance': 20, 'Yahtzee': 0}
    >>> show_result(player_1, player_2, player_1_sheet, player_2_sheet)
    Ken : 333
    Sandy : 127
    Congratulation!!! The winner is Ken!!!
    """
    print(f"{player_1_name} : {sum_score(player_1_score)}")
    print(f"{player_2_name} : {sum_score(player_2_score)}")
    if sum_score(player_1_score) < sum_score(player_2_score):
        print(f"Congratulation!!! The winner is {player_2_name}!!!")
    elif sum_score(player_2_score) < sum_score(player_1_score):
        print(f"Congratulation!!! The winner is {player_1_name}!!!")
    else:
        print('It was a tie game...')


def more_than_two_yahtzee(player_1_name: str, player_2_name: str, player_1_score: dict, player_2_score: dict) -> None:
    """
    Check if one of the players got two or more Yahtzee. If so, allow the player to finish the game.

    :param player_1_name: a string that represents the name defined by the first player
    :param player_2_name: a string that represents the name defined by the second player
    :param player_1_score: a dictionary that represents the first player's score sheet of the Yahtzee game
    :param player_2_score: a dictionary that represents the second player's score sheet of the Yahtzee game
    :precondition: the function that is used in more_than_two_yahtzee must be correctly working.
    :post-condition: continue the game until the player who got two or more Yahtzee is done.
    :return: None
    """
    while EMPTY_SCORE() in list(player_2_score.values()):
        player_2_dice = [[INITIAL_DICE() for _ in range(NUMBER_OF_DICE())], []]
        turn(player_2_name, player_2_dice, player_2_score)
    while EMPTY_SCORE() in list(player_1_score.values()):
        player_1_dice = [[INITIAL_DICE() for _ in range(NUMBER_OF_DICE())], []]
        turn(player_1_name, player_1_dice, player_1_score)


def main() -> None:
    """
    Drives the program.
    """
    # import doctest
    # doctest.testmod(verbose=True)
    print(f"{'=' * 51}\nWELCOME TO THE YAHTZEE WORLD!!\n{'=' * 51}")
    yahtzee()


if __name__ == '__main__':
    main()
