"""
COMP 1510
Final Exam - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


from unittest import TestCase
from yahtzee import sum_score


class TestSumScore(TestCase):

    def test_sum_score_arbitrary_key_value(self):
        player_score = {'ab': 1, 2: 2, 'Small Straight': 3, 'AB': 4}
        expected_return = 10
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_upper_section_below_63(self):
        player_score = {'Aces': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6, 'Yahtzee': 0}
        expected_return = 21
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_upper_section_equal_to_63(self):
        player_score = {'Aces': 3, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Yahtzee': 0}
        expected_return = 98
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_greater_than_63(self):
        player_score = {'Aces': 4, 'Twos': 8, 'Threes': 9, 'Fours': 12, 'Fives': 20, 'Sixes': 24, 'Yahtzee': 0}
        expected_return = 112
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_one_yahtzee(self):
        player_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 1}
        expected_return = 50
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_two_yahtzee(self):
        player_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 2}
        expected_return = 150
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_three_yahtzee(self):
        player_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Yahtzee': 3}
        expected_return = 250
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_full_score_sheet_minimum_score(self):
        player_score = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0,
                        'Three of a kind': 0, 'Four of a kind': 0, 'Full House': 0, 'Small straight': 0,
                        'Large straight': 0, 'Chance': 5, 'Yahtzee': 0}
        expected_return = 5
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_full_score_sheet_maximum_score_one_yahtzee(self):
        player_score = {'Aces': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30,
                        'Three of a kind': 30, 'Four of a kind': 30, 'Full House': 25, 'Small straight': 30,
                        'Large straight': 40, 'Chance': 30, 'Yahtzee': 1}
        expected_return = 375
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)

    def test_sum_score_full_score_sheet_maximum_score_two_yahtzee(self):
        player_score = {'Aces': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30,
                        'Three of a kind': 30, 'Four of a kind': 30, 'Full House': 25, 'Small straight': 30,
                        'Large straight': 40, 'Chance': 30, 'Yahtzee': 2}
        expected_return = 475
        actual_return = sum_score(player_score)
        self.assertEqual(expected_return, actual_return)
