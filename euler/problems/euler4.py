#!/usr/bin/env python
from euler.lib.strings import is_palindrome
from euler.problems.registry import register


def num_is_palindrome(n):
    return is_palindrome(str(n))


def max_palindrome():
    m = None
    for x in xrange(100, 999 + 1):
        for y in xrange(100, 999 + 1):
            n = x * y
            if num_is_palindrome(n):
                if m is None or n > m:
                    m = n
    return m


@register
class Euler:
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    NUMBER = 4
    NAME = "Largest palindrome product"
    ANSWER = 906609

    def run(self):
        return max_palindrome()

    def test(self):
        assert num_is_palindrome(101)
        assert num_is_palindrome(123321)
        assert num_is_palindrome(1234321)
        assert not num_is_palindrome(1010)
        assert not num_is_palindrome(10110)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
