#!/usr/bin/env python
import os
from euler.problems.euler18 import Tree
from euler.problems.registry import register


def open_tree():
    fname = os.path.join(os.path.dirname(__file__), "euler67.txt")
    with open(fname) as tree_file:
        structure = tree_file.read()
        return Tree(structure)


@register
class Euler:
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
    from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text
    file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this
    problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take
    over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
    """
    NUMBER = 67
    NAME = "Maximum path sum II"
    ANSWER = 7273

    def run(self):
        return open_tree().largest_sum_in_tree()

    def test(self):
        tree = open_tree()
        for index, row in enumerate(tree):
            assert len(row) == index + 1


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
