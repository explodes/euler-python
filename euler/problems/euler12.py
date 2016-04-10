#!/usr/bin/env python
from euler.lib.gen import item_n, first_n
from euler.lib.math import divisors
from euler.problems.registry import register

DIVISORS = 500


def triangle_gen():
    s = 0
    i = 1
    while True:
        s += i
        i += 1
        yield s


def first_triangle_number_with_n_divisors(n):
    for triangle_number in triangle_gen():
        d = divisors(triangle_number)
        num_divisors = len(d)
        if num_divisors >= n:
            return triangle_number


@register
class Euler:
    """
    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    """
    NUMBER = 12
    NAME = "Highly divisible triangular number"
    ANSWER = 76576500

    def run(self):
        return first_triangle_number_with_n_divisors(DIVISORS)

    def test(self):
        assert divisors(1) == [1]
        assert divisors(3) == [1, 3]
        assert divisors(6) == [1, 2, 3, 6]
        assert divisors(10) == [1, 2, 5, 10]
        assert divisors(15) == [1, 3, 5, 15]
        assert divisors(21) == [1, 3, 7, 21]
        assert divisors(28) == [1, 2, 4, 7, 14, 28]

        assert item_n(triangle_gen(), 6) == 28
        assert first_n(triangle_gen(), 10) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        assert first_triangle_number_with_n_divisors(5) == 28


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
