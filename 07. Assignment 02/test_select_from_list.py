import io
from unittest import TestCase
from unittest.mock import patch
from books import select_from_list


class TestSelectFromList(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_select_from_list_minimum_valid_input(self, mock_input):
        search_result = [{'1': 'Dog', '2': 'Cat'}, {'1': 'Bat'}, {'A': 'Pizza'}]
        actual = select_from_list(search_result)
        expected = 0

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_select_from_list_maximum_valid_input(self, mock_input):
        search_result = [{'1': 'Dog', '2': 'Cat'}, {'1': 'Bat'}, {'A': 'Pizza'}]
        actual = select_from_list(search_result)
        expected = 2

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_from_list_invalid_empty_input(self, mock_output, mock_input):
        search_result = [{'1': 'Dog', '2': 'Cat'}, {'1': 'Bat'}, {'A': 'Pizza'}]
        select_from_list(search_result)
        expected = '\nPlease enter a number...\n\n'

        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['apple'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_from_list_invalid_alphabetic_input(self, mock_output, mock_input):
        search_result = [{'1': 'Dog', '2': 'Cat'}, {'1': 'Bat'}, {'A': 'Pizza'}]
        select_from_list(search_result)
        expected = '\nPlease enter a number...\n\n'

        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_from_list_invalid_input_out_of_boundary(self, mock_output, mock_input):
        search_result = [{'1': 'Dog', '2': 'Cat'}, {'1': 'Bat'}, {'A': 'Pizza'}]
        select_from_list(search_result)
        expected = '\nYou chose the wrong number...\n\n'

        self.assertEqual(expected, mock_output.getvalue())
