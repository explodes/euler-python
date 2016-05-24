#!/usr/bin/env python
# coding=utf-8
from euler.lib.mem import memoize
from euler.problems.registry import register


@memoize(memoize_on=lambda value, options, start=0: (value, start))
def num_comprising_combinations(value, options, start=0):
    num_variations = 0
    for index in xrange(start, len(options)):
        option = options[index]
        if value == option:
            num_variations += 1
        elif value > option:
            num_variations += num_comprising_combinations(value - option, options, index)

    return num_variations


@register
class Euler:
    """
    In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
    """
    NUMBER = 31
    NAME = "Coin sums"
    ANSWER = None

    def run(self):
        return num_comprising_combinations(200, [1, 2, 5, 10, 20, 50, 100, 200])

    def test(self):
        def test_num_comprising_combinations(value, options, expected):
            result = num_comprising_combinations(value, options)
            assert result == expected, 'possibilites(%d, %s) was %d not %d' % (value, options, result, expected)

        test_num_comprising_combinations(10, [], 0)
        test_num_comprising_combinations(10, [11], 0)
        test_num_comprising_combinations(10, [10], 1)
        test_num_comprising_combinations(10, [5, 10], 2)  # 0,0 + 1
        test_num_comprising_combinations(10, [5, 5, 10], 4)  # possible combos: 0,0 + 0,1 + 1,1 + 2 # NOT 1,0 also.
        test_num_comprising_combinations(10, [1, 10], 2)


if __name__ == '__main__':
    euler = Euler()
    # euler.test()
    print euler.run()
