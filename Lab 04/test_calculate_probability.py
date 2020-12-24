import io
from unittest import TestCase
from unittest.mock import patch
from letter_finder import calculate_probability


class TestCalculateProbability(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['1'], ['a'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_one_not_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['1'], ['g'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_two_one_all_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['2'], ['a', 'a'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_two_one_leading_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['2'], ['a', 'z'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.5 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_two_one_trailing_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['2'], ['z', 'a'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.5 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_two_not_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['2'], ['t', 'r'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_two_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['2'], ['a', 'r'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_two_not_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['2'], ['u', 'r'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_three_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['3'], ['a', 'b', 'c'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.3333 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_three_two_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['3'], ['a', 'a', 'c'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.6667 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_three_all_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['3'], ['a', 'a', 'a'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_three_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['3'], ['o', 'a', 'h'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.6667 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_three_two_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['3'], ['o', 'a', 'a'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_one_out_of_ten_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['1']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.1 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_ten_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.2 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_ten_two_leading_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.3778 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_ten_two_middle_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['z', 'b', 'a', 'd', 'e', 'f', 'g', 'a', 'i', 'j'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.3778 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_ten_two_trailing_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['z', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'a'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.3778 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_ten_three_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['z', 'b', 'c', 'd', 'a', 'f', 'g', 'a', 'i', 'a'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.5333 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_ten_five_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'a', 'd', 'a', 'f', 'g', 'a', 'i', 'a'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.7778 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_two_out_of_ten_seven_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'a', 'd', 'a', 'a', 'g', 'a', 'a', 'a'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.9333 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_three_out_of_ten_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['3']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.3 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_three_out_of_ten_three_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['z', 'b', 'c', 'd', 'a', 'f', 'g', 'a', 'i', 'a'], ['3']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.7083 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_three_out_of_ten_five_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'a', 'd', 'a', 'f', 'g', 'a', 'i', 'a'], ['3']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.9167 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_three_out_of_ten_seven_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'a', 'd', 'a', 'a', 'g', 'a', 'a', 'a'], ['3']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.9917 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_five_out_of_ten_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['5']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.5 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_five_out_of_ten_three_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['z', 'b', 'c', 'd', 'a', 'f', 'g', 'a', 'i', 'a'], ['5']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.9167 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_five_out_of_ten_five_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'a', 'd', 'a', 'f', 'g', 'a', 'i', 'a'], ['5']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.996 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_five_out_of_ten_seven_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'a', 'd', 'a', 'a', 'g', 'a', 'a', 'a'], ['5']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_seven_out_of_ten_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['7']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.7 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_seven_out_of_ten_three_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'a', 'e', 'f', 'g', 'a', 'i', 'j'], ['7']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.9917 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_seven_out_of_ten_five_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'a', 'e', 'f', 'a', 'a', 'i', 'a'], ['7']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_finder_calculate_probability_pick_ten_out_of_ten_one_a(self, mock_output):
        string_to_find = 'a'
        letters_list = [['10'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['10']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "1.0 probability that a pair of items selected will contain one or more 'a'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_b_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = 'b'
        letters_list = [['4'], ['b', 'a', 'b', 'c'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more 'b'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_c_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = 'c'
        letters_list = [['4'], ['a', 'c', 'b', 'c'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more 'c'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_z_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = 'z'
        letters_list = [['4'], ['e', 'z', 'a', 'z'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more 'z'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_A_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = 'A'
        letters_list = [['4'], ['A', 'A', 'a', 'z'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more 'A'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_Z_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = 'Z'
        letters_list = [['4'], ['A', 'Z', 'Z', 'z'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more 'Z'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_asterisk_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = '*'
        letters_list = [['4'], ['*', '*', '?', '>'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more '*'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_number_7_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = '7'
        letters_list = [['4'], ['2', '3', '7', '7'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more '7'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tab_key_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = '\t'
        letters_list = [['4'], ['\t', '3', '\t', '7'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more '\t'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_quotation_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = "'"
        letters_list = [['4'], ["'", '3', "'", 'a'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more '\''\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_double_quotation_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = '"'
        letters_list = [['4'], ['"', '3', '"', 'C'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more '\"'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_a_to_z_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = 'abcdefghijklmnopqrstuvwxyz'
        letters_list = [['4'], ['abcdefghijklmnopqrstuvwxyz', '3', 'abcdefghijklmnopqrstuvwxyz', 'C'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain " \
                          "one or more 'abcdefghijklmnopqrstuvwxyz'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_A_to_Z_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letters_list = [['4'], ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'a-z', 'C'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain " \
                          "one or more 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\n"
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_0_to_9_finder_calculate_probability_pick_two_out_of_four(self, mock_output):
        string_to_find = '0123456789'
        letters_list = [['4'], ['0123456789', 'A-Z', '0123456789', 'C'], ['2']]
        calculate_probability(string_to_find, letters_list)
        actual_output = mock_output.getvalue()
        expected_output = "0.8333 probability that a pair of items selected will contain one or more '0123456789'\n"
        self.assertEqual(expected_output, actual_output)
