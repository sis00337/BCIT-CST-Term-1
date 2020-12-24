"""
COMP 1510
09. Yahtzee Game - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import is_upper_section


class TestIsUpperSection(TestCase):

    def test_is_upper_section_mark_choice_1_empty_score(self):
        player_score = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}
        mark_choice = 1
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_upper_section_mark_choice_1_occupied(self, mock_output):
        player_score = {1: 3, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}
        mark_choice = 1
        dice_list = [1, 2, 3, 4, 5]
        expected_return = True
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        expected_print = 'You have already chosen [1] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_is_upper_section_mark_choice_2_empty_score(self):
        player_score = {1: 3, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}
        mark_choice = 2
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_upper_section_mark_choice_2_occupied(self, mock_output):
        player_score = {1: 3, 2: 6, 3: -1, 4: -1, 5: -1, 6: -1}
        mark_choice = 2
        dice_list = [1, 2, 3, 4, 5]
        expected_return = True
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        expected_print = 'You have already chosen [2] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_is_upper_section_mark_choice_3_empty_score(self):
        player_score = {1: 3, 2: 6, 3: -1, 4: -1, 5: -1, 6: -1}
        mark_choice = 3
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_upper_section_mark_choice_3_occupied(self, mock_output):
        player_score = {1: 3, 2: 6, 3: 9, 4: -1, 5: -1, 6: -1}
        mark_choice = 3
        dice_list = [1, 2, 3, 4, 5]
        expected_return = True
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        expected_print = 'You have already chosen [3] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_is_upper_section_mark_choice_4_empty_score(self):
        player_score = {1: 3, 2: 6, 3: 9, 4: -1, 5: -1, 6: -1}
        mark_choice = 4
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_upper_section_mark_choice_4_occupied(self, mock_output):
        player_score = {1: 3, 2: 6, 3: 9, 4: 'ABC', 5: -1, 6: -1}
        mark_choice = 4
        dice_list = [1, 2, 3, 4, 5]
        expected_return = True
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        expected_print = 'You have already chosen [4] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_is_upper_section_mark_choice_5_empty_score(self):
        player_score = {1: 3, 2: 6, 3: 9, 4: 'ABC', 5: -1, 6: -1}
        mark_choice = 5
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_upper_section_mark_choice_5_occupied(self, mock_output):
        player_score = {1: 3, 2: 6, 3: 9, 4: 'ABC', 5: '20', 6: -1}
        mark_choice = 5
        dice_list = [1, 2, 3, 4, 5]
        expected_return = True
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        expected_print = 'You have already chosen [5] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_is_upper_section_mark_choice_6_empty_score(self):
        player_score = {1: 3, 2: 6, 3: 9, 4: 'ABC', 5: '20', 6: -1}
        mark_choice = 6
        dice_list = [1, 2, 3, 4, 5]
        expected_return = False
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_upper_section_mark_choice_6_occupied(self, mock_output):
        player_score = {1: 3, 2: 6, 3: 9, 4: 'ABC', 5: '20', 6: 30}
        mark_choice = 6
        dice_list = [1, 2, 3, 4, 5]
        expected_return = True
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        expected_print = 'You have already chosen [6] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_upper_section_mark_choice_sixes_occupied(self, mock_output):
        player_score = {'Ace': -1, 'Twos': 6, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 30}
        mark_choice = 6
        dice_list = [1, 2, 3, 4, 5]
        expected_return = True
        actual_return = is_upper_section(player_score, mark_choice, dice_list)
        expected_print = 'You have already chosen [Sixes] before. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)
