import io
from unittest import TestCase
from unittest.mock import patch
from books import search


class TestSearchBooks(TestCase):

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_1_empty_input(self, mock_output, mock_input):
        user_input = 1
        books_tuple = ({1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Chris', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Harry', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Vincent', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n4 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Chris', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "3. {1: 'Harry', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "4. {1: 'Vincent', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['j'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_1_lower_input(self, mock_output, mock_input):
        user_input = 1
        books_tuple = ({1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Joon', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Joon', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n2 result(s) found\n\n"\
                         "1. {1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Joon', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['S'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_1_upper_input(self, mock_output, mock_input):
        user_input = 1
        books_tuple = ({1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Joon', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Chris', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Nicholas', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Spencer', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n4 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Chris', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "3. {1: 'Nicholas', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "4. {1: 'Spencer', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_2_empty_input(self, mock_output, mock_input):
        user_input = 2
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Harry', 2: 'Cow', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n4 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "3. {1: 'Harry', 2: 'Cow', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "4. {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['dog'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_2_lower_input(self, mock_output, mock_input):
        user_input = 2
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'B', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n2 result(s) found\n\n"\
                         "1. {1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['T'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_2_upper_input(self, mock_output, mock_input):
        user_input = 2
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'B', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Dani', 2: 'Bat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Eiman', 2: 'Tiger', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n3 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Dani', 2: 'Bat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "3. {1: 'Eiman', 2: 'Tiger', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_3_empty_input(self, mock_output, mock_input):
        user_input = 3
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n4 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "3. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "4. {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['la'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_3_lower_input(self, mock_output, mock_input):
        user_input = 3
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n2 result(s) found\n\n"\
                         "1. {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['A'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_3_upper_input(self, mock_output, mock_input):
        user_input = 3
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: 'C', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: 'C', 5: 'D', 6: 'E'})
        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: 'C', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n6 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "3. {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "4. {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "5. {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "6. {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: 'C', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_4_empty_input(self, mock_output, mock_input):
        user_input = 4
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'D', 6: 'E'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'},
                                 {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'D', 6: 'E'},
                                 {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n4 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'}\n" \
                         "2. {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'D', 6: 'E'}\n" \
                         "3. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'}\n" \
                         "4. {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_4_numeric_input(self, mock_output, mock_input):
        user_input = 4
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: 'C', 5: '20', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: '7', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: '7', 5: 'D', 6: 'E'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n1 result(s) found\n\n"\
                         "1. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['read'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_4_lower_input(self, mock_output, mock_input):
        user_input = 4
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: 'C', 5: '20', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: '7', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: '7', 5: 'D', 6: 'E'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n1 result(s) found\n\n"\
                         "1. {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['NOGU'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_4_upper_input(self, mock_output, mock_input):
        user_input = 4
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'D', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'D', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: 'C', 5: '20', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'D', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'D', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'D', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'D', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: '7', 5: 'D', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: '7', 5: 'D', 6: 'E'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'D', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n1 result(s) found\n\n" \
                         "1. {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'D', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_5_empty_input(self, mock_output, mock_input):
        user_input = 5
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'E'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'E'},
                                 {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'},
                                 {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n4 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'E'}\n" \
                         "2. {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'}\n" \
                         "3. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'E'}\n" \
                         "4. {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['sports'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_5_lower_input(self, mock_output, mock_input):
        user_input = 5
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: '20', 5: 'Sports', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'Sailing', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'Architecture', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'Style', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: '7', 5: 'Python', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: '7', 5: 'Java', 6: 'E'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'},
                                 {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: '20', 5: 'Sports', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n2 result(s) found\n\n"\
                         "1. {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'}\n" \
                         "2. {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: '20', 5: 'Sports', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['CO'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_5_upper_input(self, mock_output, mock_input):
        user_input = 5
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'E'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'E'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'E'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: '20', 5: 'Sports', 6: 'E'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'Sailing', 6: 'E'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'Architecture', 6: 'E'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'Style', 6: 'E'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'E'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: '7', 5: 'Python', 6: 'E'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: '7', 5: 'Java', 6: 'E'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'E'},
                                 {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'E'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n3 result(s) found\n\n" \
                         "1. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'E'}\n" \
                         "2. {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'E'}\n" \
                         "3. {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'E'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_6_empty_input(self, mock_output, mock_input):
        user_input = 6
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'South Korea'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'Brazil'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'China'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'South Korea'},
                                 {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'},
                                 {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'Brazil'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'China'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n4 result(s) found\n\n" \
                         "1. {1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'South Korea'}\n" \
                         "2. {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'}\n" \
                         "3. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'Brazil'}\n" \
                         "4. {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'China'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['united'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_6_lower_input(self, mock_output, mock_input):
        user_input = 6
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'South Korea'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'Brazil'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'China'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: '20', 5: 'Sports', 6: 'Japan'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'Sailing', 6: 'Iran'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'Architecture', 6: 'Canada'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'Style', 6: 'United Kingdom'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'France'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: '7', 5: 'Python', 6: 'Belgium'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: '7', 5: 'Java', 6: 'Italy'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'},
                                 {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'Style',
                                  6: 'United Kingdom'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n2 result(s) found\n\n"\
                         "1. {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'}\n" \
                         "2. {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'Style', " \
                         "6: 'United Kingdom'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)

    @patch('builtins.input', side_effect=['RA'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_key_num_6_upper_input(self, mock_output, mock_input):
        user_input = 6
        books_tuple = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'South Korea'},
                       {1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'},
                       {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'Brazil'},
                       {1: 'Vincent', 2: 'Dog', 3: 'Keyboard', 4: '3', 5: 'Accounting', 6: 'China'},
                       {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: '20', 5: 'Sports', 6: 'Japan'},
                       {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'Sailing', 6: 'Iran'},
                       {1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'Architecture', 6: 'Canada'},
                       {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'Style', 6: 'United Kingdom'},
                       {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'France'},
                       {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: '7', 5: 'Python', 6: 'Belgium'},
                       {1: 'Spencer', 2: 'Eagle', 3: 'Fan', 4: '7', 5: 'Java', 6: 'Italy'})

        actual_return_value = search(user_input, books_tuple)
        expected_return_value = [{1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'Brazil'},
                                 {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'Sailing', 6: 'Iran'},
                                 {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'France'}]

        print_actual = mock_output.getvalue()
        print_expected = "\n3 result(s) found\n\n" \
                         "1. {1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'Computer', 6: 'Brazil'}\n" \
                         "2. {1: 'Joon', 2: 'Donkey', 3: 'Pillow', 4: '15', 5: 'Sailing', 6: 'Iran'}\n" \
                         "3. {1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: '23', 5: 'Computer', 6: 'France'}\n" \
                         "\r\n"

        self.assertEqual(print_expected, print_actual)
        self.assertEqual(expected_return_value, actual_return_value)
