#!/usr/bin/env python
# coding=utf-8

from euler.lib.prime import is_prime
from euler.problems.registry import register

BOUNDARY = 999


def quad_formula(a, b):
    def f(n):
        return n * n + a * n + b

    return f


def number_of_consecutive_primes(a, b):
    n = 0
    while True:
        if not is_prime(n * n + a * n + b):
            break
        n += 1
    return n


def longest_run_of_primes(a_min, a_max, b_min, b_max):
    longest_run = None
    longest_a, longest_b = None, None

    for a in xrange(a_min, a_max + 1):
        for b in xrange(b_min, b_max + 1):
            run = number_of_consecutive_primes(a, b)
            if longest_run is None or run > longest_run:
                longest_run = run
                longest_a, longest_b = a, b
    return longest_a, longest_b


def product_of_longest_run(a_min, a_max, b_min, b_max):
    a, b = longest_run_of_primes(a_min, a_max, b_min, b_max)
    return a * b


@register
class Euler:
    """
    Euler discovered the remarkable quadratic formula:

    n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
    However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly
    when n = 41, 41² + 41 + 41 is clearly divisible by 41.

    The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive
    values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4
    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
    primes for consecutive values of n, starting with n = 0.
    """
    NUMBER = 27
    NAME = "Quadratic primes"
    ANSWER = -59231

    def run(self):
        return product_of_longest_run(-BOUNDARY, BOUNDARY, -BOUNDARY, BOUNDARY)

    def test(self):
        assert number_of_consecutive_primes(1, 41) == 40
        assert number_of_consecutive_primes(-79, 1601) == 80
        assert product_of_longest_run(-79, -79, 1601, 1601) == -126479


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
