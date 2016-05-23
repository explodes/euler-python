#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register


def spiral_gen(side):
    if side == 0:
        return

    value = 1
    accum = 2

    yield 1
    for ring in xrange(1, side / 2 + 1):
        for i in xrange(4):
            value += accum
            yield value
        accum += 2


@register
class Euler:
    """
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
    [43] 44    45   46 47 48 [49]
     42 [21]  22  23  24 [25] 26
     41  20  [7]  8  [9]  10  27
     40  19   6  [1]  2   11  28
     39  18  [5]  4  [3]  12  29
     38 [17]  16  15  14 [13] 30
    [37] 36   35  34  33  32 [31]

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    """
    NUMBER = 28
    NAME = "Number spiral diagonals"
    ANSWER = 669171001

    def run(self):
        return sum(spiral_gen(1001))

    def test(self):
        def test_spiral_gen(side, expected):
            result = sum(spiral_gen(side))
            assert result == expected, "sprial_gen_sum(%d) was %d not %d" % (side, result, expected)

        test_spiral_gen(1, 1)
        test_spiral_gen(3, 25)
        test_spiral_gen(5, 101)


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
