#!/usr/bin/env python
from collections import namedtuple

from euler.lib.gen import item_n
from euler.problems.registry import register

START_DATE = (1901, 0)
END_DATE = (2000, 11)
SUNDAY = 0
MONDAY = 1
Month = namedtuple("Month", ["year", "month", "day_of_week"])

always_30 = lambda year: 30
february = lambda year: 29 if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0) else 28
always_31 = lambda year: 31
DAYS_IN_MONTH = [
    always_31,  # jan
    february,  # feb
    always_31,  # mar
    always_30,  # apr
    always_31,  # may
    always_30,  # jun
    always_31,  # jul
    always_31,  # aug
    always_30,  # sep
    always_31,  # oct
    always_30,  # nov
    always_31,  # dec
]


def month_gen():
    year = 1900
    month = 0
    day = MONDAY
    yield Month(year, month, MONDAY)
    while True:
        day += DAYS_IN_MONTH[month](year)
        month += 1
        if month > 11:
            month = 0
            year += 1
        yield Month(year, month, day % 7)


def month_range(start_year, start_month, end_year, end_month):
    gen = month_gen()

    while True:
        month = next(gen)
        if month.year == start_year and month.month == start_month:
            break

    while True:
        month = next(gen)
        yield month
        if month.year == end_year and month.month == end_month:
            break


def num_sundays(start_year, start_month, end_year, end_month):
    count = 0
    for month in month_range(start_year, start_month, end_year, end_month):
        if month.day_of_week == SUNDAY:
            count += 1
    return count


@register
class Euler:
    """
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """
    NUMBER = 19
    NAME = "Counting Sundays"

    def run(self):
        return num_sundays(START_DATE[0], START_DATE[1], END_DATE[0], END_DATE[1])

    def test(self):
        assert item_n(month_gen(), 0).day_of_week == MONDAY
        assert num_sundays(2015, 0, 2015, 11) == 3
        assert num_sundays(2016, 0, 2016, 11) == 1


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
