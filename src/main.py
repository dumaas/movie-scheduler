import argparse
import os
from datetime import date
from pathlib import Path

from src.movie import Movie
from src.schedule import Schedule
from src.theater import Theater


def validate_filename(filename: str) -> Path:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} does not exist.")
    return Path(filename)


def main(filename: Path) -> None:
    print(filename)

    # 1. Parse movies from file
    movies = Movie.parse_movies_from_file(filename)

    # 2. Generate schedule for the theater on a given day
    theater = Theater()
    schedule = Schedule(day=date.today(), theater=theater)
    for movie in movies:
        schedule.generate_showtimes(movie)

    # 3. Print the schedule
    schedule.print_showtimes()


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="sample_input.txt", type=validate_filename)
    args = parser.parse_args()

    main(args.filename)
