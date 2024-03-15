import unittest
from dict2 import dict2, KeyNotFoundException

class TestDict2(unittest.TestCase):
    def test_store_and_access(self):
        obj = dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        self.assertEqual(obj['a'], 1)
        self.assertEqual(obj['b'], 2)
        self.assertEqual(obj['c'], 3)

    def test_access_nonexistent_key(self):
        obj = dict2()
        with self.assertRaises(KeyNotFoundException):
            _ = obj['nonexistent']

    def test_iteration(self):
        obj = dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        keys = [k for k in obj]
        self.assertListEqual(keys, ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()
