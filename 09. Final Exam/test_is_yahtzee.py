"""
COMP 1510
09. Final Exam - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


from unittest import TestCase
from yahtzee import is_yahtzee


class TestIsYahtzee(TestCase):

    def test_is_yahtzee_empty_score(self):
        player_score = {'Yahtzee': -1}
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_yahtzee(player_score, dice_list)
        self.assertEqual(expected_return, actual_return)

    def test_is_yahtzee_occupied_number(self):
        player_score = {'Yahtzee': 2}
        dice_list = [1, 1, 1, 1, 1]
        expected_return = False
        actual_return = is_yahtzee(player_score, dice_list)
        self.assertEqual(expected_return, actual_return)

    def test_is_yahtzee_occupied_string(self):
        player_score = {'Yahtzee': 'Occupied'}
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_yahtzee(player_score, dice_list)
        self.assertEqual(expected_return, actual_return)

    def test_is_yahtzee_empty_score_other_keys(self):
        player_score = {'Yahtzee': -1, 1: 'ABC', 2: 345}
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_yahtzee(player_score, dice_list)
        self.assertEqual(expected_return, actual_return)

    def test_is_yahtzee_occupied_other_keys(self):
        player_score = {'Yahtzee': 3, 1: 'ABC', 2: 345}
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_yahtzee(player_score, dice_list)
        self.assertEqual(expected_return, actual_return)
