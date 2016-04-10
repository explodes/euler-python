def factors(n):
    """
    Get all prime factors for a number
    :param n: Number to get a list of factors for
    :param f:
    :return:
    """
    factors = []
    divisor = 2
    while divisor <= n / 2:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
    factors.append(n)
    return factors


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
