#!/usr/bin/env python
# coding=utf-8
from itertools import permutations

from euler.lib.backtrack import Permutations, SolutionHandler
from euler.lib.gen import item_n
from euler.problems.registry import register

DIGITS = '0123456789'
TARGET = 1000000


class Perms(Permutations, SolutionHandler):
    n = 0
    limit = 0
    solution = None

    def perms(self, items, limit):
        self.n = 0
        self.limit = limit
        self.solution = None
        self.find_permutations(items)

    def report_solution(self, solution):
        self.n += 1
        if self.n > self.limit:
            self.solution = ''.join(solution)
            self.finished = True


def lex_perm_number_hard(s, n):
    # ~7.7s usually
    p = Perms()
    p.perms(s, n)
    return p.solution


def lex_perms_easy(s):
    # ~0.44s usually
    # really cheating using the builtin..
    for x in permutations(s):
        yield ''.join(x)


def lex_perm_number_easy(s, n):
    return item_n(lex_perms_easy(s), n)


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
        return lex_perm_number_easy(DIGITS, TARGET - 1)

    def test(self):
        assert '3124' in tuple(lex_perms_easy('1234'))
        assert tuple(lex_perms_easy('012')) == ('012', '021', '102', '120', '201', '210')
        assert lex_perm_number_easy('012', 0) == '012'
        assert lex_perm_number_easy('012', 5) == '210'

        assert lex_perm_number_hard('012', 0) == '012'
        assert lex_perm_number_hard('012', 5) == '210'


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
