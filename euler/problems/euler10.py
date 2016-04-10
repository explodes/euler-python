#!/usr/bin/env python
from euler.lib.prime import prime_gen
from euler.problems.registry import register

LIMIT = 2000000


def sum_of_primes(below):
    s = 0
    primes = prime_gen()
    while True:
        prime = next(primes)
        if prime < below:
            s += prime
        else:
            return s


@register
class Euler:
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    NUMBER = 10
    NAME = "Summation of primes"

    def run(self):
        return sum_of_primes(LIMIT)

    def test(self):
        assert sum_of_primes(10) == 17


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
