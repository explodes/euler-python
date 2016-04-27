#!/usr/bin/env python
from __future__ import absolute_import

import math as m
from euler.lib.seq import insert_in_order
from euler.lib.gen import lrange


def product(seq):
    """
    Multiply each item in the list and return the value
    """
    total_product = 1
    for item in seq:
        total_product *= item
    return total_product


def divisors(n):
    """
    List all divisors for a given integer
    """
    # a number is always divisible by one and itself
    all_divisors = [1] if n == 1 else [1, n]

    # we could skip even numbers if our input is odd
    # but profiling has shown no performance gains event for large values of `n`

    # search up to the sqrt of our value
    for divisor in lrange(2, int(m.sqrt(n)) + 1):
        if n % divisor == 0:
            insert_in_order(all_divisors, divisor)
            # don't add the square root twice
            if divisor * divisor != n:
                insert_in_order(all_divisors, n / divisor)

    return all_divisors


def proper_divisors(n):
    """
    A proper divisor is a number below n that divides into n evenly.
    """
    d = divisors(n)
    if n in d:
        d.remove(n)
    return d


def sum_of_digits(n):
    """
    Compute the sum of all digits in a number
    """
    return sum(int(c) for c in str(n))


def factorial(n):
    """
    Compute n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    from euler.lib.timing import time


    @time
    def timed_divisors(n):
        return divisors(n)


    assert timed_divisors(4) == [1, 2, 4]
    assert timed_divisors(5) == [1, 5]
    assert timed_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220]
    assert timed_divisors(234262351) == [1, 67, 3496453, 234262351]
    # assert timed_divisors(1326443518324400147398873) == [1, 1152846547, 1150581160845859, 1326443518324400147398873]
