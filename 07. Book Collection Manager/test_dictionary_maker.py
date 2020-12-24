from unittest import TestCase
from books import dictionary_maker


class TestDictionaryMaker(TestCase):

    def test_dictionary_maker_empty_values(self):
        key = [1, 2, 3]
        line_list = ['', '', '']
        actual = dictionary_maker(key, line_list)
        expected = {1: '', 2: '', 3: ''}
        self.assertEqual(expected, actual)

    def test_dictionary_maker_same_keys(self):
        key = [1, 1, 1]
        line_list = ['Dog', 'Cat', 'Cow']
        actual = dictionary_maker(key, line_list)
        expected = {1: 'Cow'}
        self.assertEqual(expected, actual)

    def test_dictionary_maker_same_values(self):
        key = [1, 2, 3]
        line_list = ['Dog', 'Dog', 'Dog']
        actual = dictionary_maker(key, line_list)
        expected = {1: 'Dog', 2: 'Dog', 3: 'Dog'}
        self.assertEqual(expected, actual)

    def test_dictionary_maker_longer_values(self):
        key = ['A', 'B', 'C', 'D', 'E']
        line_list = ['Eyes', 'Nose', 'Mouth']
        actual = dictionary_maker(key, line_list)
        expected = {'A': 'Eyes', 'B': 'Nose', 'C': 'Mouth'}
        self.assertEqual(expected, actual)
