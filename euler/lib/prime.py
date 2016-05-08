#!/usr/bin/env python
from __future__ import absolute_import

from math import sqrt

from euler.lib.mem import memoize


@memoize()
def factors(n):
    """
    Get all prime factors for a number.
    This function is recursive and memoized for performance.
    """
    m = int(sqrt(n))
    for i in xrange(2, m + 1):
        if n % i == 0:
            f = []
            f.extend(factors(i))
            f.extend(factors(n / i))
            return f
    return [n]


def is_prime(n):
    """
    Return whether or not `n` is prime
    """
    if n < 0:
        n = -n
    return len(factors(n)) == 1


def prime_gen():
    """
    Generate prime numbers in order starting with 2
    """
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    primes = {}
    n = 2
    while True:
        if n not in primes:
            yield n  # hasn't been marked not-prime
            primes[n * n] = [n]
        else:
            for prime in primes[n]:
                primes.setdefault(prime + n, []).append(prime)  # sieve
            del primes[n]  # won't revisit the prime again, clear memory
        n += 1


if __name__ == '__main__':
    assert is_prime(7)
    assert factors(7) == [7]
    assert factors(7) == [7]
    assert factors(144) == [2, 2, 2, 2, 3, 3]
    assert is_prime(131)
    assert not is_prime(144)
    assert is_prime(7)
    assert not is_prime(8)
