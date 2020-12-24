from unittest import TestCase
from books import convert_book_list_to_tuple


class TestTupleMaker(TestCase):

    def test_convert_book_list_to_tuple_one_element(self):
        original_list = ([{1: 'Dog', 2: 'Cat'}])
        actual = convert_book_list_to_tuple(original_list)
        expected = ({1: 'Dog', 2: 'Cat'},)
        self.assertEqual(expected, actual)

    def test_convert_book_list_to_tuple_empty_values(self):
        original_list = ([{1: '', 2: '', 3: ''}])
        actual = convert_book_list_to_tuple(original_list)
        expected = ({1: 'None', 2: 'None', 3: 'None'},)
        self.assertEqual(expected, actual)

    def test_convert_book_list_to_tuple_multiple_elements(self):
        original_list = ([{1: 'Dog', 2: 'Cat'}, {'A': 'Chicken', 'B': 'Pizza', 'C': 'Hamburger'}])
        actual = convert_book_list_to_tuple(original_list)
        expected = ({1: 'Dog', 2: 'Cat'}, {'A': 'Chicken', 'B': 'Pizza', 'C': 'Hamburger'})
        self.assertEqual(expected, actual)
