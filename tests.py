#!/usr/bin/python3

import stringClassifier as sc
import unittest

class TestStringMethods(unittest.TestCase):

    def test_maxLen(self):
        self.assertEqual(sc.maxLen(["aa", "aaaa"]), 4)

if __name__ == '__main__':
    unittest.main()
