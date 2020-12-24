"""
COMP 1510
Final Exam - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


from unittest import TestCase
from yahtzee import initialize_player_score


class TestInitializePlayer(TestCase):

    def test_initialize_player_empty_name(self):
        expected_return = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1,
                           'Three of a kind': -1, 'Four of a kind': -1, 'Full House': -1, 'Small straight': -1,
                           'Large straight': -1, 'Chance': -1, 'Yahtzee': -1}
        actual_return = initialize_player_score()
        self.assertEqual(expected_return, actual_return)
