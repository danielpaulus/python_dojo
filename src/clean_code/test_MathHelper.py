import unittest
import logging
import sys
from src.clean_code.MathHelper import MathHelper


class Test(unittest.TestCase):

    def setUp(self):
        self.math_helper = MathHelper()

    def test_find_largest_number_in_list_random_numbers(self):
        example_list = [4, 9, 2, 4, 99, 2, 1, 1, 1, 1, 0, 0, 2]
        expected = 99
        actual = self.math_helper.find_largest_number_in_list(example_list)
        self.assertEqual(expected, actual)

    def test_find_largest_number_in_list_empty_list(self):
        example_list = []
        expected = -sys.maxsize - 1
        actual = self.math_helper.find_largest_number_in_list(example_list)
        self.assertEqual(expected, actual)

    def test_find_largest_number_in_list_all_equal(self):
        example_list = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = 1
        actual = self.math_helper.find_largest_number_in_list(example_list)
        self.assertEqual(expected, actual)

    def test_find_largest_number_in_list_negative(self):
        example_list = [-4, -99, -7, -23, 0]
        expected = 0
        actual = self.math_helper.find_largest_number_in_list(example_list)
        self.assertEqual(expected, actual)
