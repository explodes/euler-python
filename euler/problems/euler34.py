#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register


@register
class Euler:
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    NUMBER = 34
    NAME = "Digit factorials"
    ANSWER = None

    def run(self):
        return "NOT IMPLEMENTED"

    def test(self):
        pass


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
