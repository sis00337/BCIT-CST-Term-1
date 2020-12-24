from unittest import TestCase
from regex import is_nakamoto


class TestIsNakamoto(TestCase):

    def test_is_nakamoto_empty_string(self):
        name = ''
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_first_name_uppercase(self):
        name = 'WONDER Nakamoto'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_first_name_lowercase(self):
        name = 'wonder Nakamoto'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_first_name_numbers(self):
        name = '1234 Nakamoto'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_first_name_mr(self):
        name = 'Mr. Nakamoto'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_first_name_title_case(self):
        name = 'Wonder Nakamoto'
        expected = True
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_first_name_camel_case(self):
        name = 'wonderWoman Nakamoto'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_last_name_correct_format(self):
        name = 'Santa Nakamoto'
        expected = True
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_last_name_not_nakamoto(self):
        name = 'Santa Nakamura'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_last_name_lowercase(self):
        name = 'Santa nakamoto'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_last_name_uppercase(self):
        name = 'Santa NAKAMOTO'
        expected = False
        actual = is_nakamoto(name)
        self.assertEqual(expected, actual)
