#!/usr/bin/env python
# coding=utf-8
from euler.lib.strings import is_palindrome
from euler.problems.registry import register

LIMIT = 1000000


def num_is_palindrome(n):
    return is_palindrome(str(n))


def binary_is_palindrom(n):
    seq = bin(n)
    seq = seq[2:]  # trim off leading 0b
    return is_palindrome(seq)


def is_double_palindromic(n):
    return num_is_palindrome(n) and binary_is_palindrom(n)


def palindrome_sums(limit):
    s = 0
    for n in xrange(1, limit):
        if is_double_palindromic(n):
            s += n
    return s


@register
class Euler:
    """
    The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
    """
    NUMBER = 36
    NAME = "Double-base palindromes"
    ANSWER = 872187

    def run(self):
        return palindrome_sums(LIMIT)

    def test(self):
        assert num_is_palindrome(585)
        assert binary_is_palindrom(585)
        assert is_double_palindromic(585)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
