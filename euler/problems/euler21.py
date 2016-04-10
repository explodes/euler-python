#!/usr/bin/env python
# coding=utf-8
from euler.lib.math import proper_divisors
from euler.problems.registry import register

LIMIT = 10000


def sum_proper_divisors(n):
    return sum(proper_divisors(n))


def amicable_numbers(below):
    # map numbers to sums
    d = {}
    for i in xrange(1, below):
        d[i] = sum_proper_divisors(i)

    # when a != b and d[b] = a and d[a] == b, a and b are amicable
    amicable = set()
    for number, s in d.iteritems():
        if not number == s and s in d and d[s] == number:
            amicable.add(number)
            amicable.add(s)

    return amicable


def sum_amicable_numbers(below):
    return sum(amicable_numbers(below))


@register
class Euler:
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b
    are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    NUMBER = 21
    NAME = "Amicable numbers"
    ANSWER = 31626

    def run(self):
        return sum_amicable_numbers(LIMIT)

    def test(self):
        assert proper_divisors(4) == [1, 2]
        assert proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
        assert sum_proper_divisors(220) == 284
        assert proper_divisors(284) == [1, 2, 4, 71, 142]
        assert sum_proper_divisors(284) == 220

        amicable = amicable_numbers(300)
        assert 220 in amicable
        assert 284 in amicable


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
