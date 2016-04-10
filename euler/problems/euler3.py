#!/usr/bin/env python
from euler.lib.prime import factors
from euler.problems.registry import register

VALUE = 600851475143


def max_factor(n):
    return max(factors(n))


@register
class Euler:
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    NUMBER = 3
    NAME = "Largest prime factor"
    ANSWER = 6857

    def run(self):
        return max_factor(VALUE)

    def test(self):
        assert factors(13195) == [5, 7, 13, 29]


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
