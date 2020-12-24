"""
COMP 1510
Final Exam - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""

import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import choose_a_combination_helper


class TestChooseACombinationHelper(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_invalid_number_lower_bound(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 0
        player_score = {'Aces': -1}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_invalid_number_upper_bound(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 14
        player_score = {'Aces': -1}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_aces_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 1
        player_score = {'Aces': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_aces_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 1
        player_score = {'Aces': 4}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Aces] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_twos_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 2
        player_score = {'Aces': 4, 'Twos': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_twos_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 2
        player_score = {'Aces': 4, 'Twos': 8}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Twos] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_threes_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 3
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_threes_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 3
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Threes] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_fours_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 4
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_fours_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 4
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Fours] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_fives_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 5
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_fives_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 5
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Fives] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_sixes_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 6
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_sixes_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 6
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Sixes] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_three_of_a_kind_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 7
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_three_of_a_kind_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 7
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Three of a kind] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_four_of_a_kind_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 8
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_four_of_a_kind_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 8
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Four of a kind] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_full_house_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 9
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_full_house_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 9
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Full House] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_small_straight_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 10
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_small_straight_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 10
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': 30}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Small straight] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_large_straight_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 11
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': 30,
                        'Large straight': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_large_straight_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 11
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': 30,
                        'Large straight': 40}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Large straight] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_chance_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 12
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': 30,
                        'Large straight': 40, 'Chance': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_a_combination_helper_chance_occupied(self, mock_output):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 12
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': 30,
                        'Large straight': 40, 'Chance': 20}
        expected_return = True
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        expected_print = "You have already chosen [Chance] before. Please try again.\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_choose_a_combination_helper_yahtzee_empty(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 13
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': 30,
                        'Large straight': 40, 'Chance': 20, 'Yahtzee': -1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)

    def test_choose_a_combination_helper_yahtzee_occupied(self):
        determinant = True
        dice_list = [1, 1, 1, 1, 5]
        mark_choice = 13
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 20, 'Sixes': 18,
                        'Three of a kind': 24, 'Four of a kind': 21, 'Full House': 25, 'Small straight': 30,
                        'Large straight': 40, 'Chance': 20, 'Yahtzee': 1}
        expected_return = False
        actual_return = choose_a_combination_helper(determinant, dice_list, mark_choice, player_score)
        self.assertEqual(expected_return, actual_return)
