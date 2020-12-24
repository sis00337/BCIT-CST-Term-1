from unittest import TestCase
from letter_finder import process_data
from io import StringIO


class TestProcessEachLineOfText(TestCase):
    def test_process_data_empty_text(self):
        file_object = StringIO('')
        actual_return = process_data(file_object)
        expected_return = []
        self.assertEqual(expected_return, actual_return)

    def test_process_data_a_line_of_text(self):
        file_object = StringIO('Hello\n')
        actual_return = process_data(file_object)
        expected_return = [['Hello']]
        self.assertEqual(expected_return, actual_return)

    def test_process_data_space_separated(self):
        file_object = StringIO('H e l l o\n')
        actual_return = process_data(file_object)
        expected_return = [['H', 'e', 'l', 'l', 'o']]
        self.assertEqual(expected_return, actual_return)

    def test_process_data_empty_multi_lines_of_text(self):
        file_object = StringIO('\n\n\n\n\n\n\n')
        actual_return = process_data(file_object)
        expected_return = [[''], [''], [''], [''], [''], [''], ['']]
        self.assertEqual(expected_return, actual_return)

    def test_process_data_multi_lines_of_text(self):
        file_object = StringIO('1 23\nHello World !\nThis is Unit testing\n')
        actual_return = process_data(file_object)
        expected_return = [['1', '23'], ['Hello', 'World', '!'], ['This', 'is', 'Unit', 'testing']]
        self.assertEqual(expected_return, actual_return)
