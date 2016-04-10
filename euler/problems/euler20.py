#!/usr/bin/env python
from euler.lib.math import factorial, sum_of_digits
from euler.problems.registry import register

VALUE = 100


def sum_of_factorial_digits(n):
    return sum_of_digits(factorial(n))


@register
class Euler:
    """
    n! means n * (n - 1) * ... * 3 * 2 * 1

    For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """
    NUMBER = 20
    NAME = "Factorial digit sum"

    def run(self):
        return sum_of_factorial_digits(VALUE)

    def test(self):
        assert sum_of_factorial_digits(10) == 3628800


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
