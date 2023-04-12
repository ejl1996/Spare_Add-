import unittest
from sparsevector import sparse_add


class TestAdd(unittest.TestCase):
    def test_sparse_add_valid_and_weird_additions(self):
        # normal test case
        self.assertEqual(sparse_add({"length": 3, 0: 1, 2: 3}, {"length": 3, 0: 4, 1: 5, 2: 6}),
                         {'length': 3, 0: 5, 1: 5, 2: 9})
        # normal test case different order of keys
        self.assertEqual(sparse_add({0: 1, 2: 3, "length": 3}, {"length": 3, 0: 4, 1: 5, 2: 6}),
                         {'length': 3, 0: 5, 1: 5, 2: 9})
        # small test cases
        self.assertEqual(sparse_add({"length": 1, 0: 1}, {"length": 1, 0: -1}), {"length": 1, 0: 0})
        self.assertEqual(sparse_add({"length": 2, 0: 1, 1: 2}, {"length": 2}), {"length": 2, 0: 1, 1: 2})
        self.assertEqual(sparse_add({"length": 0}, {"length": 0}), {"length": 0})
        self.assertEqual(sparse_add({"length": 0}, {"length": 0}), {"length": 0})
        self.assertEqual(sparse_add({"length": 5, 0: 0, 1: 0}, {"length": 5}), {"length": 5, 0: 0, 1: 0})

    def test_sparse_add_invalid_wrong_values(self):
        with self.assertRaises(ValueError):
            sparse_add({"length": 8, 0: 1, 2: 3}, {"length": 4, 0: 4, 1: 5, 2: 6})

    def test_sparse_add_key_error(self):
        with self.assertRaises(KeyError):
            sparse_add({0: 1, 2: 3}, {"length": 3, 0: 4, 1: 5, 2: 6})
        with self.assertRaises(KeyError):
            sparse_add({"length": 3, 0: 1, 2: 3}, {0: 4, 1: 5, 2: 6})