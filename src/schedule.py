from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import date, timedelta

from src.movie import Movie
from src.theater import Theater


@dataclass
class Schedule:
    day: date
    theater: Theater
    showtimes: dict = field(default_factory=lambda: defaultdict(deque))

    def generate_showtimes(self, movie: Movie):
        """
        - Prioritize 'prime-time' (evening) over earlier times
        - Show as many times as possible
        - 1 screen per movie
        - Pretty start times (5-minute increments)
        - Showtime must start and end within business hours
        """
        start, end = self.theater.get_hours(self.day)
        curr = end

        while curr >= start:
            # Get the start time of the next showing
            curr -= movie.duration
            # Round to the next 'pretty' number
            # 3:27 -> 3:25
            minutes_to_subtract = curr.minute % 5
            curr -= timedelta(minutes=minutes_to_subtract)

            # Check if start time is valid
            if curr < start:
                break

            # Include showtime in the list (start, end)
            self.showtimes[movie].appendleft((curr, curr + movie.duration))

            # Take turnover time into account
            curr -= self.theater.turnover_duration

    def print_showtimes(self):
        """
        Thursday 12/31/2015

        There's Something About Mary - Rated R, 2:14
            12:15 - 14:29
            15:05 - 17:19
            17:55 - 20:09
            20:45 - 22:59

        High Fidelity - Rated R, 1:54
            ...
        """
        # Print the current day
        print("\n")
        print(f"{self.day.strftime('%A')} {self.day.strftime('%m/%d/%y')}")

        for movie in self.showtimes:
            print("\n")
            print(f"{movie.title} - Rated {movie.rating}, {movie.runtime}")
            for start, end in self.showtimes[movie]:
                print(f"\t{start.strftime('%H:%M')} - {end.strftime('%H:%M')}")
