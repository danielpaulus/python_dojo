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


if __name__ == '__main__':
    unittest.main()
