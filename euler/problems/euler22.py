#!/usr/bin/env python
# coding=utf-8
import os
from euler.problems.registry import register

FILE = "p022_names.txt"


def read_names():
    with open(os.path.join(os.path.dirname(__file__), FILE), "r") as names:
        text = names.read()
    return text.replace('"', '').split(",")


def sorted_names():
    return sorted(read_names())


def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)


def scores():
    for index, name in enumerate(sorted_names()):
        s = (index + 1) * name_score(name)
        yield s


def sum_scores():
    return sum(scores())


@register
class Euler:
    """
    Using names.txt, a 46K text file containing over five-thousand
    first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
    the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """
    NUMBER = 22
    NAME = "Names scores"
    ANSWER = 871198282

    def run(self):
        return sum_scores()

    def test(self):
        assert name_score("COLIN") == 53


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
