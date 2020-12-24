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
from yahtzee import is_full_house


class TestIsFullHouse(TestCase):

    def test_is_full_house_empty_score(self):
        player_score = {'Full House': -1}
        same_number_list = [1, 0, 2, 1, 1, 1]
        expected_return = False
        actual_return = is_full_house(player_score, same_number_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_full_house_occupied_number(self, mock_output):
        player_score = {'Full House': 40}
        same_number_list = [1, 0, 2, 1, 1, 1]
        expected_return = True
        actual_return = is_full_house(player_score, same_number_list)
        expected_print = 'You have already chosen [Full House] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_full_house_occupied_string(self, mock_output):
        player_score = {'Full House': 'ABC'}
        same_number_list = [1, 0, 2, 1, 1, 1]
        expected_return = True
        actual_return = is_full_house(player_score, same_number_list)
        expected_print = 'You have already chosen [Full House] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_is_full_house_empty_score_other_keys(self):
        player_score = {'Full House': -1, 1: 'ABC', 2: '123', 3: 678}
        same_number_list = [1, 0, 2, 1, 1, 1]
        expected_return = False
        actual_return = is_full_house(player_score, same_number_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_full_house_occupied_other_keys(self, mock_output):
        player_score = {'Full House': 40, 1: 'ABC', 2: '123', 3: 678}
        same_number_list = [1, 0, 2, 1, 1, 1]
        expected_return = True
        actual_return = is_full_house(player_score, same_number_list)
        expected_print = 'You have already chosen [Full House] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)
