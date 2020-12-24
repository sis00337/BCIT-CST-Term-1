import io
import re
from unittest import TestCase
from unittest.mock import patch
from regex import find_hand


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_high_card(self, mock_output):
        hand = '87342'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is High Card\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_one_pair(self, mock_output):
        hand = 'tt789'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is One Pair\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_two_pairs(self, mock_output):
        hand = 'AATT2'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is Two Pairs\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_three_of_a_kind(self, mock_output):
        hand = 'KKKJQ'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is Three of a Kind\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_full_house(self, mock_output):
        hand = '666TT'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is Full House\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_four_of_a_kind(self, mock_output):
        hand = 'JJJJ9'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is Four of a Kind\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_lowest_straight_flush(self, mock_output):
        hand = '23456'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is Straight Flush\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_highest_straight_flush(self, mock_output):
        hand = 'AKQJT'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is Straight Flush\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_find_hand_not_straight_flush(self, mock_output):
        hand = 'QKA23'
        is_straight = re.compile(r'A2345|5432A|23456|65432|34567|76543|45678|87654|56789|98765|6789T|'
                                 r'T9876|789TJ|JT987|89TJQ|QJT98|9TJQK|KQJT9|TJQKA|AKQJT', re.I)
        is_four_of_a_kind = re.compile(r'([AKQJT2-9])\1{3}([AKQJT2-9])', re.I)
        is_three_repetition = re.compile(r'([AKQJT2-9])\1{2}([AKQJT2-9]){2}', re.I)
        is_two_repetition = re.compile(r'([AKQJT2-9])\1', re.I)
        find_hand(hand, is_straight, is_four_of_a_kind, is_three_repetition, is_two_repetition)
        expected_print = 'Your hand is High Card\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_print, actual_print)
