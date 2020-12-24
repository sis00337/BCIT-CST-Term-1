import io
from unittest import TestCase
from unittest.mock import patch
from books import move_menu


class TestAskForSearchMenuSelectionForMovingBook(TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_valid_one(self, mock_output, mock_input):
        actual_return_value = move_menu()
        expected_return_value = 1

        print_actual = mock_output.getvalue()
        print_expected = "\r\n" \
                         "---------- Search Menu ----------\n"\
                         "Please search books that you want to change the shelf number.\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_valid_two(self, mock_output, mock_input):
        actual_return_value = move_menu()
        expected_return_value = 2

        print_actual = mock_output.getvalue()
        print_expected = "\r\n" \
                         "---------- Search Menu ----------\n" \
                         "Please search books that you want to change the shelf number.\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_valid_three(self, mock_output, mock_input):
        actual_return_value = move_menu()
        expected_return_value = 3

        print_actual = mock_output.getvalue()
        print_expected = "\r\n" \
                         "---------- Search Menu ----------\n" \
                         "Please search books that you want to change the shelf number.\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_valid_four(self, mock_output, mock_input):
        actual_return_value = move_menu()
        expected_return_value = 4

        print_actual = mock_output.getvalue()
        print_expected = "\r\n" \
                         "---------- Search Menu ----------\n" \
                         "Please search books that you want to change the shelf number.\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_valid_five(self, mock_output, mock_input):
        actual_return_value = move_menu()
        expected_return_value = 5

        print_actual = mock_output.getvalue()
        print_expected = "\r\n" \
                         "---------- Search Menu ----------\n" \
                         "Please search books that you want to change the shelf number.\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_valid_six(self, mock_output, mock_input):
        actual_return_value = move_menu()
        expected_return_value = 6

        print_actual = mock_output.getvalue()
        print_expected = "\r\n" \
                         "---------- Search Menu ----------\n" \
                         "Please search books that you want to change the shelf number.\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_invalid_number_zero(self, mock_output, mock_input):
        move_menu()
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\r\n" \
                          "---------- Search Menu ----------\n" \
                          "Please search books that you want to change the shelf number.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('builtins.input', side_effect=['7'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_invalid_number_seven(self, mock_output, mock_input):
        move_menu()
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\r\n" \
                          "---------- Search Menu ----------\n" \
                          "Please search books that you want to change the shelf number.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('builtins.input', side_effect=['ABC'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_menu_invalid_alpha(self, mock_output, mock_input):
        move_menu()
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\r\n" \
                          "---------- Search Menu ----------\n" \
                          "Please search books that you want to change the shelf number.\n"
        self.assertEqual(expected_output, the_function_printed_this)
