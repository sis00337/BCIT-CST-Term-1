"""
SUD Game
Contributor 1: Min Soo Hwang
Contributor 2: JoonHyeong Kim
"""

import random


def game():
    """ Run the game until the goal is achieved or the player died.

    :return: no return
    """
    character = make_character()
    if character[0] == 'QUIT':
        print("\nYou quit the game.\n\nGame Ended")
        quit()
    move_character(character[1])

    achieved_goal = False
    while not achieved_goal:
        direction = get_user_choice()
        if direction == 'quit':
            print("\nYou quit the game.\n\nGame Ended")
            quit()
        valid_move = validate_move(direction, character)
        print(f"Your HP : {character[2]}")

        alien = monster(random.randint(1, 4))
        if valid_move:
            move_character(character[1])
            check_for_monsters(alien, character)
        else:
            print("You cannot go there :(")


def check_for_monsters(monster_info, character_info):
    """ Check if there is a monster in where you moved to.

    :param monster_info: a list of monster information
    :param character_info: a list of monster information
    :precondition: The arguments must be lists in correct format
    :post-condition: Do not meet a monster with 75% probability, meet a monster with 75% probability
    :retrun: no return
    """
    probability = random.randint(1, 4)
    if probability == 1:
        print(f"You met a {monster_info[0]}!!\n")
        flee_or_fight(character_info, monster_info)
    else:
        print("You didn't meet any aliens~~\n")
        character_info[2] += 2
        if character_info[2] > 10:
            character_info[2] = 10
        return False


def monster(monster_pick):
    """ Identify which monster the play monster_hit.

    :param monster_pick: a random number between 1 to 4 inclusive
    :post-condition: pick a random monster and return it
    :return: a random monster

    >>> monster(1)
    ['Big Alien', 5]
    >>> monster(2)
    ['Small Alien', 4]
    >>> monster(3)
    ['Evolved Bacteria', 3]
    >>> monster(4)
    ['Bacteria', 2]
    """

    if monster_pick == 1:
        return ['Big Alien', 5]
    elif monster_pick == 2:
        return ['Small Alien', 4]
    elif monster_pick == 3:
        return ['Evolved Bacteria', 3]
    elif monster_pick == 4:
        return ['Bacteria', 2]


def flee_or_fight(character_info, monster_info):
    """ Get user's choice whether flee or fight.

    :param character_info: a list of monster information
    :param monster_info:a list of monster information
    :precondition: The arguments must be lists in correct format
    :post-condition: get user input of behaviour, and determine whether flee or fight

    """
    while character_info[2] > 0 and monster_info[1] > 0:
        pick_list = ['attack', 'flee', 'a', 'f', 'quit']
        user_pick = input(f"What do you want to do? [Attack (a), Flee (f)]\n").lower().strip()
        if user_pick not in pick_list:
            print("Please choose Attack (a) or Flee (f)\n")
        elif user_pick == 'quit':
            print("\nYou quit the game.\n\nGame Ended")
            quit()
        elif user_pick in ['a', 'attack']:
            print(monster_info[0])
            fight(character_info, monster_info)
            if character_info[2] < 1:
                print("\nYou died..\nGame Over.\n")
                quit()
        elif user_pick in ['flee', 'f']:
            while flee(character_info, monster_info):
                flee(character_info, monster_info)
            break


def fight(character_info, monster_info):
    """ Determine who is going to attack first depending on the result of rolling dice.

    :param character_info: a list containing the character's name, current location, and health point
    :param monster_info: a list containing the alien's name and health point
    :precondition: all parameters must be in a correct format
    :post-condition: determine whether the user or the alien attacks first
                     comparing the random number between 1 to 20 inclusive.
    :return: no return
    """
    user_choice = random.randint(1, 20)
    monster_choice = random.randint(1, 20)
    user_attack = random.randint(1, 6)
    monster_attack = random.randint(1, 6)

    if user_choice > monster_choice:
        print("You attacked the alien First!")
        user_hit(character_info, monster_info, user_attack)
        monster_hit(character_info, monster_info, monster_attack)
    elif user_choice < monster_choice:
        print("The alien attacked you first!")
        monster_hit(character_info, monster_info, monster_attack)
        user_hit(character_info, monster_info, user_attack)
    elif user_choice == monster_choice:
        print("You had just a war of nerves")
    if character_info[2] > 0 and monster_info[1] > 0:
        fight(character_info, monster_info)


def user_hit(character_info, monster_info, user_attack):
    """ Show how the user attack the alien.
    
    :param character_info: a list containing the character's name, current location, and health point
    :param monster_info: a list containing the alien's name and health point
    :param user_attack: a random number between 1 to 6 inclusive
    :precondition: all parameters must be in a correct format
    :post-condition: show the process of combat between the user and the alien
    :retrun: no return
    
    >>> user_hit(['Name', [3, 3], 10], ['Big Alien', 5], 3)
    You attacked the alien! Damage : 3
    Your HP : 10
    Monster HP : 2
    >>> user_hit(['Name', [3, 3], 7], ['Big Alien', 5], 3)
    You attacked the alien! Damage : 3
    Your HP : 7
    Monster HP : 2
    >>> user_hit(['Name', [3, 3], 7], ['Small Alien', 3], 2)
    You attacked the alien! Damage : 2
    Your HP : 7
    Monster HP : 1
    """
    monster_info[1] -= user_attack
    if character_info[2] > 0:
        if monster_info[1] < 0:
            monster_info[1] = 0
        print(f"You attacked the alien! Damage : {user_attack}")
        print(f"Your HP : {character_info[2]}\nMonster HP : {monster_info[1]}")


def monster_hit(character_info, monster_info, monster_attack):
    """ Show how the alien attack the user.
    
    :param character_info: a list containing the character's name, current location, and health point
    :param monster_info: a list containing the alien's name and health point
    :param monster_attack: a random number between 1 to 6 inclusive
    :precondition: all parameters must be in a correct format
    :post-condition: show the process of combat between the user and the alien
    :retrun: no return
    
    >>> monster_hit(['Name', [3, 3], 10], ['Big Alien', 5], 3)
    The alien attacked you! Damage : 3
    Your HP : 7
    Monster HP : 5
    >>> monster_hit(['Name', [3, 3], 7], ['Big Alien', 5], 3)
    The alien attacked you! Damage : 3
    Your HP : 4
    Monster HP : 5
    Your HP is low. You are dying!!
    >>> monster_hit(['Name', [3, 3], 7], ['Small Alien', 3], 2)
    The alien attacked you! Damage : 2
    Your HP : 5
    Monster HP : 3
    """
    if monster_info[1] > 0:
        character_info[2] -= monster_attack
        print(f"The alien attacked you! Damage : {monster_attack}")
        print(f"Your HP : {character_info[2]}\nMonster HP : {monster_info[1]}")
    if character_info[2] < 5:
        print("Your HP is low. You are dying!!")
        if character_info[2] < 0:
            print(f"The alien attacked you! Damage : {monster_attack}")
            print(f"Your HP : {character_info[2]}\nMonster HP : {monster_info[1]}")


def flee(character_info, monster_info):
    """ Make the user flee from the alien to the valid direction.
    
    :param character_info: a list containing the character's name, current location, and health point
    :param monster_info: a list containing the alien's name and health point
    :precondition: the parameters must be in correct format
    :post-condition: make the user flee from the alien to the vaild direction that the user wants and
                     after the user fled, the alien might stab the user in the back with 10% of probability
    :return: no return
    """
    flee_probability = random.randint(1, 10)
    direction = get_user_choice()
    valid_move = validate_move(direction, character_info)
    if flee_probability == 1:
        random_damage = random.randint(1, 4)
        character_info[2] -= random_damage
        print(f"The {monster_info[0]} stabbed you in the back!\nYour HP has decreased by {random_damage}\n")
        flee_move(valid_move, character_info, monster_info, )
    else:
        flee_move(valid_move, character_info, monster_info, )


def flee_move(valid_move, character_info, monster_info, ):
    """ if valid_move is True, print successfully fled and move the character.
        If not, print an error message.
    
    :param valid_move: check if it is valid
    :param character_info: a list containing the character's name, current location, and health point
    :param monster_info: a list containing the alien's name and health point
    :precondition: arguments should be in right format
    :post-condition: if valid_move is True, print successfully fled and move the character.
                    If not, print an error message
    """
    if valid_move:
        move_character(character_info[1])
        fled_check_monster = check_for_monsters(monster_info, character_info)
        if not fled_check_monster:
            print("Successfully fled\n")
    else:
        print("You cannot go there :(\n")
        flee(character_info, monster_info)


def make_character():
    """ Initialize a character's name, health point, and starting point.

    :return: a list of the character's information
    """
    character_name = input("Enter Your Name:\n").upper().split()
    character_name = ''.join(character_name)
    HEALTH = 10
    character_location = [3, 3]
    character_info = [character_name, character_location, HEALTH]
    return character_info


def get_user_choice():
    """ Prompt the user for the direction that the user wants to go (East, West, South, North).

    :post-condition: the function will return the user's input
    :return: the direction that the user wants to go as a string
    """
    where_to_go = input("Where do you want to go? (East, West, South, North)\n")
    where_to_go = ''.join(where_to_go.lower().split())
    if where_to_go not in ['e', 'east', 'w', 'west', 's', 'south', 'n', 'north', 'quit']:
        print("You put the wrong direction. Try again.\n")
    return where_to_go


def move_character(current_location):
    """ Draw a map depending on the character's current location.

    :param current_location: a list of two numbers that indicate horizontal and vertical point
    :precondition: current_location must include two positive integers.
    :post-condition: print the map showing the character's current location
    :return: no return
    """
    map_list = []
    for vertical in range(1, 6):
        location_list = []
        for horizontal in range(1, 6):
            coordinates_list = [horizontal, vertical]
            if coordinates_list == current_location:
                location_list += "#"
            elif coordinates_list != current_location:
                location_list += "□"
        add_location = "".join(location_list)
        map_list.append(add_location)

    print(f"{map_list[-1]}\n{map_list[-2]}\n{map_list[-3]}\n{map_list[-4]}\n{map_list[-5]}")


def validate_move(direction, character_info):
    """ Determine whether the user wanted to move within the boundary.

    :param direction: a string that is 'e', 'w', 's', 'n', 'east', 'west', 'south', or 'north'
    :param character_info: a list containing the character's name, current location, and health point
    :precondition: all parameters must be in correct format
    :post-condition: determine whether the user wanted to move within the boundary or not, and
                    if so, move the user's current location and acknowledge it was a valid move
    :return: If the move was invalid, return False, and if the move was valid, return True
    >>> validate_move('s', ['Name', [3, 3], 10])
    True
    >>> validate_move('e', ['Name', [2, 3], 10])
    True
    >>> validate_move('w', ['Name', [1, 3], 10])
    False
    >>> validate_move('n', ['Name', [3, 5], 10])
    False
    """
    error_list1 = ['1w', '1west', '5e', '5east']
    error_list2 = ['1s', '1south', '5n', '5north']
    concatenation1 = str(character_info[1][0]) + direction
    concatenation2 = str(character_info[1][1]) + direction
    if concatenation1 in error_list1 or concatenation2 in error_list2:
        return False
    elif direction in ['e', 'east']:
        character_info[1][0] += 1
        return True
    elif direction in ['w', 'west']:
        character_info[1][0] -= 1
        return True
    elif direction in ['s', 'south']:
        character_info[1][1] -= 1
        return True
    elif direction in ['n', 'north']:
        character_info[1][1] += 1
        return True


def main():
    # Program starts here
    # import doctest
    # doctest.testmod(verbose=True)
    # Enter your code here.
    print("In 2100, During the space travel with Elon Musk's Space X...\n"
          "The spaceship has fallen down to CST Planet that you have never been before.\n"
          "After you woke up, you found that there are a lot of aliens.\n"
          "You should defend yourself until a rescue team arrives.\n")
    game()


if __name__ == "__main__":
    # Invoke the main function
    main()
