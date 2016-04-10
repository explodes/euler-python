#!/usr/bin/env python
from euler.lib.math import product
from euler.problems.registry import register

TARGET = 1000


def triplet(n, search_delta=10):
    min_search = 1
    max_search = min_search + search_delta
    while True:
        for a in range(min_search, max_search + 1):
            for b in range(min_search, max_search + 1):
                c = n - (a + b)
                # if it is a triplet
                if a * a + b * b == c * c:
                    return a, b, c
        min_search += search_delta
        max_search += search_delta


def triplet_product(n):
    return product(triplet(n))


@register
class Euler:
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    NUMBER = 9
    NAME = "Special Pythagorean triplet"

    def run(self):
        return product(triplet(TARGET, search_delta=TARGET))

    def test(self):
        assert product(triplet(3 + 4 + 5)) == 3 * 4 * 5


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
