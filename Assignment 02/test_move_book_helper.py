import io
from unittest import TestCase
from unittest.mock import patch
from books import move_book_helper


class TestMoveBookHelper(TestCase):

    @patch('builtins.input', side_effect=['AA'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_helper_valid_shelf(self, mock_output, mock_input):
        search_result = [{1: 'Harry', 'Shelf': '2', 5: 'Computer', 6: 'Brazil'},
                         {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 'Shelf': '15'},
                         {1: 'Mike', 2: 'Deer', 'Shelf': '23', 5: 'Computer', 6: 'France'}]
        result_number = 0
        shelf_options = ['1', '2', '15', '20', '23', 'AA', 'Z']
        move_book_helper(search_result, result_number, shelf_options)

        print_actual = mock_output.getvalue()
        print_expected = "\nYou moved the book from 2 to AA\n\n" \
                         "{1: 'Harry', 'Shelf': 'AA', 5: 'Computer', 6: 'Brazil'}\n\n"

        self.assertEqual(print_expected, print_actual)

    @patch('builtins.input', side_effect=['DD'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_helper_invalid_shelf(self, mock_output, mock_input):
        search_result = [{1: 'Harry', 2: 'Cow', 3: 'Wallet', 'Shelf': 'Reading', 5: 'Computer', 6: 'Brazil'},
                         {3: 'Pillow', 'Shelf': 'AA', 5: 'Sailing', 6: 'Iran'},
                         {1: 'Mike', 2: 'Deer', 3: 'Laptop', 'Shelf': '23'}]
        result_number = 0
        shelf_options = ['11', '23', 'AA', 'Reading', 'ZZ']
        move_book_helper(search_result, result_number, shelf_options)

        print_actual = mock_output.getvalue()
        print_expected = "You entered the wrong shelf...\nReturn to the Main Menu...\n\n"

        self.assertEqual(print_expected, print_actual)
