"""
COMP 1510
09. Final Exam - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import is_small_straight


class TestIsSmallStraight(TestCase):

    def test_is_small_straight_empty_score(self):
        dice_list = [1, 2, 3, 4, 5]
        player_score = {'Small straight': -1}
        expected_return = False
        actual_return = is_small_straight(player_score, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_small_straight_occupied_number(self, mock_output):
        dice_list = [1, 2, 3, 4, 5]
        player_score = {'Small straight': 30}
        expected_return = True
        actual_return = is_small_straight(player_score, dice_list)
        expected_print = 'You have already chosen [Small straight] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_small_straight_occupied_string(self, mock_output):
        dice_list = [1, 2, 3, 4, 5]
        player_score = {'Small straight': 'ABC'}
        expected_return = True
        actual_return = is_small_straight(player_score, dice_list)
        expected_print = 'You have already chosen [Small straight] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_is_small_straight_empty_score_other_keys(self):
        dice_list = [2, 3, 4, 5, 6]
        player_score = {'Small straight': -1, 1: 'ABC', 2: '123', 3: 678}
        expected_return = False
        actual_return = is_small_straight(player_score, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_small_straight_occupied_other_keys(self, mock_output):
        dice_list = [2, 3, 4, 5, 6]
        player_score = {'Small straight': 35, 1: 'ABC', 2: '123', 3: 678}
        expected_return = True
        actual_return = is_small_straight(player_score, dice_list)
        expected_print = 'You have already chosen [Small straight] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)
