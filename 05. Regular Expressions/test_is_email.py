from unittest import TestCase
from regex import is_email


class TestIsEmail(TestCase):

    def test_is_email_empty_address(self):
        address = ''
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_uppercase(self):
        address = 'ABC'
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_lowercase(self):
        address = 'abc'
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_numbers(self):
        address = '1234'
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_username_part_uppercase(self):
        address = 'STRONG@def.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_username_part_lowercase(self):
        address = 'strong@def.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_username_part_numbers(self):
        address = '98765@def.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_username_part_underscore(self):
        address = '_____@def.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_username_part_combination(self):
        address = 'strong_MAN@def.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_domain_part_uppercase(self):
        address = 'strong_MAN@CANADA.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_domain_part_lowercase(self):
        address = 'strong_MAN@canada.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_domain_part_numbers(self):
        address = 'strong_MAN@12345.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_domain_part_underscores(self):
        address = 'strong_MAN@_____.ghi'
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_domain_part_correct_combination(self):
        address = 'strong_MAN@canadaCOVID19.ghi'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_domain_part_wrong_combination(self):
        address = 'strong_MAN@canada_COVID19.ghi'
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_uppercase(self):
        address = 'strong_MAN@canada.COM'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_lowercase(self):
        address = 'strong_MAN@canada.com'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_numbers(self):
        address = 'strong_MAN@canada.123'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_special_characters(self):
        address = 'strong_MAN@canada.@#_'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_one_character(self):
        address = 'strong_MAN@canada.A'
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_two_characters(self):
        address = 'strong_MAN@canada.A4'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_three_characters(self):
        address = 'strong_MAN@canada.A4%'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_four_characters(self):
        address = 'strong_MAN@canada.A4%C'
        expected = True
        actual = is_email(address)
        self.assertEqual(expected, actual)

    def test_is_email_dot_com_part_five_characters(self):
        address = 'strong_MAN@canada.A4%CB'
        expected = False
        actual = is_email(address)
        self.assertEqual(expected, actual)
