from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta


DEFAULT_SETUP_DURATION = timedelta(minutes=60)
DEFAULT_TURNOVER_DURATION = timedelta(minutes=35)


WEEKDAY_HOURS = (time(hour=8), time(hour=23))
WEEKEND_HOURS = (time(hour=10, minute=30), time(hour=23, minute=30))


def get_default_hours():
    return {
        # day of the week (int): hours
        # starting with Monday => 0
        0: WEEKDAY_HOURS,
        1: WEEKDAY_HOURS,
        2: WEEKDAY_HOURS,
        3: WEEKDAY_HOURS,
        4: WEEKEND_HOURS,
        5: WEEKEND_HOURS,
        6: WEEKEND_HOURS,
    }


@dataclass(frozen=True)
class Theater:
    hours: dict = field(default_factory=get_default_hours)
    setup_duration: timedelta = field(default=DEFAULT_SETUP_DURATION)
    turnover_duration: timedelta = field(default=DEFAULT_TURNOVER_DURATION)

    def get_hours(self, day: date):
        start, end = self.hours[day.weekday()]

        # Convert start and end times into a datetime
        # Including setup time in hours
        start_dt = datetime.combine(day, start) + self.setup_duration
        end_dt = datetime.combine(day, end)

        return start_dt, end_dt
