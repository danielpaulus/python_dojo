#TODO: Please write a test for my Anagram function

import unittest
from src.clean_code.StringHelper import StringHelper

class Test(unittest.TestCase):

    def setUp(self):
        self.string_helper =  StringHelper()
        self.anagram1 = "mary"
        self.anagram2 = "amry"

    def test_strings_are_anagrams_random_anagram(self):
        result = self.string_helper.strings_are_anagrams(self.anagram1, self.anagram2)
        self.assertTrue(result)

    def test_strings_are_anagrams_empty_string(self):
        example_string_1 = "Here comes dots"
        example_string_2 = ""
        result = self.string_helper.strings_are_anagrams(example_string_1, example_string_2)
        self.assertFalse(result)

    def test_strings_are_anagrams_anagram_capitalized(self):
        anagram_capitalized = "Amry"
        result = self.string_helper.strings_are_anagrams(self.anagram1, anagram_capitalized)
        self.assertTrue(result)

    def test_strings_are_anagrams_integer(self):
        example_int = 2
        self.assertRaises(TypeError, self.string_helper.strings_are_anagrams, self.anagram1, example_int )



