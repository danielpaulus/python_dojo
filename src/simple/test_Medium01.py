import unittest
import random
import string

from src.simple.Medium01 import Medium01


class Test(unittest.TestCase):
    def setUp(self):
        self.medium = Medium01()

    def test_make_me_pass_01(self):
        letters = string.ascii_lowercase
        r_string = ''.join(random.choice(letters) for i in range(10))
        r_number = random.randint(1, 100000)
        my_dictionary = {r_string: r_number}
        expected = '{{"{}":{}}}'.format(r_string, r_number)

        result = self.medium.make_me_pass01(my_dictionary)
        self.assertEqual(result, expected)
