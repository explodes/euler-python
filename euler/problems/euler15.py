#!/usr/bin/env python
from euler.lib.mem import memoize
from euler.problems.registry import register

WIDTH = 20
HEIGHT = 20


@memoize()
def num_combos(width, height):
    if width == 0:
        return 1
    if height == 0:
        return 1
    down_moves = num_combos(width, height - 1)
    right_moves = num_combos(width - 1, height)
    return down_moves + right_moves


@register
class Euler:
    """
    Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20*20 grid?
    """
    NUMBER = 15
    NAME = "Lattice paths"

    def run(self):
        return num_combos(WIDTH, HEIGHT)

    def test(self):
        assert num_combos(1, 1) == 2
        assert num_combos(2, 2) == 6


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
