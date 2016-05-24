from __future__ import absolute_import

import math as m


def n_digits(n):
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
