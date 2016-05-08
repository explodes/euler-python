#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register

LIMIT = 1000000


def sum_of_powers(a, n):
    s = 0
    while a > 0:
        rem = a % 10
        s += rem ** n
        a = (a - rem) / 10
    return s


def is_sum_of_powers(a, n):
    return sum_of_powers(a, n) == a


def is_sum_of_powers_gen(n, limit):
    for i in xrange(2, limit + 1):
        if is_sum_of_powers(i, n):
            yield i


def sum_of_sum_of_powers(n, limit):
    return sum(is_sum_of_powers_gen(n, limit))


@register
class Euler:
    """
    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 14 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
    """
    NUMBER = 30
    NAME = "Digit fifth powers"
    ANSWER = 443839

    def run(self):
        return sum_of_sum_of_powers(5, LIMIT)

    def test(self):
        assert sum_of_powers(1634, 4) == 1634
        assert is_sum_of_powers(1634, 4)

        assert sum_of_powers(8208, 4) == 8208
        assert is_sum_of_powers(8208, 4)

        assert sum_of_powers(9474, 4) == 9474
        assert is_sum_of_powers(9474, 4)

        assert sum_of_sum_of_powers(4, 10000)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
