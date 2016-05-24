#!/usr/bin/env python
from __future__ import absolute_import

import math as m


def num_digits(n):
    """
    Count the number of digits in a number
    """
    if n == 0:
        return 1
    return int(m.floor(m.log10(n))) + 1


def digits_of(n):
    """
    Generate each digit of a number, starting with the lowest digit
    """
    while n > 10:
        d = n % 10
        yield d
        n = (n - d) / 10
    yield n


if __name__ == '__main__':

    assert num_digits(0) == 1
    assert num_digits(1) == 1
    assert num_digits(9) == 1
    assert num_digits(10) == 2
    assert num_digits(11) == 2
    assert num_digits(99) == 2
    assert num_digits(100) == 3
    assert num_digits(101) == 3
