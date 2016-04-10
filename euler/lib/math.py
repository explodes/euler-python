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
    all_divisors = [1] if n == 1 else [1, n]

    def add(i):
        """
        Insert i into `all_divisors` in order
        """
        for index in xrange(len(all_divisors)):
            if all_divisors[index] > i:
                all_divisors.insert(index, i)
                return
        all_divisors.append(i)

    divisor = 2
    limit = n / 2
    while divisor < limit:
        if n % divisor == 0:
            add(divisor)
            add(n / divisor)
            # optimization: search only to the highest divisor found
            limit = n / divisor
        divisor += 1
    return all_divisors


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
