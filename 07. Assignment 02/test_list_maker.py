from unittest import TestCase
from books import list_maker


class TestListMaker(TestCase):

    def test_list_maker_empty_line(self):
        line = ''
        actual = list_maker(line)
        expected = ['']
        self.assertEqual(expected, actual)

    def test_list_maker_a_line_of_string(self):
        line = 'I want to buy a backpack'
        actual = list_maker(line)
        expected = ['I want to buy a backpack']
        self.assertEqual(expected, actual)

    def test_list_maker_including_tab_keys(self):
        line = 'Blue\tRed\tWhite\tBlack\tGreen'
        actual = list_maker(line)
        expected = ['Blue', 'Red', 'White', 'Black', 'Green']
        self.assertEqual(expected, actual)

    def test_list_maker_including_tab_keys_and_newline_keys(self):
        line = 'Dog\tCat\n\tCow\tBat\n\tTiger\n'
        actual = list_maker(line)
        expected = ['Dog', 'Cat', 'Cow', 'Bat', 'Tiger']
        self.assertEqual(expected, actual)

    def test_list_maker_including_newline_keys(self):
        line = 'Dog\nCat\nCow\nBat\nTiger\n'
        actual = list_maker(line)
        expected = ['DogCatCowBatTiger']
        self.assertEqual(expected, actual)

    def test_list_maker_only_tab_keys(self):
        line = '\t\t\t\t\t\t\t\t\t\t\t'
        actual = list_maker(line)
        expected = ['', '', '', '', '', '', '', '', '', '', '', '']
        self.assertEqual(expected, actual)

    def test_list_maker_only_newline_keys(self):
        line = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
        actual = list_maker(line)
        expected = ['']
        self.assertEqual(expected, actual)
