from unittest import TestCase
from books import find_valid_shelves


class TestFindValidShelves(TestCase):

    def test_find_valid_shelves_remove_duplicates(self):
        books_tuple = ({'Shelf': '10'}, {'AA': 'Mike', 'Shelf': '10'}, {'Shelf': 'AA'}, {'Shelf': 'AA', 2: 'Cat'})
        actual = find_valid_shelves(books_tuple)
        expected = ['10', 'AA']
        self.assertEqual(expected, actual)

    def test_find_valid_shelves_numeric_sorting(self):
        books_tuple = ({'Shelf': '1'}, {1: 100, 'Shelf': '2'}, {'Shelf': '3'})
        actual = find_valid_shelves(books_tuple)
        expected = ['1', '2', '3']
        self.assertEqual(expected, actual)

    def test_find_valid_shelves_alphabetic_sorting(self):
        books_tuple = ({'Shelf': 'A'}, {1: 100, 'Shelf': 'B'}, {'Shelf': 'C'})
        actual = find_valid_shelves(books_tuple)
        expected = ['A', 'B', 'C']
        self.assertEqual(expected, actual)

    def test_find_valid_shelves_numeric_alphabetic_sorting(self):
        books_tuple = ({'Shelf': '11'}, {1: 100, 'Shelf': '20'}, {'Shelf': 'C'}, {2: 'Dog', 'Shelf': 'Z'})
        actual = find_valid_shelves(books_tuple)
        expected = ['11', '20', 'C', 'Z']
        self.assertEqual(expected, actual)
