"""
03. Addition and Dot Products of Sparse Vectors
Unit tests for the addition of sparse vectors
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : sis00337 (Delivery_KiKi)
"""


from unittest import TestCase
from sparse_vector import sparse_add


class TestSparseVectorAdd(TestCase):

    def test_sparse_add_including_zero_sum(self):
        first_vector = {0: -4, 1: 2, 2: 10, 'length': 3}
        second_vector = {0: 4, 1: 5, 'length': 3}
        expected = {1: 7, 2: 10, 'length': 3}
        actual = sparse_add(first_vector, second_vector)
        self.assertEqual(expected, actual)

    def test_sparse_add_same_position(self):
        first_vector = {0: 77, 2: 80, 4: -77, 'length': 5}
        second_vector = {0: -7, 2: 25, 4: 7, 'length': 5}
        expected = {0: 70, 2: 105, 4: -70, 'length': 5}
        actual = sparse_add(first_vector, second_vector)
        self.assertEqual(expected, actual)

    def test_sparse_add_different_position(self):
        first_vector = {2: 10, 4: 22, 7: 42, 'length': 10}
        second_vector = {0: 4, 3: 90, 7: 18, 9: -33, 'length': 10}
        expected = {0: 4, 2: 10, 3: 90, 4: 22, 7: 60, 9: -33, 'length': 10}
        actual = sparse_add(first_vector, second_vector)
        self.assertEqual(expected, actual)
