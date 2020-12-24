"""
03. Addition and Dot Products of Sparse Vectors
Unit tests for the dot product of sparse vectors
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : sis00337 (Delivery_KiKi)
"""


from unittest import TestCase
from sparse_vector import sparse_dot_product


class TestSparseVectorDotProduct(TestCase):

    def test_sparse_dot_product_including_zero_sum(self):
        first_vector = {0: -4, 1: 2, 2: 10, 'length': 3}
        second_vector = {0: 4, 1: 5, 'length': 3}
        expected = -6
        actual = sparse_dot_product(first_vector, second_vector)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_same_position(self):
        first_vector = {0: 2, 1: 5, 2: 10, 4: 5, 'length': 5}
        second_vector = {0: 5, 1: 10, 2: -4, 4: -2, 'length': 5}
        expected = 10
        actual = sparse_dot_product(first_vector, second_vector)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_different_position(self):
        first_vector = {2: 10, 4: 22, 6: 42, 'length': 10}
        second_vector = {0: 4, 3: 15, 7: 18, 9: -33, 'length': 10}
        expected = 0
        actual = sparse_dot_product(first_vector, second_vector)
        self.assertEqual(expected, actual)
