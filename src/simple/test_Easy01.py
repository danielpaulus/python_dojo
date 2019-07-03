import unittest
import logging

from src.simple.Easy01 import Easy01


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("test")

    @classmethod
    def tearDownClass(cls):
        logging.info("test")

    def setUp(self):
        self.easy = Easy01()

    def test_get_me_to_pass01(self):
        initial_x = self.easy.x
        self.easy.get_me_to_pass01()
        changed_x = self.easy.x

        self.assertGreater(changed_x, initial_x)

    def test_get_me_to_pass02_positive(self):
        my_list = [1, 2, 3]
        expected_list = [2, 4, 6]
        self.easy.get_me_to_pass02(my_list)
        self.assertListEqual(my_list, expected_list)

    def test_get_me_to_pass02_empty(self):
        my_list = []
        self.easy.get_me_to_pass02(my_list)
        self.assertListEqual(my_list, [])

    def test_get_me_to_pass02_weird_input(self):
        with self.assertRaises(Exception) as context:
            self.easy.get_me_to_pass02("hey")

        self.assertTrue('Malformed input' in context.exception)


