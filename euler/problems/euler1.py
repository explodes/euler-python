#!/usr/bin/env python
from euler.problems.registry import register


def threeFives():
    return sum(x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0)


@register
class Euler:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    NUMBER = 1
    NAME = "Multiples of 3 and 5"
    ANSWER = 233168

    def run(self):
        return threeFives()

    def test(self):
        pass


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
