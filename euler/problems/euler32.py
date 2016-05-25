#!/usr/bin/env python
# coding=utf-8
from euler.lib.num import digits_of, num_digits
from euler.lib.profile import Timer
from euler.problems.registry import register

SUM_ONE_THRU_NINE = sum(range(1, 9 + 1))


def is_pandigital(min_value, max_value, *nums):
    # optimize like crazy, this is really slow with 10,000 x 10,000 calls
    N = 0
    digit_set = set()

    for num in nums:

        digits = list(digits_of(num))

        digit_set.update(digits)
        N += len(digits)

        if len(digit_set) != N:
            # duplicate found
            # break early
            return False

    return N == (max_value - min_value + 1) and min(digit_set) == min_value and max(digit_set) == max_value


def is_pandigital_sum(*nums):
    N = 0
    s = 0
    for num in nums:
        N += num_digits(num)

    if N != 9:
        return False

    for num in nums:
        for digit in digits_of(num):
            s += digit

    return s == SUM_ONE_THRU_NINE


def is_pandigital_map(*nums):
    s = set(''.join(map(str, nums)))
    return len(s) == 9


def pan_products():
    timer = Timer()
    found_products = set()

    for a in xrange(1, 10000):
        timer.start()
        for b in xrange(1, 10000):
            product = a * b
            if product not in found_products and is_pandigital_sum(a, b, a * b):
                found_products.add(product)
                yield product
        timer.end("pan of %d (%d total found products)" % (a, len(found_products)))
        if a % 100 == 0:
            timer.log()


def pan_products_fast():
    timer = Timer()

    found_products = set()

    for a in xrange(1, 10000):

        timer.start()

        a_digits = list(digits_of(a))
        a_digit_set = set(a_digits)
        if len(a_digits) == len(a_digit_set):

            for b in xrange(1, 10000):

                b_digits = list(digits_of(b))
                b_digit_set = set(b_digits)
                if len(b_digits) == len(b_digit_set):

                    p = a * b
                    if p not in found_products:

                        p_digits = list(digits_of(a * b))
                        p_digit_set = set(p_digits)
                        if len(p_digits) == len(p_digit_set):

                            if len(a_digit_set) + len(b_digit_set) + len(p_digit_set) == 9:
                                found_products.add(p)
                                yield p

        timer.end("pan-fast of %d (%d total found products)" % (a, len(found_products)))
        if a % 50 == 0:
            timer.log()


def sum_pan_products():
    return sum(pan_products_fast())


@register
class Euler:
    """
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
    for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
    1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
    1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """
    NUMBER = 32
    NAME = "Pandigital products"
    ANSWER = None

    def run(self):
        return None  # sum_pan_products()

    def test(self):
        assert is_pandigital(0, 4, 43210)
        assert is_pandigital(0, 4, 10342)
        assert is_pandigital(1, 5, 12345)
        assert is_pandigital(1, 5, 15234)
        assert is_pandigital(1, 9, 39, 186, 7254)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
