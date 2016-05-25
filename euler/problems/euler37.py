#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register


@register
class Euler:
    """
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously
    remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
    work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """
    NUMBER = 37
    NAME = "Truncatable primes"
    ANSWER = None

    def run(self):
        return "NOT IMPLEMENTED"

    def test(self):
        pass


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
