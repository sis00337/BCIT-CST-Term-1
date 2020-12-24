"""
COMP 1510
Final Exam - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


from unittest import TestCase
from unittest.mock import patch
from yahtzee import create_player


class TestCreatePlayer(TestCase):

    @patch('builtins.input', side_effect=['', ''])
    def test_create_player_empty_string(self, mock_input):
        expected_return = ('', '')
        actual_return = create_player()
        self.assertEqual(expected_return, actual_return)

    @patch('builtins.input', side_effect=['             Ken', 'Super Man'])
    def test_create_player_1_leading_spaces(self, mock_input):
        expected_return = ('Ken', 'Super Man')
        actual_return = create_player()
        self.assertEqual(expected_return, actual_return)

    @patch('builtins.input', side_effect=['Super      Man', 'Ken'])
    def test_create_player_1_spaces_in_the_middle(self, mock_input):
        expected_return = ('Super      Man', 'Ken')
        actual_return = create_player()
        self.assertEqual(expected_return, actual_return)

    @patch('builtins.input', side_effect=['Bat Man                ', 'Super Man'])
    def test_create_player_1_trailing_spaces(self, mock_input):
        expected_return = ('Bat Man', 'Super Man')
        actual_return = create_player()
        self.assertEqual(expected_return, actual_return)

    @patch('builtins.input', side_effect=['Super Man', '             Ken'])
    def test_create_player_2_leading_spaces(self, mock_input):
        expected_return = ('Super Man', 'Ken')
        actual_return = create_player()
        self.assertEqual(expected_return, actual_return)

    @patch('builtins.input', side_effect=['Ken', 'Super      Man'])
    def test_create_player_2_spaces_in_the_middle(self, mock_input):
        expected_return = ('Ken', 'Super      Man')
        actual_return = create_player()
        self.assertEqual(expected_return, actual_return)

    @patch('builtins.input', side_effect=['Super Man', 'Bat Man                '])
    def test_create_player_2_trailing_spaces(self, mock_input):
        expected_return = ('Super Man', 'Bat Man')
        actual_return = create_player()
        self.assertEqual(expected_return, actual_return)
