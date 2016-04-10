#!/usr/bin/env python
from euler.lib.gen import first_n, item_n
from euler.lib.prime import prime_gen
from euler.problems.registry import register

LIMIT = 10001


def first_n_primes(n):
    return first_n(prime_gen(), n)


def nth_prime(n):
    return item_n(prime_gen(), n - 1)


@register
class Euler:
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10001st prime number?
    """
    NUMBER = 7
    NAME = "10001st prime"
    ANSWER = 104743

    def run(self):
        return nth_prime(LIMIT)

    def test(self):
        assert first_n_primes(6) == [2, 3, 5, 7, 11, 13]
        assert nth_prime(6) == 13
        assert nth_prime(100) == 541
        assert nth_prime(1000) == 7919


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
