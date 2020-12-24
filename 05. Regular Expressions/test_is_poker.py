import io
from unittest import TestCase
from unittest.mock import patch
from regex import is_poker


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_empty_hand(self, mock_output):
        hand = ''
        expected_return = False
        actual_return = is_poker(hand)
        expected_print = 'Your hand is not valid\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_five_same_cards(self, mock_output):
        hand = '22222'
        expected_return = False
        actual_return = is_poker(hand)
        expected_print = 'Your hand is not valid\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_six_cards(self, mock_output):
        hand = 'AKQJT9'
        expected_return = False
        actual_return = is_poker(hand)
        expected_print = 'Your hand is not valid\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_not_poker_cards(self, mock_output):
        hand = 'abcde'
        expected_return = False
        actual_return = is_poker(hand)
        expected_print = 'Your hand is not valid\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_high_card(self, mock_output):
        hand = 'a34tq'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is High Card\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_one_pair(self, mock_output):
        hand = '77AKQ'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is One Pair\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_two_pairs(self, mock_output):
        hand = 'KKQQ2'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is Two Pairs\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_three_of_a_kind(self, mock_output):
        hand = '66689'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is Three of a Kind\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_full_house(self, mock_output):
        hand = 'TTT22'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is Full House\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_four_of_a_kind(self, mock_output):
        hand = '4444K'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is Four of a Kind\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_straight_flush(self, mock_output):
        hand = '23456'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is Straight Flush\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_highest_straight_flush(self, mock_output):
        hand = 'AKQJT'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is Straight Flush\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_poker_not_straight_flush(self, mock_output):
        hand = 'JQKA2'
        expected_return = True
        actual_return = is_poker(hand)
        expected_print = 'Your hand is High Card\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)
