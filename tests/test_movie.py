from unittest import TestCase
from datetime import timedelta
from parameterized import parameterized
from src.movie import Movie


class TestMovie(TestCase):
    def mock_row(self, title, year, rating, runtime):
        return dict(
            title=title,
            year=year,
            rating=rating,
            runtime=runtime,
        )

    @parameterized.expand([
        ("Mock Title", "2025", "PG", "1:30", timedelta(minutes=90)),
    ])
    def test_from_row(self, title, year, rating, runtime, duration):
        row = self.mock_row(title, year, rating, runtime)
        res = Movie.from_row(row)

        self.assertEqual(res.title, title)
        self.assertEqual(res.year, int(year))
        self.assertEqual(res.rating, rating)
        self.assertEqual(res.runtime, runtime)
        self.assertEqual(res.duration, duration)

    def test_parse_movies_from_file(self):
        filename = "sample_input.txt"
        movies = Movie.parse_movies_from_file(filename)

        self.assertEqual(len(movies), 7)
