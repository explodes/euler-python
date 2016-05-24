#!/usr/bin/env python
# coding=utf-8

from euler.lib.num import n_digits
from euler.lib.prime import is_prime
from euler.problems.registry import register

LIMIT = 1000000


def rotations_gen(n):
    digits = n_digits(n)
    pow_10 = 10 ** (digits - 1)
    for digit in xrange(digits):
        yield n
        # take the lowest digit
        d = n % 10

        # remove it
        n -= d
        n /= 10

        # add it to the beginning
        n += d * pow_10


def is_circular_prime(n):
    for rotation in rotations_gen(n):
        if not is_prime(rotation):
            return False
    return True


def circular_prime_count(limit):
    count = 0
    for n in xrange(2, limit + 1):
        if is_circular_prime(n):
            count += 1
    return count


@register
class Euler:
    """
    The number, 197, is called a circular prime because all rotations of the digits:
    197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
    """
    NUMBER = 35
    NAME = "Circular primes"
    ANSWER = 55

    def run(self):
        return circular_prime_count(LIMIT)

    def test(self):
        assert n_digits(0) == 1
        assert n_digits(1) == 1
        assert n_digits(10) == 2
        assert n_digits(11) == 2
        assert n_digits(19) == 2
        assert n_digits(99) == 2
        assert n_digits(100) == 3

        assert list(rotations_gen(197)) == [197, 719, 971]
        assert list(rotations_gen(1978)) == [1978, 8197, 7819, 9781]

        assert is_circular_prime(197)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
