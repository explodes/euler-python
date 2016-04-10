#!/usr/bin/env python
from euler.lib.mem import memoize
from euler.problems.registry import register


class Tree:
    def __init__(self, structure):
        self.rows = [map(lambda x: int(x, 10), row.strip().split()) for row in structure.strip().split('\n') if row]

    def __eq__(self, other):
        return self.rows == other.rows

    def __hash__(self):
        # used to hash the tree for memoization in _helper
        return id(self)

    def __getitem__(self, item):
        return self.rows[item]

    def __len__(self):
        return len(self.rows)

    @memoize()
    def _sum_helper(self, row, index):
        val = self[row][index]
        if row + 1 == len(self):
            return val
        left = self._sum_helper(row + 1, index)
        right = self._sum_helper(row + 1, index + 1)
        return val + max(left, right)

    def largest_sum_in_tree(self):
        return self._sum_helper(0, 0)


@register
class Euler:
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
    Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)
    """
    NUMBER = 18
    NAME = "Maximum path sum I"

    def run(self):
        tree = Tree("""
                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """)
        return tree.largest_sum_in_tree()

    def test(self):
        tree = Tree("""
       3
      7 4
     2 4 6
    8 5 9 3
    """)
        assert len(tree) == 4
        for index, row in enumerate(tree):
            assert len(row) == index + 1
        assert tree.largest_sum_in_tree() == 23


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
