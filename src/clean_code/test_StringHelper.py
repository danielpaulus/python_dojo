#TODO: Please write a test for my Anagram function

import unittest
from src.clean_code.StringHelper import StringHelper

class Test(unittest.TestCase):

    def setUp(self):
        self.string_helper =  StringHelper()

    def test_strings_are_anagrams_random_anagram(self):
        example_string_1 = "mary"
        example_string_2 = "amry"
        expected = True
        actual = self.string_helper.strings_are_anagrams(example_string_1, example_string_2)
        self.assertEqual(expected, actual)

    def test_strings_are_anagrams_empty_string(self):
        example_string_1 = "Here comes dots"
        example_string_2 = ""
        expected = False
        actual = self.string_helper.strings_are_anagrams(example_string_1, example_string_2)
        self.assertEqual(expected, actual)

    #def test_strings_are_anagrams_anagram_capitalized(self)

