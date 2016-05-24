#!/usr/bin/env python
from euler.lib.maths import product
from euler.lib.prime import factors
from euler.problems.registry import register

LIMIT = 20


def count(l, x):
    c = 0
    for i in l:
        if i == x:
            c += 1
    return c


def factor_count(f, n):
    s = 0
    for l in f:
        c = count(l, n)
        if c > s:
            s = c
    return s


def factor_list(n):
    f = []
    for i in xrange(2, n + 1):
        prime_factors = factors(i)
        f.append(prime_factors)
    return f


def most_frequent_factors(f, n):
    t = []
    for i in xrange(2, n + 1):
        c = factor_count(f, i)
        if n > 0:
            t.append(i ** c)
    return t


def collect_factors(n):
    f = factor_list(n)
    return most_frequent_factors(f, n)


def least_common_multiple(nums):
    return product(collect_factors(nums))


@register
class Euler:
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    NUMBER = 5
    NAME = "Smallest multiple"
    ANSWER = 232792560

    def run(self):
        return least_common_multiple(LIMIT)

    def test(self):
        assert factors(4) == [2, 2]
        assert count([1, 2, 3], 1) == 1
        assert count([1, 1, 3], 1) == 2
        assert count([1, 1, 1], 1) == 3

        assert least_common_multiple(1) == 1
        assert least_common_multiple(2) == 2
        assert least_common_multiple(3) == 6
        assert least_common_multiple(4) == 12
        assert least_common_multiple(10) == 2520


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
