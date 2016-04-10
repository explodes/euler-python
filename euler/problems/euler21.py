#!/usr/bin/env python
# coding=utf-8
from euler.lib.mem import memoize
from euler.lib.math import divisors
from euler.problems.registry import register

VALUE = 100


@memoize()
def mem_divisors(n):
    return divisors(n)


def proper_divisors(n):
    d = mem_divisors(n)
    if n in d:
        d.remove(n)
    return d


def sum_proper_divisors(n):
    return sum(proper_divisors(n))


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
    ANSWER = "unknown"

    def run(self):
        pass

    def test(self):
        assert proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
        assert sum_proper_divisors(220) == 284
        assert proper_divisors(284) == [1, 2, 4, 71, 142]
        assert sum_proper_divisors(284) == 220


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
