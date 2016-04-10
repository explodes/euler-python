#!/usr/bin/env python
from euler.problems.registry import register


def is_palindrome(n):
    s = str(n)
    n = len(s) / 2
    for i in xrange(n):
        if not s[i] == s[-(i + 1)]:
            return False
    return True


def max_palindrome():
    m = None
    for x in xrange(100, 1000):
        for y in xrange(100, 1000):
            n = x * y
            if is_palindrome(n):
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
        assert is_palindrome(101)
        assert is_palindrome(123321)
        assert is_palindrome(1234321)
        assert not is_palindrome(1010)
        assert not is_palindrome(10110)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
