#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register

LIMIT = 100


def a_to_b_gen(n):
    for a in xrange(2, n + 1):
        for b in xrange(2, n + 1):
            yield a ** b


def distinct_sorted_values_a_to_b(n):
    return sorted(set(a_to_b_gen(n)))


@register
class Euler:
    """
    Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    22=4, 23=8, 24=16, 25=32
    32=9, 33=27, 34=81, 35=243
    42=16, 43=64, 44=256, 45=1024
    52=25, 53=125, 54=625, 55=3125
    If they are then placed in numerical order, with any repeats removed, we get the following sequence
    of 15 distinct terms:

    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
    """
    NUMBER = 29
    NAME = "Distinct powers"
    ANSWER = 9183

    def run(self):
        return len(distinct_sorted_values_a_to_b(LIMIT))

    def test(self):
        assert distinct_sorted_values_a_to_b(5) == [4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125]


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
