#!/usr/bin/env python
from euler.lib.math import sum_of_digits
from euler.problems.registry import register

EXPONENT = 1000


def sum_of_exponent(n):
    return sum_of_digits(2 ** n)


@register
class Euler:
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
    """
    NUMBER = 16
    NAME = "Power digit sum"
    ANSWER = 1366

    def run(self):
        return sum_of_exponent(EXPONENT)

    def test(self):
        assert sum_of_exponent(15) == 26


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
