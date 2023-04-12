import unittest
from sparsevector import sparse_dot_product


class TestDot(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sparse_dot_product({}, {}), 0)

    def test_single_key_vectors(self):
        self.assertEqual(sparse_dot_product({0: 1}, {0: 4}), 4)

    def test_two_key_vectors(self):
        self.assertEqual(sparse_dot_product({0: 1}, {0: 4}), 4)

    def test_three_key_vectors(self):
        self.assertEqual(sparse_dot_product({0: 1, 1: 1, 2: 2}, {0: 4, 1: 3, 2: 2}), 11)

    def test_no_common_keys(self):
        self.assertEqual(sparse_dot_product({0: 1, 2: 3}, {1: 5, 3: 6}), 0)

    def test_couple_common_keys(self):
        self.assertEqual(sparse_dot_product({0: 1, 2: 3}, {0: 4, 1: 5, 2: 6}), 22)

    def test_all_common_keys(self):
        self.assertEqual(sparse_dot_product({0: 1, 1: 2, 2: 3}, {0: 4, 1: 5, 2: 6}), 32)

    def test_zero_values(self):
        self.assertEqual(sparse_dot_product({0: 0, 1: 0, 2: 0}, {0: 4, 1: 5, 2: 6}), 0)

    def test_all_common_keys_with_some_negatives(self):
        self.assertEqual(sparse_dot_product({0: -1, 1: -2, 2: -3}, {0: -4, 1: 5, 2: -6}), 12)