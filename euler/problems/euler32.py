#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register


@register
class Euler:
    """
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
    for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
    1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
    1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """
    NUMBER = 32
    NAME = "Pandigital products"
    ANSWER = None

    def run(self):
        return "NOT IMPLEMENTED"

    def test(self):
        pass


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
