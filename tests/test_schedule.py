from unittest import TestCase

from src.theater import Theater


class TestSchedule(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.theater = Theater()

    def test_generate_showtimes(self):
        movie = self.mock_movie()
        schedule = Schedule()
