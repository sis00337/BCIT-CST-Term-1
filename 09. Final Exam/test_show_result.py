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
from yahtzee import show_result


class TestShowResult(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_arbitrary_key_value_score_sheet(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'ab': 1, 2: 2, 'Small Straight': 3, 'AB': 4}
        player_2_score = {1: 2, 2: 4, 3: 6, 'AB': 8}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 10\n' \
                         'Sandy : 20\n' \
                         'Congratulation!!! The winner is Sandy!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_both_score_sheet_upper_section_below_63(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 2, 'Twos': 4, 'Threes': 6, 'Fours': 8, 'Fives': 10, 'Sixes': 12, 'Yahtzee': 0}
        player_2_score = {'Aces': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6, 'Yahtzee': 0}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 42\n' \
                         'Sandy : 21\n' \
                         'Congratulation!!! The winner is Ken!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_2_score_sheet_upper_section_equal_to_63(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 2, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Yahtzee': 0}
        player_2_score = {'Aces': 3, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Yahtzee': 0}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 62\n' \
                         'Sandy : 98\n' \
                         'Congratulation!!! The winner is Sandy!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_1_score_sheet_upper_section_greater_than_63(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 5, 'Twos': 8, 'Threes': 9, 'Fours': 12, 'Fives': 20, 'Sixes': 24, 'Yahtzee': 0}
        player_2_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 20, 'Sixes': 6, 'Yahtzee': 0}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 113\n' \
                         'Sandy : 51\n' \
                         'Congratulation!!! The winner is Ken!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_2_score_sheet_one_yahtzee(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 0}
        player_2_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 1}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 0\n' \
                         'Sandy : 50\n' \
                         'Congratulation!!! The winner is Sandy!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_1_score_sheet_two_yahtzee(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 2}
        player_2_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 0}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 150\n' \
                         'Sandy : 0\n' \
                         'Congratulation!!! The winner is Ken!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_1_score_sheet_three_yahtzee(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 3}
        player_2_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 0}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 250\n' \
                         'Sandy : 0\n' \
                         'Congratulation!!! The winner is Ken!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_1_full_score_sheet_minimum_score(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0,
                          'Three of a kind': 0, 'Four of a kind': 0, 'Full House': 0, 'Small straight': 0,
                          'Large straight': 0, 'Chance': 5, 'Yahtzee': 0}
        player_2_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0,
                          'Three of a kind': 0, 'Four of a kind': 0, 'Full House': 25, 'Small straight': 0,
                          'Large straight': 0, 'Chance': 5, 'Yahtzee': 0}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 5\n' \
                         'Sandy : 30\n' \
                         'Congratulation!!! The winner is Sandy!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_1_full_score_sheet_maximum_score_one_yahtzee(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30,
                          'Three of a kind': 30, 'Four of a kind': 30, 'Full House': 25, 'Small straight': 30,
                          'Large straight': 40, 'Chance': 30, 'Yahtzee': 1}
        player_2_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0,
                          'Three of a kind': 0, 'Four of a kind': 0, 'Full House': 25, 'Small straight': 0,
                          'Large straight': 0, 'Chance': 5, 'Yahtzee': 0}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 375\n' \
                         'Sandy : 30\n' \
                         'Congratulation!!! The winner is Ken!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_player_2_full_score_sheet_maximum_score_two_yahtzee(self, mock_output):
        player_1_name = 'Ken'
        player_2_name = 'Sandy'
        player_1_score = {'Aces': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30,
                          'Three of a kind': 30, 'Four of a kind': 30, 'Full House': 25, 'Small straight': 30,
                          'Large straight': 40, 'Chance': 30, 'Yahtzee': 1}
        player_2_score = {'Aces': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30,
                          'Three of a kind': 30, 'Four of a kind': 30, 'Full House': 25, 'Small straight': 30,
                          'Large straight': 40, 'Chance': 30, 'Yahtzee': 2}
        show_result(player_1_name, player_2_name, player_1_score, player_2_score)
        expected_print = 'Ken : 375\n' \
                         'Sandy : 475\n' \
                         'Congratulation!!! The winner is Sandy!!!\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)
