#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register


@register
class Euler:
    """
    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
    """
    NUMBER = 36
    NAME = "Double-base palindromes"
    ANSWER = None

    def run(self):
        return "NOT IMPLEMENTED"

    def test(self):
        pass


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
