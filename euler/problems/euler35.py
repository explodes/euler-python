#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register


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
    ANSWER = None

    def run(self):
        return "NOT IMPLEMENTED"

    def test(self):
        pass


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
