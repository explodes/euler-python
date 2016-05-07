#!/usr/bin/env python
# coding=utf-8
from euler.lib.math import proper_divisors
from euler.lib.mem import memoize
from euler.problems.registry import register

LIMIT = 28123


def abundance(n):
    """
    Determine the abundance of a number.
    An abundant number is a number where the sum of its proper divisors is greater than the number
    An deficient number is a number where the sum of its proper divisors is less than the number
    An perfect number is a number where the sum of its proper divisors is equal to the number
    :param n: number to determine its abundance status
    :return: <0 for deficient numbers. 0 for perfect numbers. >0 for abundant numbers
    """
    divisors = proper_divisors(n)
    return sum(divisors) - n


@memoize()
def is_abundant(n):
    return abundance(n) > 0


def can_be_sum_of_two_abundant_numbers(n):
    for i in xrange(1, n / 2 + 1):
        if is_abundant(i):
            j = n - i
            if is_abundant(j):
                return True
    return False


def sum_of_numbers_cant_be_sum_of_two_abundant_numbers(limit):
    s = 0
    for i in xrange(limit + 1):
        if not can_be_sum_of_two_abundant_numbers(i):
            s += i
    return s


@register
class Euler:
    """
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
    that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called
    abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
    sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than
    28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further
    by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
    numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """
    NUMBER = 23
    NAME = "Non-abundant sums"
    ANSWER = 4179871

    def run(self):
        return sum_of_numbers_cant_be_sum_of_two_abundant_numbers(LIMIT)

    def test(self):
        assert abundance(28) == 0
        assert abundance(12) > 0
        assert is_abundant(12)
        assert can_be_sum_of_two_abundant_numbers(24)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
