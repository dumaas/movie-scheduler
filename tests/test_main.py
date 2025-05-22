from unittest import TestCase
from src.main import main


class TestMain(TestCase):
    def test_hello_world(self):
        res = main()
        self.assertEqual(res, "Hello World!")
