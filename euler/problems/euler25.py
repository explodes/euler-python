#!/usr/bin/env python
# coding=utf-8
from euler.lib.mem import memoize
from euler.problems.registry import register

DIGITS = 1000


@memoize()
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_with_digits(d):
    x = 1
    while True:
        f = fib(x)

        if len(str(f)) >= d:
            return x

        x += 1


@register
class Euler:
    """
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    NUMBER = 25
    NAME = "1000-digit Fibonacci number"
    ANSWER = 4782

    def run(self):
        return fib_with_digits(DIGITS)

    def test(self):
        assert fib(1) == 1
        assert fib(2) == 1
        assert fib(3) == 2
        assert fib(4) == 3
        assert fib(5) == 5
        assert fib(6) == 8
        assert fib(7) == 13
        assert fib(8) == 21
        assert fib(9) == 34
        assert fib(10) == 55
        assert fib(11) == 89
        assert fib(12) == 144
        assert fib_with_digits(3) == 12


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
