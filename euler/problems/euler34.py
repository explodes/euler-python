#!/usr/bin/env python
# coding=utf-8
from euler.lib.math import factorial
from euler.lib.mem import memoize
from euler.problems.registry import register

LIMIT = 100000


@memoize()
def factorial_mem(n):
    return factorial(n)


def digits_of(n):
    while n > 10:
        d = n % 10
        yield d
        n = (n - d) / 10
    yield n


def is_curious(n):
    return n == sum(factorial_mem(d) for d in digits_of(n))


def curious_gen(limit):
    for x in xrange(3, limit + 1):
        if is_curious(x):
            yield x


def curious_sum(limit):
    return sum(curious_gen(limit))


@register
class Euler:
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    NUMBER = 34
    NAME = "Digit factorials"
    ANSWER = 40730

    def run(self):
        return curious_sum(LIMIT)

    def test(self):
        def test_digits_of(n, expected):
            result = list(digits_of(n))
            assert result == expected, 'digits_of(%d) == %s, not %s' % (n, result, expected)

        test_digits_of(1, [1])
        test_digits_of(12, [2, 1])
        test_digits_of(123, [3, 2, 1])
        test_digits_of(145, [5, 4, 1])

        assert is_curious(145)
        assert 145 in curious_gen(145)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
