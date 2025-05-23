from csv import DictReader
from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    rating: str
    runtime: str
    duration: timedelta

    @classmethod
    def from_row(cls, row):
        runtime = row["runtime"]  # 1:30
        hours, minutes = runtime.split(":")
        duration = timedelta(minutes=(int(hours) * 60 + int(minutes)))

        return cls(
            title=row["title"],
            year=int(row["year"]),
            rating=row["rating"],
            runtime=runtime,
            duration=duration,
        )

    @classmethod
    def parse_movies_from_file(cls, filename) -> list:
        movies = []

        with open(filename, "r") as f:
            reader = DictReader(f)
            for row in reader:
                movie = Movie.from_row(row)
                movies.append(movie)

        return movies
