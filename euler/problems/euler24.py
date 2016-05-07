#!/usr/bin/env python
# coding=utf-8
from itertools import permutations
from euler.lib.gen import item_n
from euler.problems.registry import register

DIGITS = '0123456789'
TARGET = 1000000


def lex_perms(s):
    # really cheating using the builtin..
    # todo: roll your own
    for x in permutations(s):
        yield ''.join(x)


def lex_perm_number(s, n):
    return item_n(lex_perms(s), n)


@register
class Euler:
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
    digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    NUMBER = 24
    NAME = "Lexicographic permutations"
    ANSWER = '2783915460'

    def run(self):
        return lex_perm_number(DIGITS, TARGET - 1)

    def test(self):
        assert '3124' in tuple(lex_perms('1234'))
        assert tuple(lex_perms('012')) == ('012', '021', '102', '120', '201', '210')
        assert lex_perm_number('012', 0) == '012'
        assert lex_perm_number('012', 5) == '210'


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
