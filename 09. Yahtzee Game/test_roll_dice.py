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
from yahtzee import roll_dice


class TestRollDice(TestCase):

    @patch('random.randint', side_effect=[1, 2, 3, 4, 5])
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_current_dice_length_five(self, mock_output, mock_input, random_number_generator):
        player_dice = [[0, 0, 0, 0, 0], []]
        roll_dice(player_dice)
        expected_print = "Press <ENTER> to roll dice.\n" \
                         "[1, 2, 3, 4, 5]      Keeping Dice : []\n\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('random.randint', side_effect=[6, 3, 4, 1])
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_current_dice_length_four(self, mock_output, mock_input, random_number_generator):
        player_dice = [[5, 5, 5, 5], [5]]
        roll_dice(player_dice)
        expected_print = "Press <ENTER> to roll dice.\n" \
                         "[1, 3, 4, 6]      Keeping Dice : [5]\n\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('random.randint', side_effect=[4, 2, 3])
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_current_dice_length_three(self, mock_output, mock_input, random_number_generator):
        player_dice = [[1, 1, 1], [4, 5]]
        roll_dice(player_dice)
        expected_print = "Press <ENTER> to roll dice.\n" \
                         "[2, 3, 4]      Keeping Dice : [4, 5]\n\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('random.randint', side_effect=[2, 3])
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_current_dice_length_two(self, mock_output, mock_input, random_number_generator):
        player_dice = [[5, 6], [1, 2, 3]]
        roll_dice(player_dice)
        expected_print = "Press <ENTER> to roll dice.\n" \
                         "[2, 3]      Keeping Dice : [1, 2, 3]\n\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('random.randint', side_effect=[6])
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_current_dice_length_one(self, mock_output, mock_input, random_number_generator):
        player_dice = [[6], [5, 5, 5, 5]]
        roll_dice(player_dice)
        expected_print = "Press <ENTER> to roll dice.\n" \
                         "[6]      Keeping Dice : [5, 5, 5, 5]\n\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_current_dice_length_zero(self, mock_output, mock_input):
        player_dice = [[], [1, 2, 3, 4, 5]]
        roll_dice(player_dice)
        expected_print = "Press <ENTER> to roll dice.\n" \
                         "[]      Keeping Dice : [1, 2, 3, 4, 5]\n\n"
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)
