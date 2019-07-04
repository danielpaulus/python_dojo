import unittest
import random
import string
import re

from src.simple.Medium01 import Medium01


class Test(unittest.TestCase):
    def setUp(self):
        self.medium = Medium01()

    def test_make_me_pass_01(self):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        random_number = random.randint(1, 100000)

        my_dictionary = {random_string: random_number}
        expected = '{{"{}": {}}}'.format(random_string, random_number)

        result = self.medium.make_me_pass01(my_dictionary)
        self.assertEqual(result, expected)

    def test_make_me_pass_02(self):
        letters = string.ascii_lowercase
        fake_email = ''.join(random.choice(letters) for i in range(10))
        my_login = {"email": fake_email, "password": 123456789}
        email_regex = '/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/'
        test = re.search(my_login["email"], email_regex)
        result = self.medium.make_me_pass02(my_login)
        self.assertEqual(result, test)