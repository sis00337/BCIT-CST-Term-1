from unittest import TestCase
from books import search_helper


class TestSearchHelper(TestCase):

    def test_search_by_key_num_1_helper(self):
        books = ({1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
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
        keyword = 'j'
        menu_num = 1
        user_input = 1

        actual_return_value = search_helper(books, keyword, menu_num, user_input)
        expected_return_value = [{1: 'James', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Joon', 2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]
        self.assertEqual(expected_return_value, actual_return_value)

    def test_search_by_key_num_2_helper(self):
        books = ({1: 'James', 2: 'Cat', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
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
        keyword = 'dog'
        menu_num = 2
        user_input = 2

        actual_return_value = search_helper(books, keyword, menu_num, user_input)
        expected_return_value = [{1: 'Chris', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Vincent', 2: 'Dog', 3: 'B', 4: 'C', 5: 'D', 6: 'E'}]
        self.assertEqual(expected_return_value, actual_return_value)

    def test_search_by_key_num_3_helper(self):
        books = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: 'C', 5: 'D', 6: 'E'},
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
        keyword = 'la'
        menu_num = 3
        user_input = 3

        actual_return_value = search_helper(books, keyword, menu_num, user_input)
        expected_return_value = [{1: 'Mike', 2: 'Deer', 3: 'Laptop', 4: 'C', 5: 'D', 6: 'E'},
                                 {1: 'Henry', 2: 'Sheep', 3: 'Calculator', 4: 'C', 5: 'D', 6: 'E'}]
        self.assertEqual(expected_return_value, actual_return_value)

    def test_search_by_key_num_4_helper_numeric_keyword(self):
        books = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'},
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
        keyword = '2'
        menu_num = 4
        user_input = 4

        actual_return_value = search_helper(books, keyword, menu_num, user_input)
        expected_return_value = [{1: 'Harry', 2: 'Cow', 3: 'Wallet', 4: '2', 5: 'D', 6: 'E'}]
        self.assertEqual(expected_return_value, actual_return_value)

    def test_search_by_key_num_4_helper_alphabetic_keyword(self):
        books = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'D', 6: 'E'},
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
        keyword = 'read'
        menu_num = 4
        user_input = 4

        actual_return_value = search_helper(books, keyword, menu_num, user_input)
        expected_return_value = [{1: 'Eiman', 2: 'Tiger', 3: 'Cup', 4: 'Reading', 5: 'D', 6: 'E'}]
        self.assertEqual(expected_return_value, actual_return_value)

    def test_search_by_key_num_5_helper(self):
        books = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'E'},
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
        keyword = 'sports'
        menu_num = 5
        user_input = 5

        actual_return_value = search_helper(books, keyword, menu_num, user_input)
        expected_return_value = [{1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'E'},
                                 {1: 'Dani', 2: 'Bat', 3: 'Bed', 4: '20', 5: 'Sports', 6: 'E'}]
        self.assertEqual(expected_return_value, actual_return_value)

    def test_search_by_key_num_6_helper(self):
        books = ({1: 'James', 2: 'Cat', 3: 'Chair', 4: '1', 5: 'Architecture', 6: 'South Korea'},
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
        keyword = 'united'
        menu_num = 6
        user_input = 6

        actual_return_value = search_helper(books, keyword, menu_num, user_input)
        expected_return_value = [{1: 'Chris', 2: 'Dog', 3: 'Desk', 4: '1', 5: 'Sports', 6: 'United States'},
                                 {1: 'Nicholas', 2: 'Lion', 3: 'Notebook', 4: 'Noguchi', 5: 'Style',
                                  6: 'United Kingdom'}]
        self.assertEqual(expected_return_value, actual_return_value)
