#!/usr/bin/env python
import math


def num_digits(n):
    """
    Count the number of digits in a number
    """
    if n == 0:
        return 1
    digits = math.log10(n)
    digits = math.floor(digits)
    digits = int(digits) + 1  # convert to int
    return digits


def digits_of(n):
    """
    Generate each digit of a number, starting with the lowest digit
    """
    while n >= 10:
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

    assert list(digits_of(10203)) == [3, 0, 2, 0, 1]
    assert list(digits_of(1023)) == [3, 2, 0, 1]
    assert list(digits_of(123)) == [3, 2, 1]
    assert list(digits_of(321)) == [1, 2, 3]
