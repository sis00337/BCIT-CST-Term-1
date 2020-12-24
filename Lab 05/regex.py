"""
Lab 06
Regular Expressions
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""

import re
from re import Pattern


def is_email(address: str) -> bool:
    """ Check if a string is in the email format.

    :param address: a string
    :post-condition: If address is in the correct email format, return True. Otherwise, return False.
    :return: True or False

    >>> is_email('')
    False
    >>> is_email('ABC')
    False
    >>> is_email('ABC@DEF.GHI')
    True
    >>> is_email('strong_man20@aaa.com')
    True
    >>> is_email('strong_man@south_korea.ca')
    False
    >>> is_email('email_address@canada.a')
    False
    >>> is_email('email_address@canada19.ca')
    True
    >>> is_email('email_address@canaca.com')
    True
    >>> is_email('email_address@canada.king')
    True
    >>> is_email('email_address@canada.train')
    False
    """
    valid_email = re.compile(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.(\w|\W){2,4}$')
    match_object = valid_email.match(address)
    if match_object:
        return True
    else:
        return False


def is_nakamoto(name: str) -> bool:
    """ Check if a string is in the correct name format that starts with the capital letter and ends with 'Nakamoto'.

    :param name: a string
    :post-condition: If name is in the correct name format, return True.
                    Otherwise, return False.
    :return: True or False

    >>> is_nakamoto('')
    False
    >>> is_nakamoto('ABC Nakamoto')
    False
    >>> is_nakamoto('Abc Nakamoto')
    True
    >>> is_nakamoto('123 Nakamoto')
    False
    >>> is_nakamoto('A1b Nakamoto')
    False
    >>> is_nakamoto('Santa Nakamoto')
    True
    >>> is_nakamoto('santa Nakamoto')
    False
    >>> is_nakamoto('Santa nakamoto')
    False
    >>> is_nakamoto('Nakamoto')
    False
    >>> is_nakamoto('Santa_Claus Nakamoto')
    False
    >>> is_nakamoto('Satochi Nakamoto')
    True
    >>> is_nakamoto('Alice Nakamoto')
    True
    >>> is_nakamoto('Robocop Nakamoto')
    True
    >>> is_nakamoto('Mr. Nakamoto')
    False
    """
    valid_nakamoto_name = re.compile(r'^[A-Z][a-z]* Nakamoto$')
    match_object = valid_nakamoto_name.match(name)
    if match_object:
        return True
    else:
        return False


def is_poker(hand: str) -> bool:
    """ Check the input is valid and Check what poker hand the input belongs to.

    :param hand: a string that contains five letters
    :precondition: hand must include five letters
    :post-condition: If hand is valid, check what poker hand it belongs to and return True.
                    Otherwise, print the error message and return False.
    :return: True or False

    >>> is_poker('')
    Your hand is not valid
    False
    >>> is_poker('aaaaa')
    Your hand is not valid
    False
    >>> is_poker('AAAAA')
    Your hand is not valid
    False
    >>> is_poker('AKQJT2')
    Your hand is not valid
    False
    >>> is_poker('a34tq')
    Your hand is High Card
    True
    >>> is_poker('33AKQ')
    Your hand is One Pair
    True
    >>> is_poker('66TTK')
    Your hand is Two Pairs
    True
    >>> is_poker('99984')
    Your hand is Three of a Kind
    True
    >>> is_poker('QQQ77')
    Your hand is Full House
    True
    >>> is_poker('KKKK4')
    Your hand is Four of a Kind
    True
    >>> is_poker('23456')
    Your hand is Straight Flush
    True
    >>> is_poker('AKQJT')
    Your hand is Straight Flush
    True
    """
    is_same_cards = re.compile(r'^([AKQJT2-9])+\1{4}$', re.I)
    is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                             r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
    is_four_of_a_kind = re.compile(r'([AKQJT2-9])+\1{3}([AKQJT2-9])', re.I)
    is_three_repetition = re.compile(r'([AKQJT2-9])+\1{2}([AKQJT2-9]){2}', re.I)
    is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
    is_high_card = re.compile(r'^([AKQJT2-9]){5}$', re.I)
    if not is_high_card.search(hand) or is_same_cards.search(hand):
        print('Your hand is not valid')
        return False
    elif not is_same_cards.search(hand):
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        return True


def find_hand(hand: str, sf: Pattern[str], four: Pattern[str], three: Pattern[str], two: Pattern[str]) -> None:
    """ Check what poker hand the input belongs to.

    :param hand: a string that contains five letters
    :param sf: a regular expression for finding the straight flush hand
    :param four: a regular expression for finding the four-of-a-kind hand
    :param three: a regular expression for finding a certain letter repeated three times
    :param two: a regular expression for finding a certain letter repeated twice

    :precondition: hand must include five letters, a combination of letters A, K, Q, J, and T and numbers
                    between 2 to 9 inclusive (case insensitive)
    :precondition: If hand contains the repetition of a certain letter, the repetition must always come first
    :precondition: If there are two repetitions, the longer repetition must come first
    :precondition: If hand contains all different letters, it must be sorted by ascending or descending order
    :precondition: is_four_of_a_kind, is_three_repetition and is_two_repetition must be the correct regular expressions
                    that can find each hand

    :post-condition: print what kind of hand it is
    :return: nothing
    >>> cards = 'a34tq'
    >>> is_straight = re.compile(r'''A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
    ... r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT''', re.I)
    >>> is_four_of_a_kind = re.compile(r'([AKQJT2-9])\\1{3}([AKQJT2-9])', re.I)
    >>> is_three_repetition = re.compile(r'([AKQJT2-9])\\1{2}([AKQJT2-9]){2}', re.I)
    >>> is_two_repetition = re.compile(r'([AKQJT2-9])\\1', re.I)
    >>> find_hand(cards, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
    Your hand is High Card

    >>> cards = 'AA978'
    >>> is_straight = re.compile(r'''A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
    ... r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT''', re.I)
    >>> is_four_of_a_kind = re.compile(r'([AKQJT2-9])\\1{3}([AKQJT2-9])', re.I)
    >>> is_three_repetition = re.compile(r'([AKQJT2-9])\\1{2}([AKQJT2-9]){2}', re.I)
    >>> is_two_repetition = re.compile(r'([AKQJT2-9])\\1', re.I)
    >>> find_hand(cards, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
    Your hand is One Pair

    >>> cards = 'QQ55K'
    >>> is_straight = re.compile(r'''A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
    ... r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT''', re.I)
    >>> is_four_of_a_kind = re.compile(r'([AKQJT2-9])\\1{3}([AKQJT2-9])', re.I)
    >>> is_three_repetition = re.compile(r'([AKQJT2-9])\\1{2}([AKQJT2-9]){2}', re.I)
    >>> is_two_repetition = re.compile(r'([AKQJT2-9])\\1', re.I)
    >>> find_hand(cards, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
    Your hand is Two Pairs

    >>> cards = '77789'
    >>> is_straight = re.compile(r'''A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
    ... r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT''', re.I)
    >>> is_four_of_a_kind = re.compile(r'([AKQJT2-9])\\1{3}([AKQJT2-9])', re.I)
    >>> is_three_repetition = re.compile(r'([AKQJT2-9])\\1{2}([AKQJT2-9]){2}', re.I)
    >>> is_two_repetition = re.compile(r'([AKQJT2-9])\\1', re.I)
    >>> find_hand(cards, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
    Your hand is Three of a Kind

    >>> cards = 'tttKK'
    >>> is_straight = re.compile(r'''A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
    ... r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT''', re.I)
    >>> is_four_of_a_kind = re.compile(r'([AKQJT2-9])\\1{3}([AKQJT2-9])', re.I)
    >>> is_three_repetition = re.compile(r'([AKQJT2-9])\\1{2}([AKQJT2-9]){2}', re.I)
    >>> is_two_repetition = re.compile(r'([AKQJT2-9])\\1', re.I)
    >>> find_hand(cards, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
    Your hand is Full House

    >>> cards = '55559'
    >>> is_straight = re.compile(r'''A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
    ... r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT''', re.I)
    >>> is_four_of_a_kind = re.compile(r'([AKQJT2-9])\\1{3}([AKQJT2-9])', re.I)
    >>> is_three_repetition = re.compile(r'([AKQJT2-9])\\1{2}([AKQJT2-9]){2}', re.I)
    >>> is_two_repetition = re.compile(r'([AKQJT2-9])\\1', re.I)
    >>> find_hand(cards, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
    Your hand is Four of a Kind

    >>> cards = 'AKQJT'
    >>> is_straight = re.compile(r'''A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
    ... r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT''', re.I)
    >>> is_four_of_a_kind = re.compile(r'([AKQJT2-9])\\1{3}([AKQJT2-9])', re.I)
    >>> is_three_repetition = re.compile(r'([AKQJT2-9])\\1{2}([AKQJT2-9]){2}', re.I)
    >>> is_two_repetition = re.compile(r'([AKQJT2-9])\\1', re.I)
    >>> find_hand(cards, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
    Your hand is Straight Flush
    """
    if sf.search(hand):
        print('Your hand is Straight Flush')
    elif four.search(hand):
        print(f'Your hand is Four of a Kind')
    elif three.search(hand):
        three_object = three.search(hand)
        if three_object.group()[3] == three_object.group()[4]:
            print('Your hand is Full House')
        else:
            print(f'Your hand is Three of a Kind')
    elif two.findall(hand):
        two_object = two.findall(hand)
        if len(two_object) == 2:
            print(f'Your hand is Two Pairs')
        else:
            print(f'Your hand is One Pair')
    else:
        print('Your hand is High Card')


def main() -> None:
    """
    Drives the program.
    """
    # import doctest
    # doctest.testmod(verbose=True)
    # is_email('sis00337@gmail.com')
    # is_nakamoto('Satoshi Nakamoto')
    is_poker('25436')


if __name__ == "__main__":
    main()
