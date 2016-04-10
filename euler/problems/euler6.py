#!/usr/bin/env python
from euler.problems.registry import register

LIMIT = 100


def sum_of_squares(n):
    return sum(x ** 2 for x in xrange(1, n + 1))


def sum_squared(n):
    return sum(xrange(1, n + 1)) ** 2


@register
class Euler:
    """
    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and
    the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and
    the square of the sum.
    """
    NUMBER = 6
    NAME = "Sum square difference"
    ANSWER = 25164150

    def run(self):
        return sum_squared(LIMIT) - sum_of_squares(LIMIT)

    def test(self):
        assert sum_of_squares(10) == 385
        assert sum_squared(10) == 3025
        assert sum_squared(10) - sum_of_squares(10) == 2640


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
