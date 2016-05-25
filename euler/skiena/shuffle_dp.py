#!/usr/bin/env python
# coding=utf-8
from euler.lib.profile import time


def is_shuffle(x, y, z):
    """
    Is z a shuffle of x and y?

    If z is a merging of x and y, preserving the ordering of x and y

    e.g.  {a12c3, 1abc23, ...} subset-of shuffles(abc, 123)
    """

    len_x = len(x)
    len_y = len(y)
    len_z = len(z)

    if len_z != len_x + len_y:
        return False

    M = [None] * ((len_x + 1) * (len_y + 1))

    def at(i, j):
        return i + j * (len_x + 1)

    def printM():
        print_map = {
            True: "✓",
            False: "✗",
            None: "?"
        }
        print '  0',
        for c in y:
            print c,
        print
        for i in xrange(len_x + 1):
            if i == 0:
                print '0',
            else:
                print x[i - 1],
            for j in xrange(len_y + 1):
                key = M[at(i, j)]
                print print_map.get(key, key),
            print

    for i in xrange(len_x + 1):
        M[at(i, 0)] = True

    for j in xrange(len_y + 1):
        M[at(0, j)] = True

    for i in xrange(1, len_x + 1):
        for j in xrange(1, len_y + 1):
            prev_is_shuffle = M[at(i - 1, j)] or M[at(i, j - 1)]

            next_char_index = (i - 1) + (j - 1)
            next_char = z[next_char_index]

            next_is_shuffle = next_char == x[i - 1] or next_char == y[j - 1]

            M[at(i, j)] = next_char if prev_is_shuffle and next_is_shuffle else False

    printM()

    return M[at(i, j)]


"""
x 0 c h i p
-----------
0 ✓ ✓ ✓ ✓ ✓
c ✓ v
h ✓
o ✓
c ✓
o ✓
l ✓
a ✓
t ✓
e ✓
"""


@time
def is_shuffle_recursive(x, y, z, Xi=0, Yi=0):
    # basis case: impossible shuffle- mismatched lengths
    if len(z) != len(x) + len(y):
        return False

    # basis case: end of the run, last characters from X and Y picked
    if len(z) == Xi + Yi:
        return True

    # whether or not a letter can be picked from X or Y
    x_ok = Xi < len(x) and x[Xi] == z[Xi + Yi]
    y_ok = Yi < len(y) and y[Yi] == z[Xi + Yi]

    # pick a letter from X, and/or pick a letter from Y
    return (x_ok and is_shuffle_recursive(x, y, z, Xi + 1, Yi)) or \
           (y_ok and is_shuffle_recursive(x, y, z, Xi, Yi + 1))


if __name__ == '__main__':

    func = is_shuffle

    assert not func('chocolate', 'chips', 'abc')
    assert func('aaa', 'aaa', 'aaaaaa')
    assert not func('aaa', 'aaa', 'aaaaab')
    assert func('chocolate', 'chips', 'chocolatechips')
    assert func('chocolate', 'chips', 'chipschocolate')
    assert func('chocolate', 'chips', 'cchocohilaptes')
    assert not func('chocolate', 'chips', 'chocochilatspe')

    n = 100
    assert func('a' * n, 'a' * n, 'a' * (2 * n))
